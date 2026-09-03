"""Extract the stock Quake III arena and pickup catalogue from pak0.pk3."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import struct
import zipfile
from pathlib import Path
from typing import Iterator

SCHEMA_VERSION = 4
STOCK_MAP_KEYS = tuple(
    [f"q3dm{i}" for i in range(20)] + [f"q3tourney{i}" for i in range(1, 7)]
)
CPMA_MAP_KEYS = (
    "cpm1a",
    "cpm2",
    "cpm3",
    "cpm3a",
    "cpm4",
    "cpm4a",
    "cpm5",
    "cpm6",
    "cpm7",
    "cpm8",
    "cpm9",
    "cpm10",
    "cpm11",
    "cpm11a",
    "cpm12",
    "cpm13",
    "cpm14",
    "cpm15",
    "cpm16",
    "cpm17",
    "cpm18",
    "cpm18r",
    "cpm19",
    "cpm20",
    "cpm21",
    "cpm22",
    "cpm23",
    "cpm24",
    "cpm25",
    "cpm26",
    "cpm27",
    "cpm28",
    "cpm29",
    "cpma3",
)
MAP_KEYS = STOCK_MAP_KEYS + CPMA_MAP_KEYS

# Mirrors the base-game item classnames in the pinned bg_misc.c. Ammo belongs
# to its weapon permission because receiving unusable ammo is pointless.
ITEM_FAMILIES = {
    "item_armor_shard": "Armor",
    "item_armor_jacket": "Armor",
    "item_armor_combat": "Armor",
    "item_armor_body": "Armor",
    "item_health_small": "Health",
    "item_health": "Health",
    "item_health_large": "Health",
    "item_health_mega": "Mega Health",
    "weapon_shotgun": "Shotgun",
    "weapon_machinegun": "Machinegun",
    "weapon_grenadelauncher": "Grenade Launcher",
    "weapon_rocketlauncher": "Rocket Launcher",
    "weapon_lightning": "Lightning Gun",
    "weapon_railgun": "Railgun",
    "weapon_plasmagun": "Plasma Gun",
    "weapon_bfg": "BFG10K",
    "ammo_shells": "Shotgun",
    "ammo_bullets": "Machinegun",
    "ammo_grenades": "Grenade Launcher",
    "ammo_cells": "Plasma Gun",
    "ammo_lightning": "Lightning Gun",
    "ammo_rockets": "Rocket Launcher",
    "ammo_slugs": "Railgun",
    "ammo_bfg": "BFG10K",
    "holdable_teleporter": "Personal Teleporter",
    "holdable_medkit": "Medkit",
    "item_quad": "Quad Damage",
    "item_enviro": "Battle Suit",
    "item_haste": "Haste",
    "item_invis": "Invisibility",
    "item_regen": "Regeneration",
    "item_flight": "Flight",
}

ITEM_DISPLAY_NAMES = {
    "item_armor_shard": "Armor Shard",
    "item_armor_jacket": "Green Armor",
    "item_armor_combat": "Armor",
    "item_armor_body": "Heavy Armor",
    "item_health_small": "5 Health",
    "item_health": "25 Health",
    "item_health_large": "50 Health",
    "item_health_mega": "Mega Health",
    "weapon_shotgun": "Shotgun",
    "weapon_machinegun": "Machinegun",
    "weapon_grenadelauncher": "Grenade Launcher",
    "weapon_rocketlauncher": "Rocket Launcher",
    "weapon_lightning": "Lightning Gun",
    "weapon_railgun": "Railgun",
    "weapon_plasmagun": "Plasma Gun",
    "weapon_bfg": "BFG10K",
    "ammo_shells": "Shells",
    "ammo_bullets": "Bullets",
    "ammo_grenades": "Grenades",
    "ammo_cells": "Cells",
    "ammo_lightning": "Lightning",
    "ammo_rockets": "Rockets",
    "ammo_slugs": "Slugs",
    "ammo_bfg": "Bfg Ammo",
    "holdable_teleporter": "Personal Teleporter",
    "holdable_medkit": "Medkit",
    "item_quad": "Quad Damage",
    "item_enviro": "Battle Suit",
    "item_haste": "Speed",
    "item_invis": "Invisibility",
    "item_regen": "Regeneration",
    "item_flight": "Flight",
}

WEAPON_FAMILIES = (
    "Shotgun",
    "Machinegun",
    "Grenade Launcher",
    "Rocket Launcher",
    "Lightning Gun",
    "Railgun",
    "Plasma Gun",
    "BFG10K",
)
NONWEAPON_FAMILIES = (
    "Armor",
    "Health",
    "Mega Health",
    "Personal Teleporter",
    "Medkit",
    "Quad Damage",
    "Battle Suit",
    "Haste",
    "Invisibility",
    "Regeneration",
    "Flight",
)
MAJOR_POWERUP_FAMILIES = frozenset(
    (
        "Quad Damage",
        "Battle Suit",
        "Haste",
        "Invisibility",
        "Regeneration",
        "Flight",
    )
)

# The non-"Team Arena" portion of bg_itemlist in the pinned bg_misc.c. The three
# entries without unlock families do not spawn in the selected FFA/Tournament
# variants, but keeping them here makes an unexpected active occurrence fatal.
BASE_ITEM_CLASSNAMES = frozenset(ITEM_FAMILIES) | {
    "weapon_gauntlet",
    "weapon_grapplinghook",
    "team_CTF_redflag",
    "team_CTF_blueflag",
}


def tokenize(text: str) -> Iterator[str]:
    """Yield Quake info/entity tokens, including block braces."""
    index = 0
    length = len(text)
    while index < length:
        if text[index].isspace() or text[index] == "\0":
            index += 1
            continue
        if text.startswith("//", index):
            newline = text.find("\n", index + 2)
            index = length if newline < 0 else newline + 1
            continue
        if text[index] in "{}":
            yield text[index]
            index += 1
            continue
        if text[index] == '"':
            index += 1
            value: list[str] = []
            while index < length and text[index] != '"':
                if text[index] == "\\" and index + 1 < length:
                    index += 1
                value.append(text[index])
                index += 1
            if index >= length:
                raise ValueError("unterminated quoted token")
            index += 1
            yield "".join(value)
            continue
        end = index
        while end < length and not text[end].isspace() and text[end] not in "{}":
            end += 1
        yield text[index:end]
        index = end


def parse_blocks(text: str) -> list[dict[str, str]]:
    tokens = iter(tokenize(text))
    blocks: list[dict[str, str]] = []
    for token in tokens:
        if token != "{":
            raise ValueError(f"expected '{{', got {token!r}")
        block: dict[str, str] = {}
        while True:
            try:
                key = next(tokens)
            except StopIteration as error:
                raise ValueError("unterminated block") from error
            if key == "}":
                break
            if key == "{":
                raise ValueError("nested block")
            try:
                value = next(tokens)
            except StopIteration as error:
                raise ValueError(f"missing value for {key!r}") from error
            if value == "{" or value == "}":
                raise ValueError(f"invalid value for {key!r}")
            block[key] = value
        blocks.append(block)
    return blocks


def read_bsp_entities(data: bytes) -> list[dict[str, str]]:
    header_size = 8 + 17 * 8
    if len(data) < header_size:
        raise ValueError("BSP header is truncated")
    magic, version = struct.unpack_from("<4sI", data)
    if magic != b"IBSP" or version != 46:
        raise ValueError(f"unsupported BSP header {magic!r} version {version}")
    offset, size = struct.unpack_from("<ii", data, 8)
    if offset < header_size or size < 0 or offset + size > len(data):
        raise ValueError("BSP entity lump is out of bounds")
    return parse_blocks(data[offset : offset + size].decode("latin-1"))


def entity_is_active(entity: dict[str, str], game_type: str) -> bool:
    if int(entity.get("notfree", "0") or 0):
        return False
    if int(entity.get("notq3a", "0") or 0):
        return False
    allowed_types = entity.get("gametype")
    return allowed_types is None or game_type in allowed_types


def parse_origin(value: str, key: str, entity_index: int) -> list[int | float]:
    parts = value.split()
    if len(parts) != 3:
        raise ValueError(f"invalid pickup origin in {key} entity {entity_index + 1}")
    result: list[int | float] = []
    for part in parts:
        number = float(part)
        result.append(int(number) if number.is_integer() else number)
    return result


def parse_arenas(text: str) -> dict[str, dict[str, object]]:
    arenas: dict[str, dict[str, object]] = {}
    for block in parse_blocks(text):
        key = block.get("map")
        if not key:
            continue
        bots = block.get("bots", "").split() or ["sarge"]
        frag_limit = int(block.get("fraglimit", "0"))
        arenas[key] = {
            "name": block.get("longname", key),
            "bots": bots,
            "frag_limit": (
                frag_limit if 1 <= frag_limit <= 50 else min(20, 5 * (len(bots) + 1))
            ),
            "arena_types": block.get("type", "").split(),
        }
    return arenas


def build_pickups(
    entities: list[dict[str, str]], key: str, game_type: str
) -> list[dict[str, object]]:
    groups: dict[tuple[str, object], list[dict[str, object]]] = {}
    give_targets = {
        entity.get("target")
        for entity in entities
        if entity.get("classname") == "target_give"
        and entity.get("target")
        and entity_is_active(entity, game_type)
    }
    for entity_index, entity in enumerate(entities):
        classname = entity.get("classname", "")
        family = ITEM_FAMILIES.get(classname)
        if (
            classname in BASE_ITEM_CLASSNAMES
            and entity_is_active(entity, game_type)
            and not family
        ):
            raise ValueError(f"active item {classname!r} has no unlock family in {key}")
        if (
            not family
            or not entity_is_active(entity, game_type)
            or entity.get("targetname") in give_targets
        ):
            continue
        variant = {
            "bsp_entity_ordinal": entity_index + 1,
            "classname": classname,
            "origin": parse_origin(entity.get("origin", ""), key, entity_index),
            "display_name": ITEM_DISPLAY_NAMES[classname],
            "family": family,
        }
        group = (
            ("team", entity["team"]) if entity.get("team") else ("entity", entity_index)
        )
        groups.setdefault(group, []).append(variant)

    pickups = []
    for variants in groups.values():
        families = list(dict.fromkeys(variant["family"] for variant in variants))
        classnames = list(dict.fromkeys(variant["classname"] for variant in variants))
        display_names = list(
            dict.fromkeys(variant["display_name"] for variant in variants)
        )
        pickups.append(
            {
                **variants[0],
                "ordinal": len(pickups) + 1,
                "display_name": " / ".join(display_names),
                "families": families,
                "classnames": classnames,
                "variants": variants,
            }
        )
    return pickups


def build_traversals(
    entities: list[dict[str, str]], game_type: str
) -> list[dict[str, object]]:
    traversals = []
    counts = {"jump_pad": 0, "teleporter": 0}
    for entity_index, entity in enumerate(entities):
        classname = entity.get("classname")
        kind = (
            "jump_pad"
            if classname == "trigger_push"
            else "teleporter" if classname == "trigger_teleport" else None
        )
        if not kind or not entity_is_active(entity, game_type):
            continue
        if kind == "teleporter" and int(entity.get("spawnflags", "0") or 0) & 1:
            continue
        counts[kind] += 1
        traversals.append(
            {
                "ordinal": len(traversals) + 1,
                "kind_ordinal": counts[kind],
                "bsp_entity_ordinal": entity_index + 1,
                "kind": kind,
            }
        )
    return traversals


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def load_cpma_maps(
    baseq3_path: Path,
) -> tuple[dict[str, tuple[dict[str, object], list[dict[str, str]]]], dict[str, str]]:
    maps: dict[str, tuple[dict[str, object], list[dict[str, str]]]] = {}
    hashes: dict[str, str] = {}
    for path in sorted(baseq3_path.glob("map_*.pk3")):
        with zipfile.ZipFile(path) as archive:
            names = {name.lower(): name for name in archive.namelist()}
            arenas: dict[str, dict[str, object]] = {}
            for lower_name, name in names.items():
                if lower_name.endswith(".arena"):
                    arenas.update(parse_arenas(archive.read(name).decode("latin-1")))
            used = False
            for key in CPMA_MAP_KEYS:
                bsp_name = names.get(f"maps/{key}.bsp")
                if not bsp_name:
                    continue
                if key in maps:
                    raise ValueError(f"duplicate CPMA map {key}")
                if key not in arenas:
                    raise ValueError(
                        f"arena metadata is missing for {key} in {path.name}"
                    )
                maps[key] = (arenas[key], read_bsp_entities(archive.read(bsp_name)))
                used = True
            if used:
                hashes[path.name] = file_sha256(path)
    missing = set(CPMA_MAP_KEYS) - maps.keys()
    if missing:
        raise ValueError(f"CPMA maps are missing: {', '.join(sorted(missing))}")
    return maps, hashes


def build_catalog(pak0_path: Path) -> dict[str, object]:
    pak_hash = file_sha256(pak0_path)
    cpma_maps, cpma_hashes = load_cpma_maps(pak0_path.parent)
    with zipfile.ZipFile(pak0_path) as archive:
        arenas = parse_arenas(archive.read("scripts/arenas.txt").decode("latin-1"))
        maps: list[dict[str, object]] = []
        for map_index, key in enumerate(STOCK_MAP_KEYS):
            if key not in arenas:
                raise ValueError(f"arena metadata is missing for {key}")
            game_type = "tournament" if key.startswith("q3tourney") else "ffa"
            entities = read_bsp_entities(archive.read(f"maps/{key}.bsp"))
            pickups = build_pickups(entities, key, game_type)
            traversals = build_traversals(entities, game_type)
            arena = arenas[key]
            present_families = {
                family for pickup in pickups for family in pickup["families"]
            }
            maps.append(
                {
                    "map_index": map_index,
                    "key": key,
                    "name": arena["name"],
                    "game_type": game_type,
                    "frag_limit": arena["frag_limit"],
                    "bots": arena["bots"],
                    "arena_types": arena["arena_types"],
                    "weapon_families": [
                        name for name in WEAPON_FAMILIES if name in present_families
                    ],
                    "nonweapon_families": [
                        name for name in NONWEAPON_FAMILIES if name in present_families
                    ],
                    "pickups": pickups,
                    "traversals": traversals,
                    "has_major_powerup": bool(
                        present_families & MAJOR_POWERUP_FAMILIES
                    ),
                }
            )
    for key in CPMA_MAP_KEYS:
        arena, entities = cpma_maps[key]
        types = arena["arena_types"]
        game_type = (
            "ffa" if "ffa" in types else "tournament" if "tourney" in types else ""
        )
        if not game_type:
            raise ValueError(f"CPMA map {key} does not support FFA or Tournament")
        pickups = build_pickups(entities, key, game_type)
        traversals = build_traversals(entities, game_type)
        present_families = {
            family for pickup in pickups for family in pickup["families"]
        }
        maps.append(
            {
                "map_index": len(maps),
                "key": key,
                "name": arena["name"],
                "game_type": game_type,
                "frag_limit": arena["frag_limit"],
                "bots": arena["bots"],
                "arena_types": types,
                "weapon_families": [
                    name for name in WEAPON_FAMILIES if name in present_families
                ],
                "nonweapon_families": [
                    name for name in NONWEAPON_FAMILIES if name in present_families
                ],
                "pickups": pickups,
                "traversals": traversals,
                "has_major_powerup": bool(present_families & MAJOR_POWERUP_FAMILIES),
            }
        )

    payload: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "source_pak0_sha256": pak_hash,
        "source_map_paks_sha256": cpma_hashes,
        "maps": maps,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["catalog_hash"] = hashlib.sha256(canonical).hexdigest().upper()
    return payload


def encoded_catalog(catalog: dict[str, object]) -> bytes:
    return (json.dumps(catalog, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def encoded_audit(catalog: dict[str, object]) -> bytes:
    maps = catalog["maps"]
    active_classnames = {
        pickup["classname"] for map_data in maps for pickup in map_data["pickups"]
    }
    lines = [
        "# Quake III stock catalogue audit",
        "",
        f"- Schema version: `{catalog['schema_version']}`",
        f"- Source pak0 SHA-256: `{catalog['source_pak0_sha256']}`",
        f"- CPMA map PK3s: {len(catalog['source_map_paks_sha256'])}",
        f"- Catalogue hash: `{catalog['catalog_hash']}`",
        f"- Maps: {len(maps)}",
        f"- Pickups: {sum(len(map_data['pickups']) for map_data in maps)}",
        f"- Traversals: {sum(len(map_data['traversals']) for map_data in maps)}",
        "",
        "## GPL source comparison",
        "",
        "Compared with id Software Quake III Arena commit "
        "`dbe4ddb10315479fc00086f08e25d968b4b43c49`.",
        "",
        f"- `bg_misc.c`: all {len(active_classnames)} base-game pickup classnames "
        "that occur in these FFA/Tournament variants have an unlock family.",
        "- The permanent Gauntlet, `weapon_grapplinghook`, and the two CTF flags "
        "are recognized base items but have no active occurrence in this catalogue.",
        "- `g_spawn.c`: FFA and Tournament use `notfree`; base Q3 uses `notq3a`; "
        "the optional `gametype` value is matched against `ffa` or `tournament`. "
        "`notteam` applies only at `GT_TEAM` and above.",
        "- Runtime-dropped items are absent because only original BSP entities are read.",
        "- No pickup or kill range overflow exists; the largest map has "
        f"{max(len(map_data['pickups']) for map_data in maps)} pickups.",
        "",
        "## Per-map inventory",
        "",
        "| Map | Type | Frag limit | Bots | Pickup counts by classname | Unlock families |",
        "|---|---:|---:|---|---|---|",
    ]
    for map_data in maps:
        counts = Counter(pickup["classname"] for pickup in map_data["pickups"])
        count_text = "; ".join(
            f"{name} ×{count}" for name, count in sorted(counts.items())
        )
        families = ", ".join(
            sorted({pickup["family"] for pickup in map_data["pickups"]})
        )
        lines.append(
            f"| `{map_data['key']}` ({map_data['name']}) | {map_data['game_type']} | "
            f"{map_data['frag_limit']} | {', '.join(map_data['bots'])} | {count_text} | {families} |"
        )
    return ("\n".join(lines) + "\n").encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--baseq3", type=Path, default=Path(r"C:\Users\Rando\projects\baseq3")
    )
    parser.add_argument("--output", type=Path)
    parser.add_argument("--audit-output", type=Path)
    args = parser.parse_args()
    pak0_path = args.baseq3 / "pak0.pk3"
    if not pak0_path.is_file():
        parser.error(f"missing {pak0_path}")
    catalog = build_catalog(pak0_path)
    data = encoded_catalog(catalog)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(data)
    if args.audit_output:
        args.audit_output.parent.mkdir(parents=True, exist_ok=True)
        args.audit_output.write_bytes(encoded_audit(catalog))
    print(hashlib.sha256(data).hexdigest().upper())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
