"""Generate the Python and native Quake III catalogue tables."""

from __future__ import annotations

import argparse
import json
import pprint
from pathlib import Path

from build_catalog import NONWEAPON_FAMILIES, WEAPON_FAMILIES


ITEM_BASE = 3_370_000
LOCATION_BASE = 3_380_000
NOTHING_ID = ITEM_BASE + 300
QUAD_TOKEN_ID = ITEM_BASE + 301
HEALTH_FILLER_ID = ITEM_BASE + 302
ARMOR_FILLER_ID = ITEM_BASE + 303
AMMO_FILLER_BASE = ITEM_BASE + 304
AMMO_FILLERS = (
    ("+2 Shells", "Shotgun", 2),
    ("+5 Bullets", "Machinegun", 5),
    ("+1 Grenade", "Grenade Launcher", 1),
    ("+1 Rocket", "Rocket Launcher", 1),
    ("+10 Lightning Ammo", "Lightning Gun", 10),
    ("+1 Slug", "Railgun", 1),
    ("+5 Cells", "Plasma Gun", 5),
    ("+1 BFG Ammo", "BFG10K", 1),
)
TRAVERSAL_OFFSET = 200
POWERUP_FRAG_OFFSET = 350


def item_name(family: str) -> str:
    return f"{family} Unlock"


def build_tables(catalog: dict[str, object]) -> dict[str, object]:
    if len(catalog["maps"]) > 64:
        raise ValueError("catalog exceeds the 64-map client protocol limit")
    item_names: dict[str, int] = {}
    location_names: dict[str, int] = {}
    maps = []

    for map_data in catalog["maps"]:
        map_index = map_data["map_index"]
        label = f"{map_data['name']} ({map_data['key']})"
        stage_name = f"{label} - Stage Access"
        item_names[stage_name] = ITEM_BASE + map_index
        pickups = []
        map_base = LOCATION_BASE + map_index * 512
        for pickup in map_data["pickups"]:
            location_id = map_base + pickup["ordinal"]
            location_name = (
                f"{label} - Pickup {pickup['ordinal']:03d} - {pickup['display_name']}"
            )
            location_names[location_name] = location_id
            pickups.append({**pickup, "location_id": location_id, "location_name": location_name})
        traversals = []
        for traversal in map_data["traversals"]:
            location_id = map_base + TRAVERSAL_OFFSET + traversal["ordinal"]
            kind = "Jump Pad" if traversal["kind"] == "jump_pad" else "Teleporter"
            location_name = f"{label} - {kind} {traversal['kind_ordinal']:02d}"
            location_names[location_name] = location_id
            traversals.append({**traversal, "location_id": location_id, "location_name": location_name})
        if len(traversals) >= POWERUP_FRAG_OFFSET - TRAVERSAL_OFFSET:
            raise ValueError(f"{map_data['key']} has too many traversal locations")
        powerup_frag_id = map_base + POWERUP_FRAG_OFFSET if map_data["has_major_powerup"] else 0
        powerup_frag_name = f"{label} - Powerup Frag" if powerup_frag_id else None
        if powerup_frag_name:
            location_names[powerup_frag_name] = powerup_frag_id
        kills = []
        for number in range(1, map_data["frag_limit"] + 1):
            location_id = map_base + 400 + number
            location_name = f"{label} - Kill {number:02d}"
            location_names[location_name] = location_id
            kills.append({"number": number, "location_id": location_id, "location_name": location_name})
        clear_id = map_base + 500
        clear_name = f"{label} - Stage Clear"
        location_names[clear_name] = clear_id
        maps.append({
            **map_data,
            "stage_item_id": ITEM_BASE + map_index,
            "stage_item_name": stage_name,
            "pickups": pickups,
            "traversals": traversals,
            "powerup_frag_location_id": powerup_frag_id,
            "powerup_frag_location_name": powerup_frag_name,
            "kills": kills,
            "clear_location_id": clear_id,
            "clear_location_name": clear_name,
        })

    used_weapon_families = set().union(*(set(data["weapon_families"]) for data in catalog["maps"]))
    used_nonweapon_families = set().union(*(set(data["nonweapon_families"]) for data in catalog["maps"]))
    weapons = [family for family in WEAPON_FAMILIES if family in used_weapon_families]
    nonweapons = [family for family in NONWEAPON_FAMILIES if family in used_nonweapon_families]
    for index, family in enumerate(weapons):
        item_names[item_name(family)] = ITEM_BASE + 100 + index
    for index, family in enumerate(nonweapons):
        item_names[item_name(family)] = ITEM_BASE + 200 + index
    item_names["Nothing"] = NOTHING_ID
    item_names["Quad Token"] = QUAD_TOKEN_ID
    item_names["+1 Health"] = HEALTH_FILLER_ID
    item_names["+1 Armor"] = ARMOR_FILLER_ID
    for index, (name, family, amount) in enumerate(AMMO_FILLERS):
        item_names[name] = AMMO_FILLER_BASE + index

    if len(item_names) != len(set(item_names.values())):
        raise ValueError("generated item IDs are not unique")
    if len(location_names) != len(set(location_names.values())):
        raise ValueError("generated location IDs are not unique")
    if not all(ITEM_BASE <= value <= ITEM_BASE + 999 for value in item_names.values()):
        raise ValueError("item ID exceeds reserved block")
    if not all(LOCATION_BASE <= value < LOCATION_BASE + 64 * 512 for value in location_names.values()):
        raise ValueError("location ID exceeds reserved block")

    return {
        "schema_version": catalog["schema_version"],
        "catalog_hash": catalog["catalog_hash"],
        "item_name_to_id": item_names,
        "location_name_to_id": location_names,
        "weapon_families": weapons,
        "nonweapon_families": nonweapons,
        "maps": maps,
    }


def python_output(tables: dict[str, object]) -> bytes:
    def literal(value: object) -> str:
        return pprint.pformat(value, width=120, sort_dicts=False)

    item_names = tables["item_name_to_id"]
    location_names = tables["location_name_to_id"]
    text = f'''# Generated by tools/export_catalog.py. Do not edit.
SCHEMA_VERSION = {tables["schema_version"]}
CATALOG_HASH = {tables["catalog_hash"]!r}
WEAPON_FAMILIES = {literal(tuple(tables["weapon_families"]))}
NONWEAPON_FAMILIES = {literal(tuple(tables["nonweapon_families"]))}
AMMO_FILLERS = {literal(AMMO_FILLERS)}
ITEM_NAME_TO_ID = {literal(item_names)}
ITEM_ID_TO_NAME = {{value: name for name, value in ITEM_NAME_TO_ID.items()}}
LOCATION_NAME_TO_ID = {literal(location_names)}
LOCATION_ID_TO_NAME = {{value: name for name, value in LOCATION_NAME_TO_ID.items()}}
MAPS = {literal(tuple(tables["maps"]))}
MAP_BY_KEY = {{map_data["key"]: map_data for map_data in MAPS}}
'''
    return text.encode("utf-8")


def c_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=True)


def c_output(tables: dict[str, object]) -> bytes:
    maps = tables["maps"]
    families = list(tables["weapon_families"]) + list(tables["nonweapon_families"])
    family_index = {name: index for index, name in enumerate(families)}
    lines = [
        "/* Generated by worlds/quake3/tools/export_catalog.py. Do not edit. */",
        "#ifndef Q3AP_CATALOG_H",
        "#define Q3AP_CATALOG_H",
        "",
        "#include <stdint.h>",
        "#include <string.h>",
        "",
        f"#define Q3AP_CATALOG_SCHEMA_VERSION {tables['schema_version']}",
        f"#define Q3AP_CATALOG_HASH {c_string(tables['catalog_hash'])}",
        f"#define Q3AP_ITEM_BASE {ITEM_BASE}",
        f"#define Q3AP_NOTHING_ITEM_ID {NOTHING_ID}",
        f"#define Q3AP_QUAD_TOKEN_ITEM_ID {QUAD_TOKEN_ID}",
        f"#define Q3AP_HEALTH_FILLER_ITEM_ID {HEALTH_FILLER_ID}",
        f"#define Q3AP_ARMOR_FILLER_ITEM_ID {ARMOR_FILLER_ID}",
        f"#define Q3AP_AMMO_FILLER_ITEM_BASE {AMMO_FILLER_BASE}",
        f"#define Q3AP_AMMO_FILLER_COUNT {len(AMMO_FILLERS)}",
        f"#define Q3AP_REFILL_COUNT {2 + len(AMMO_FILLERS)}",
        "typedef struct { int32_t item_id; int family_index; int amount; } q3ap_ammo_filler_t;",
        "static const q3ap_ammo_filler_t q3ap_ammo_fillers[] = {",
        *(f"    {{ {AMMO_FILLER_BASE + index}, {family_index[family]}, {amount} }},"
          for index, (name, family, amount) in enumerate(AMMO_FILLERS)),
        "};",
        f"#define Q3AP_LOCATION_BASE {LOCATION_BASE}",
        "#define Q3AP_LOCATION_MAP_STRIDE 512",
        f"#define Q3AP_TRAVERSAL_LOCATION_OFFSET {TRAVERSAL_OFFSET}",
        f"#define Q3AP_POWERUP_FRAG_LOCATION_OFFSET {POWERUP_FRAG_OFFSET}",
        "#define Q3AP_KILL_LOCATION_OFFSET 400",
        "#define Q3AP_CLEAR_LOCATION_OFFSET 500",
        f"#define Q3AP_MAP_COUNT {len(maps)}",
        f"#define Q3AP_FAMILY_COUNT {len(families)}",
        "",
        "typedef struct {",
        "    uint16_t ordinal;",
        "    uint16_t bsp_entity_ordinal;",
        "    int32_t location_id;",
        "    uint16_t family_index;",
        "    const char *classname;",
        "    const char *display_name;",
        "} q3ap_catalog_pickup_t;",
        "",
        "typedef struct {",
        "    uint16_t bsp_entity_ordinal;",
        "    int32_t location_id;",
        "    uint8_t kind; /* 0 = jump pad, 1 = teleporter */",
        "} q3ap_catalog_traversal_t;",
        "",
        "typedef struct {",
        "    const char *key;",
        "    const char *name;",
        "    const char *bots;",
        "    uint16_t pickup_count;",
        "    uint16_t traversal_count;",
        "    uint8_t map_index;",
        "    uint8_t game_type; /* 0 = FFA, 1 = Tournament */",
        "    uint8_t frag_limit;",
        "    int32_t stage_item_id;",
        "    int32_t clear_location_id;",
        "    int32_t powerup_frag_location_id;",
        "    const q3ap_catalog_pickup_t *pickups;",
        "    const q3ap_catalog_traversal_t *traversals;",
        "} q3ap_catalog_map_t;",
        "",
        "typedef struct { const char *name; int32_t item_id; uint8_t weapon; } q3ap_catalog_family_t;",
        "",
    ]
    for map_data in maps:
        lines.append(f"static const q3ap_catalog_pickup_t q3ap_pickups_{map_data['key']}[] = {{")
        for pickup in map_data["pickups"]:
            for variant in pickup["variants"]:
                lines.append(
                    "    { %d, %d, %d, %d, %s, %s }," % (
                        pickup["ordinal"], variant["bsp_entity_ordinal"], pickup["location_id"],
                        family_index[variant["family"]], c_string(variant["classname"]),
                        c_string(pickup["display_name"]),
                    )
                )
        lines.extend(["};", ""])
        lines.append(f"static const q3ap_catalog_traversal_t q3ap_traversals_{map_data['key']}[] = {{")
        if not map_data["traversals"]:
            lines.append("    { 0, 0, 0 },")
        for traversal in map_data["traversals"]:
            lines.append(
                "    { %d, %d, %d }," % (
                    traversal["bsp_entity_ordinal"], traversal["location_id"],
                    0 if traversal["kind"] == "jump_pad" else 1,
                )
            )
        lines.extend(["};", ""])
    lines.append("static const q3ap_catalog_family_t q3ap_catalog_families[Q3AP_FAMILY_COUNT] = {")
    for index, family in enumerate(families):
        base = 100 if index < len(tables["weapon_families"]) else 200
        local_index = index if base == 100 else index - len(tables["weapon_families"])
        lines.append(
            f"    {{ {c_string(family)}, {ITEM_BASE + base + local_index}, "
            f"{1 if base == 100 else 0} }},"
        )
    lines.extend(["};", "", "static const q3ap_catalog_map_t q3ap_catalog_maps[Q3AP_MAP_COUNT] = {"])
    for map_data in maps:
        lines.append(
            "    { %s, %s, %s, %d, %d, %d, %d, %d, %d, %d, %d, q3ap_pickups_%s, q3ap_traversals_%s }," % (
                c_string(map_data["key"]), c_string(map_data["name"]),
                c_string(" ".join(map_data["bots"])),
                sum(len(pickup["variants"]) for pickup in map_data["pickups"]),
                len(map_data["traversals"]), map_data["map_index"],
                1 if map_data["game_type"] == "tournament" else 0,
                map_data["frag_limit"], map_data["stage_item_id"],
                map_data["clear_location_id"], map_data["powerup_frag_location_id"],
                map_data["key"], map_data["key"],
            )
        )
    lines.extend([
        "};", "",
        "static const q3ap_catalog_map_t *Q3AP_CatalogMapByKey(const char *key) {",
        "    unsigned int index;",
        "    for (index = 0; index < Q3AP_MAP_COUNT; ++index)",
        "        if (!strcmp(q3ap_catalog_maps[index].key, key)) return &q3ap_catalog_maps[index];",
        "    return 0;",
        "}",
        "",
        "static const q3ap_catalog_pickup_t *Q3AP_CatalogPickupByLocation(int32_t location_id) {",
        "    unsigned int map_index, pickup_index;",
        "    for (map_index = 0; map_index < Q3AP_MAP_COUNT; ++map_index)",
        "        for (pickup_index = 0; pickup_index < q3ap_catalog_maps[map_index].pickup_count; ++pickup_index)",
        "            if (q3ap_catalog_maps[map_index].pickups[pickup_index].location_id == location_id)",
        "                return &q3ap_catalog_maps[map_index].pickups[pickup_index];",
        "    return 0;",
        "}",
        "",
        "static const q3ap_catalog_traversal_t *Q3AP_CatalogTraversalByLocation(int32_t location_id) {",
        "    unsigned int map_index, traversal_index;",
        "    for (map_index = 0; map_index < Q3AP_MAP_COUNT; ++map_index)",
        "        for (traversal_index = 0; traversal_index < q3ap_catalog_maps[map_index].traversal_count; ++traversal_index)",
        "            if (q3ap_catalog_maps[map_index].traversals[traversal_index].location_id == location_id)",
        "                return &q3ap_catalog_maps[map_index].traversals[traversal_index];",
        "    return 0;",
        "}",
        "",
        "#endif",
        "",
    ])
    return "\n".join(lines).encode("utf-8")


def write_or_check(path: Path, data: bytes, check: bool) -> bool:
    if check:
        if not path.is_file() or path.read_bytes() != data:
            print(f"stale generated file: {path}")
            return False
        return True
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return True


def main() -> int:
    repository = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", type=Path, default=repository / "worlds/quake3/data/maps.json")
    parser.add_argument("--python-output", type=Path, default=repository / "worlds/quake3/data/generated.py")
    parser.add_argument("--c-output", type=Path,
                        default=repository.parent / "Quake3e-main/code/ap/q3ap_catalog.h")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    tables = build_tables(json.loads(args.catalog.read_text(encoding="utf-8")))
    valid = write_or_check(args.python_output, python_output(tables), args.check)
    valid &= write_or_check(args.c_output, c_output(tables), args.check)
    return 0 if valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
