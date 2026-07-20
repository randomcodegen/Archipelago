# ZALiA Archipelago Data Contract

This directory contains the shared name↔ID mapping between the ZALiA game (GML) and the
Archipelago apworld (Python).

## Files

- `zalia_locations.json` — Exported from the game. Each entry: location name, category,
  obscurity rating, intended item-type, room name, location number.
- `zalia_items.json` — Exported from the game. Item/spell/skill/town lists plus metadata.

## Regeneration Procedure

1. Open `ZALiA.project.gmx` in GameMaker:Studio 1.4.9999.
2. Run the game in debug mode.
3. Trigger the export from a dev context (e.g. `Dev_RmWarper` or a key bind) that calls
   `dev_ap_export_data()` after the randomizer has initialized its data.
4. The file `ap_export_data.json` will be written to %localappdata%/ZALiA/.
5. Copy it here as `zalia_data_export.json`.

**Important:** IDs are assigned by sorting entries by their internal location/item number.
Do NOT reorder the JSON arrays manually — always regenerate from the game to ensure IDs stay
in sync. Any drift between the JSONs and the game's own definitions will silently corrupt seeds.
