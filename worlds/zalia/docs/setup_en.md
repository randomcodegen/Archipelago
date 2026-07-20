# ZALiA Multiworld Setup Guide

## Requirements

- The Archipelago-enabled ZALiA Windows build
- An active Archipelago room and your slot name

ZALiA connects directly to Archipelago. No separate game client is needed.

## Connection Setup

1. Launch ZALiA once. This creates:

   `%LOCALAPPDATA%\ZALiA\ap_config.ini`

2. Close the game. The first connection may fail because the new file uses local defaults.
3. Open `ap_config.ini` in a text editor:

   ```ini
   [Connection]
   server=archipelago.gg:38281
   slot=Player Name
   password=
   ```

4. Replace `server` with the room address and port.
5. Replace `slot` with your exact player slot name.
6. Set `password` only when the room requires one.
7. Save the file and relaunch ZALiA.

The default file is:

```ini
[Connection]
server=localhost:38281
slot=Player1
password=
```

The game reads this file at startup and connects automatically. Restart after changing it.

## Start Playing

1. Confirm the game connects to your slot.
2. Create a new save from the file-select screen.
3. The server's slot settings and seed configure the new game.


## Troubleshooting

| Problem | Fix |
|---|---|
| `ap_config.ini` is missing | Launch the game once, then check `%LOCALAPPDATA%\ZALiA` again. |
| Connection fails and the game closes | Check the server hostname, port, and whether the room is active. |
| Slot connection is refused | Check the exact slot name and room password. |
| Config changes are ignored | Save `ap_config.ini`, close ZALiA fully, then relaunch it. |
