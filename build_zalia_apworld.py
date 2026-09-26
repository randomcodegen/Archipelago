"""Build the ZALiA apworld with the Archipelago 0.6.x container format."""

import json
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

CONTAINER_VERSION = 7
ROOT = Path(__file__).resolve().parent
WORLD = ROOT / "worlds" / "zalia"


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit("Usage: python build_zalia_apworld.py [output.apworld]")

    files_source = (ROOT / "worlds" / "Files.py").read_text(encoding="utf-8")
    if (
        f"container_version: int = {CONTAINER_VERSION}" not in files_source
        or f'manifest["compatible_version"] = {CONTAINER_VERSION}' not in files_source
    ):
        raise RuntimeError(
            "Archipelago's container format changed, review the pinned version before building."
        )

    manifest = json.loads((WORLD / "archipelago.json").read_text(encoding="utf-8"))
    manifest.update(version=CONTAINER_VERSION, compatible_version=CONTAINER_VERSION)
    output = (
        Path(sys.argv[1])
        if len(sys.argv) == 2
        else ROOT / "build" / "apworlds" / "zalia.apworld"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(".apworld.tmp")

    with ZipFile(temporary, "w", ZIP_DEFLATED, compresslevel=9) as archive:
        archive.writestr("zalia/archipelago.json", json.dumps(manifest))
        for path in sorted(WORLD.rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(WORLD)
            if (
                relative.name == "archipelago.json"
                or relative.name == "README.md"
                or relative.name.startswith(".")
                or path.suffix in (".pyc", ".pyo")
                or any(
                    part in ("test", "__pycache__", "__pycache_check_backup")
                    for part in relative.parts
                )
            ):
                continue
            archive.write(path, "zalia/" + relative.as_posix())

    with ZipFile(temporary) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Built apworld failed ZIP integrity check.")
        if json.loads(archive.read("zalia/archipelago.json")) != manifest:
            raise RuntimeError(
                "Built apworld manifest does not match the requested version."
            )
    temporary.replace(output)
    print(output)
    print(f"world_version={manifest['world_version']} version=7 compatible_version=7")


if __name__ == "__main__":
    main()
