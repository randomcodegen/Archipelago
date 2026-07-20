# ZALiA (Zelda Again: Link is Adventuresome)

## Game Options

ZALiA supports these randomization options:

### Item Options
- **randomize_item_locations** — Shuffle main items, quest items, maps, container pieces, and 1-Up Dolls (default: on)
- **randomize_pbag_locations** — Include P-Bags in the item shuffle (default: off)
- **randomize_key_locations** — Include palace small keys in the shuffle (default: off)
- **randomize_allkey_location** — Shuffle the Magical Key instead of using its vanilla Great Palace location (default: off)
- **limit_obscure_locations** — Reduce chance for progression at obscure locations (default: off)
- **dark_room_difficulty** — Light rules: 0 = all dark rooms need Candle/Fire, 1 = only the hardest do, 2 = none do (0-2, default: 0)
- **hard_logic_tricks** — Allow precise itemless tricks in logic (default: off)
- **item_location_hints** — Enable hints from marked NPCs and objects (default: on)
- **zelda_hint** — Hint none, Flute, Magical Key, or Jump's town (default: none)
- **hint_giver_percent** — Useful hint-giver percentage (0-100, default: 25)

### Spell Options
- **shuffle_spells_among_wise_men** — Shuffle spells among Wise Men only (default: off)
- **randomize_spell_locations** — Put spells in the general item pool; overrides Wise Man shuffling (default: off)
- **randomize_spell_cost** — Randomize spell MP costs by -25% to +10% (default: on)

### Dungeon Options
- **randomize_dungeon_rooms** — Randomize dungeon room layouts (default: off)
- **randomize_dungeon_locations** — Shuffle all seven Quest 1 dungeons among dungeon tiles; needs item randomization (default: off)
- **randomize_dungeon_boss** — Shuffle bosses among the six crystal dungeons (default: off)
- **boss_item_locations** — Add an extra randomized AP location at each crystal boss (default: off)
- **randomize_town_locations** — Shuffle all eight Quest 1 towns among town tiles (default: off)
- **randomize_dungeon_tileset** — Shuffle original and custom dungeon graphics (default: off)

### Enemy Options
- **enemy_difficulty** — Difficulty rank of randomized enemies (1-4, default: 1)
- **enemy_randomization_method** — Vanilla, Random Spawns, or Random Types (default: Vanilla)
- **randomize_enemy_spawners** — Shuffle spawner locations and randomize drop-spawner enemies (default: off)
- **enemy_enigma** — Enigma transforms enemies into random enemies instead of Blue Slimes (default: off)
- **randomize_enemy_hp** — Randomize enemy HP by -25% to +25% (default: off)
- **randomize_enemy_damage** — Randomize enemy damage by -25% to +25% (default: off)

### Other Options
- **randomize_level_cost** — Randomize level-up costs by -25% to +25% (default: on)
- **randomize_xp** — Randomize enemy and P-Bag XP by -25% to +25% (default: on)
- **randomize_palette** — Randomize color palettes (default: off)
- **force_quit_penalty** — Lose 75% XP from game-over warping; losing all lives still costs 75% when off (default: on)
- **starting_quest** — Quest 1 or Quest 2 (default: Quest 1)
- **starting_attack_level** — Starting Attack level; no logic effect (1-9, default: 1)
- **starting_magic_level** — Starting Magic level; no logic effect (1-9, default: 1)
- **starting_life_level** — Starting Life level; no logic effect (1-9, default: 1)
- **kakusu_required_count** — Gold Slimes needed for their bundled reward (0-12, default: 7)
- **kakusu_individual_location_count** — Gold Slime kills exposed as individual AP locations (0-12, default: 0)
- **crystals_required_count** — Crystals required to enter Great Palace (0-7, default: 6)
- **death_link** — Share deaths with other DeathLink players (default: off)
- **start_inventory_from_pool** — Start with chosen items removed from the item pool

## Item Progression

### Major Items (Tools)
Candle, Glove, Raft, Boots, Flute, Cross, Hammer, Bracelet, Mirror, Flower, Book, Meat, Shield, AllKey (Magical Key), Pendant, Sword, Trophy, Ring, Mask, Note, Map (Nabooru), Map (New Kasuto), Child, Rescue Fairy, Bottle

### Spells
Shield, Jump, Heal, Fairy, Fire, Reflect, Enigma, Thunder, Summon (Quest 2 only)

### Skills
Stab Down, Stab Up (obtained from the two hidden skill teachers)

### Keys
Small Keys for each of the 6 palaces (Parapa, Midoro, Island, Maze, Sea, Three Eye)

### Containers
Heart container pieces and Magic container pieces (4 pieces = 1 container)

### Other Items
1-Up Dolls, P-Bags (filler)

## Location Access Rules

### West Side (Starting Area)
- **Rauru Pass** → Midoro Field: requires Hammer, Flute, Glove, or Bracelet
- **JUMP Cave** → Midoro Field: requires Jump spell + dark room passable
- **Rauru to Midoro Cave**: requires Glove or Bracelet

### Saria Bridge → Saria2
- Requires Note, OR Jump spell + Fairy spell

### Royal Cemetery
- Requires Hammer (to break boulder)
- **Royal Cemetery → Death Mountain**: requires dark room passable

### Raft Areas
- **Raft to East**: requires Raft
- **Raft to North Islands**: requires Raft + Hammer + (Jump or Fairy)

### East Continent
- **Kasuto Area**: requires Flute, OR Bracelet + Boots
- **Valley of Death → Dragmire**: requires Cross + Boots + Raft
- **Darunia Field → Maze Island**: requires Stab Down skill

### Palaces
Each palace has an overworld entrance requirement plus key-gated internal locations:
- **Parapa Palace**: dark room passable
- **Midoro Palace**: Glove + dark room passable
- **Island Palace**: Glove + Stab Down
- **Maze Island Palace**: Reflect spell
- **Palace on the Sea**: Fairy spell
- **Three Eye Rock Palace**: Glove + (Jump or Stab Down) + Fairy
- **Great Palace**: requires `crystals_required_count` palace crystals

## Victory Condition
Defeat Ganon and restore the Triforce. The Victory event is placed in the Great Palace.
