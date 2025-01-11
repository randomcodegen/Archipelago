from typing import TYPE_CHECKING, Dict, Set
import time

"""
# TODO:  Remove this when Archipelago 0.4.4 gets released
import sys

if "worlds._bizhawk" not in sys.modules:
    import importlib
    import os
    import zipimport

    bh_apworld_path = os.path.join(
        os.path.dirname(sys.modules["worlds"].__file__), "_bizhawk.apworld"
    )
    if os.path.isfile(bh_apworld_path):
        importer = zipimport.zipimporter(bh_apworld_path)
        spec = importer.find_spec(os.path.basename(bh_apworld_path).rsplit(".", 1)[0])
        mod = importlib.util.module_from_spec(spec)
        mod.__package__ = f"worlds.{mod.__package__}"
        mod.__name__ = f"worlds.{mod.__name__}"
        sys.modules[mod.__name__] = mod
        importer.exec_module(mod)
    elif not os.path.isdir(os.path.splitext(bh_apworld_path)[0]):
        raise AssertionError("Could not import worlds._bizhawk")
"""

from NetUtils import ClientStatus
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient
import time
from .Locations import checkable_locations, boss_location_dict
from .Blocks import block_info_dict
from .Items import (
    lookup_trapid_to_name,
    lookup_eventid_to_name,
    lookup_junkid_to_name,
)

powerup_list = [0xA40000, 0xA40100, 0xA40200, 0xA40300, 0xA41100]
active_junk = [0xA80900, 0xA80800, 0xA80700]

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext
else:
    BizHawkClientContext = object

# Add .apwl suffix to bizhawk client
from worlds.LauncherComponents import SuffixIdentifier, components

for component in components:
    if component.script_name == "BizHawkClient":
        component.file_identifier = SuffixIdentifier(
            *(*component.file_identifier.suffixes, ".apwl")
        )
        break

EXPECTED_ROM_NAME = "WARIOLANDAP"


class WarioLandClient(BizHawkClient):
    game = "Wario Land"
    system = ("GB", "SGB")
    # patch_suffix = ".apwl"

    def __init__(self) -> None:
        super().__init__()

    async def validate_rom(self, ctx: BizHawkClientContext) -> bool:
        from CommonClient import logger

        try:
            # Check ROM name/patch version
            rom_name_bytes = (
                await bizhawk.read(ctx.bizhawk_ctx, [(0x134, 16, "ROM")])
            )[0]
            rom_name = bytes([byte for byte in rom_name_bytes if byte != 0]).decode(
                "ascii"
            )
            if rom_name.startswith("SUPERMARIO"):
                logger.info(
                    "ERROR: You appear to be running an unpatched version of Wario Land. "
                    "You need to generate a patch file and use it to create a patched ROM."
                )
                return False
            if not rom_name.startswith(EXPECTED_ROM_NAME):
                logger.info(
                    "ERROR: The patch file used to create this ROM is not compatible with "
                    "this client. Double check your client version against the version being "
                    "used by the generator."
                )
                return False
        except UnicodeDecodeError:
            return False
        except bizhawk.RequestFailedError:
            return False  # Should verify on the next pass

        ctx.game = self.game
        ctx.items_handling = 0b111
        ctx.want_slot_data = True
        ctx.watcher_timeout = 0.125
        # Trap vars
        ctx.trap_queue = []
        ctx.last_trap_time = 0
        ctx.traps_activated = 0
        # Status vars
        ctx.refresh_connect = False
        ctx.connected = False
        ctx.data_present = False
        ctx.game_clear = False
        ctx.syrup_open = False
        ctx.event_update = False
        ctx.game_mode = 0x00
        ctx.demo_mode = 0x00
        ctx.paused = 0x00
        # Blocksanity vars
        ctx.last_block_read = 0xA430
        ctx.block_level_id = 0
        ctx.ow_id = 0x00
        # Deathlink vars
        ctx.last_deathlink_activated = 0
        ctx.local_last_death_link = 0
        ctx.last_lives_count = -1
        # Deathlink vars
        ctx.last_deathlink_activated = 0
        ctx.local_last_death_link = 0
        ctx.last_lives_count = -1
        return True

    async def set_auth(self, ctx: BizHawkClientContext) -> None:
        from CommonClient import logger

        slot_name_length = await bizhawk.read(ctx.bizhawk_ctx, [(0x674B0, 1, "ROM")])
        slot_name_bytes = await bizhawk.read(
            ctx.bizhawk_ctx, [(0x674B1, slot_name_length[0][0], "ROM")]
        )
        ctx.auth = bytes([byte for byte in slot_name_bytes[0] if byte != 0]).decode(
            "utf-8"
        )

    async def game_watcher(self, ctx: BizHawkClientContext) -> None:
        from CommonClient import logger

        if ctx.auth_status == 3:
            ctx.connected = True
        else:
            ctx.connected = False
            ctx.refresh_connect = True

        if ctx.slot_data != None:
            ctx.data_present = True
        else:
            ctx.data_present = False

        if ctx.connected and ctx.data_present:
            try:
                # Santity check game state, these bytes represent the first bytes of savefile1
                sanity_check_savefile = b"\x19d9W"
                read_result = await bizhawk.guarded_read(
                    ctx.bizhawk_ctx,
                    [(0xA000, 4, "System Bus")],
                    [(0xA000, sanity_check_savefile, "System Bus")],
                )
                if read_result is None:  # Game not loaded
                    return
                # Check if initial sync is required
                sync_required = await bizhawk.guarded_read(
                    ctx.bizhawk_ctx,
                    [(0xA4FA, 1, "System Bus")],
                    [(0xA4FA, b"\x00", "System Bus")],
                )

                if ctx.refresh_connect:
                    sync_required = True
                    ctx.refresh_connect = False
                if sync_required:
                    # Reset Deathlink vars
                    ctx.local_last_death_link = 0
                    ctx.last_local_lives = -1
                    if ctx.slot_data["death_link"]:
                        await ctx.update_death_link(True)
                        ctx.local_last_death_link = ctx.last_death_link
                    else:
                        ctx.local_last_death_link = 0
                    # Reset Deathlink vars
                    ctx.local_last_death_link = 0
                    ctx.last_local_lives = -1
                    if ctx.slot_data["death_link"]:
                        await ctx.update_death_link(True)
                        ctx.local_last_death_link = ctx.last_death_link
                    else:
                        ctx.local_last_death_link = 0
                    # Clear trap queue
                    ctx.trap_queue.clear()
                    await bizhawk.write(
                        ctx.bizhawk_ctx, [(0xA4FB, bytes(2), "System Bus")]
                    )
                    # Clear blocksanity data
                    await bizhawk.write(
                        ctx.bizhawk_ctx, [(0xA42E, bytes(64), "System Bus")]
                    )
                    ctx.last_block_read = 0xA430
                    # Activate full overworld+subworld movement
                    new_value = b"\xFF"
                    for addr in range(0xA413, 0xA421):
                        await bizhawk.write(
                            ctx.bizhawk_ctx, [(addr, new_value, "System Bus")]
                        )
                # Number of activated traps stored at 0xA4FB 2 bytes
                read_result = await bizhawk.read(
                    ctx.bizhawk_ctx, [(0xA4FB, 2, "System Bus")]
                )
                ctx.traps_activated = int.from_bytes(read_result[0], "little")

                # Number of received items stored at 0xA4FE 2 bytes
                read_result = await bizhawk.read(
                    ctx.bizhawk_ctx, [(0xA4FE, 2, "System Bus")]
                )
                local_received = int.from_bytes(read_result[0], "little")

                # Grab important info for item activation timing
                read_result = await bizhawk.read(
                    ctx.bizhawk_ctx, [(0xA8C3, 1, "System Bus")]
                )
                # 0=stopped; 1=overworld; 2=level loading; 3=gameplay; 5=respawn/leave stage; 10=door transition
                if read_result[0][0] != ctx.game_mode:
                    ctx.game_mode = read_result[0][0]
                    ctx.event_update = True

                read_result = await bizhawk.read(
                    ctx.bizhawk_ctx, [(0xA8C6, 1, "System Bus")]
                )
                # demo mode needs to be 0, otherwise demo is playing
                ctx.demo_mode = read_result[0][0]

                read_result = await bizhawk.read(
                    ctx.bizhawk_ctx, [(0xA908, 1, "System Bus")]
                )
                # 0=unpaused, 1=paused
                ctx.paused = read_result[0][0]

                # Level ID, matches with wl.apworld level IDs if not in overworld
                read_result = await bizhawk.read(
                    ctx.bizhawk_ctx, [(0xA804, 1, "System Bus")]
                )
                if read_result[0][0] != ctx.block_level_id:
                    ctx.block_level_id = read_result[0][0]
                    ctx.event_update = True

                # Current Level ID: changes when new node on subworld is selected
                read_result = await bizhawk.read(
                    ctx.bizhawk_ctx, [(0xA79F, 1, "System Bus")]
                )
                if read_result[0][0] + 0x30 != ctx.ow_id:
                    ctx.ow_id = read_result[0][0] + 0x30
                    ctx.event_update = True

                # Check Locations for completion
                new_checks = []
                for loc_name, loc_id in checkable_locations.items():
                    if loc_id not in ctx.locations_checked:
                        loc_bitmask = (loc_id) & 0xFF
                        loc_addr = loc_id >> 8
                        read_result = await bizhawk.read(
                            ctx.bizhawk_ctx, [(loc_addr, 1, "System Bus")]
                        )
                        loc_result = (read_result[0][0]) & loc_bitmask
                        if loc_result > 0:
                            if loc_id in boss_location_dict:
                                # Also award boss item on boss token received
                                new_checks.append(loc_id)
                                new_checks.append(boss_location_dict[loc_id])
                            else:
                                new_checks.append(loc_id)

                if ctx.slot_data["blocksanity"] == 1:
                    if ctx.game_mode == 3 and ctx.demo_mode == 0:
                        # Check blocksanity pointer address
                        read_result = await bizhawk.read(
                            ctx.bizhawk_ctx, [(0xA42E, 2, "System Bus")]
                        )
                        pointer_addr = int.from_bytes(read_result[0], "little")
                        read_addr = ctx.last_block_read
                        # Start with a sanity check
                        if pointer_addr > 0xA42F:
                            while read_addr < pointer_addr:
                                read_result = await bizhawk.read(
                                    ctx.bizhawk_ctx, [(read_addr, 2, "System Bus")]
                                )
                                lower_byte = int.from_bytes(read_result[0], "big")

                                # Handle special cases for flooded rice beach
                                if ctx.block_level_id == 0x17:
                                    upper_byte = 0x07 << 16
                                elif ctx.block_level_id == 0x24:
                                    upper_byte = 0x0E << 16
                                else:
                                    upper_byte = ctx.block_level_id << 16
                                # level id appended by block ptr addr
                                block_id = upper_byte + lower_byte
                                if (
                                    lower_byte > 0x00
                                    and block_info_dict[block_id].locationID
                                    not in ctx.locations_checked
                                ):
                                    new_checks.append(
                                        block_info_dict[block_id].locationID
                                    )
                                ctx.last_block_read = read_addr
                                read_addr += 2
                    elif ctx.game_mode < 3:
                        # stage over, clear blocksanity data if necessary
                        read_result = await bizhawk.read(
                            ctx.bizhawk_ctx, [(0xA42E, 1, "System Bus")]
                        )
                        if read_result[0][0] > 0x00:
                            # [b'%c' % i for i in bytes(64)]
                            await bizhawk.write(
                                ctx.bizhawk_ctx, [(0xA42E, bytes(64), "System Bus")]
                            )
                        ctx.last_block_read = 0xA430

                # Update local items if the client received new ones
                if len(ctx.items_received) > local_received:
                    for item in ctx.items_received[local_received:]:
                        local_received += 1
                        # Traps
                        if item.item in lookup_trapid_to_name:
                            ctx.trap_queue.append(item)
                        # Junk
                        elif item.item in lookup_junkid_to_name:
                            if item.item in active_junk:
                                # Lives and Hearts and Coins
                                item_addr = item.item >> 8
                                read_result = await bizhawk.read(
                                    ctx.bizhawk_ctx, [(item_addr, 1, "System Bus")]
                                )
                                new_value = (read_result[0][0] + 1).to_bytes(
                                    1, "little"
                                )
                                if (read_result[0][0]) & 0xF == 9:
                                    if (read_result[0][0]) == 0x99:
                                        # if 0x99, do nothing
                                        new_value = read_result[0][0]
                                    else:
                                        # Since the game directly displays hex values for lives we need to skip over A-F
                                        new_value = (read_result[0][0] + 7).to_bytes(
                                            1, "little"
                                        )
                                await bizhawk.write(
                                    ctx.bizhawk_ctx,
                                    [(item_addr, new_value, "System Bus")],
                                )
                            else:
                                pass
                        # Everything else
                        else:
                            item_addr = item.item >> 8
                            read_result = await bizhawk.read(
                                ctx.bizhawk_ctx, [(item_addr, 1, "System Bus")]
                            )
                            new_value = (read_result[0][0] + 1).to_bytes(1, "little")
                            await bizhawk.write(
                                ctx.bizhawk_ctx, [(item_addr, new_value, "System Bus")]
                            )
                            if item.item in powerup_list:
                                # If an upgrade item is received, make sure Wario can grow.
                                await bizhawk.write(
                                    ctx.bizhawk_ctx, [(0xA410, b"\x01", "System Bus")]
                                )
                                if item.item == 0xA41100:
                                    # We received a progressive powerup, handle accordingly
                                    upgrade_state = read_result[0][0] + 1
                                    if upgrade_state == 1:
                                        # Garlic
                                        await bizhawk.write(
                                            ctx.bizhawk_ctx,
                                            [(0xA400, b"\x01", "System Bus")],
                                        )
                                    elif upgrade_state == 2:
                                        # Bull
                                        await bizhawk.write(
                                            ctx.bizhawk_ctx,
                                            [(0xA401, b"\x01", "System Bus")],
                                        )
                                    elif upgrade_state == 3:
                                        # Dragon
                                        await bizhawk.write(
                                            ctx.bizhawk_ctx,
                                            [(0xA403, b"\x01", "System Bus")],
                                        )
                                    elif upgrade_state == 4:
                                        # Jet
                                        await bizhawk.write(
                                            ctx.bizhawk_ctx,
                                            [(0xA402, b"\x01", "System Bus")],
                                        )
                                    else:
                                        # TODO: Report that something went wrong with progressive powerups?
                                        pass
                                # Handle retroactive powerup assignment if get_previous_powerups is set
                                elif ctx.slot_data["get_previous_powerups"]:
                                    for addr in range(0xA400, item_addr):
                                        await bizhawk.write(
                                            ctx.bizhawk_ctx,
                                            [(addr, b"\x01", "System Bus")],
                                        )
                            # Events
                            if item.item in lookup_eventid_to_name:
                                # Boss tokens
                                if (
                                    item.item == 0xA41200
                                    and read_result[0][0] + 1
                                    >= ctx.slot_data["bosses_required"]
                                ):
                                    # We received the required ammount of boss tokens to fight the final boss
                                    await bizhawk.write(
                                        ctx.bizhawk_ctx,
                                        [(0xA427, b"\x01", "System Bus")],
                                    )
                            # Handle garlic hunt
                            if (
                                ctx.slot_data["goal"] == 1
                                and item.item == 0xA42800
                                and not ctx.finished_game
                            ):
                                if read_result[0][0] + 1 >= ctx.slot_data[
                                    "number_of_garlic_cloves"
                                ] * (
                                    ctx.slot_data["percentage_of_garlic_cloves"] / 100.0
                                ):
                                    ctx.game_clear = True
                    # Write new local received value to RAM
                    await bizhawk.write(
                        ctx.bizhawk_ctx,
                        [(0xA4FE, local_received.to_bytes(2, "little"), "System Bus")],
                    )
                # Update locations if we checked a new one
                for new_check_id in new_checks:
                    ctx.locations_checked.add(new_check_id)
                    location = ctx.location_names[new_check_id]
                    if not sync_required:
                        # Live checks show extra info
                        logger.info(
                            f"New Check: {location} ({len(ctx.locations_checked)}/{len(ctx.missing_locations) + len(ctx.checked_locations)})"
                        )
                    await ctx.send_msgs(
                        [{"cmd": "LocationChecks", "locations": [new_check_id]}]
                    )

                # Check for genie goal if required
                if ctx.slot_data["goal"] == 0 and not ctx.finished_game:
                    # Check for genie completion
                    read_result = await bizhawk.read(
                        ctx.bizhawk_ctx, [(0xA817, 1, "System Bus")]
                    )
                    if read_result[0][0] == 1:
                        ctx.game_clear = True

                if not ctx.finished_game and ctx.game_clear:
                    await ctx.send_msgs(
                        [{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}]
                    )
                    ctx.finished_game = True

                # Handle traps if queue is not empty
                if len(ctx.trap_queue) > ctx.traps_activated:
                    if (
                        ctx.demo_mode == 0
                        and ctx.game_mode == 3
                        and ctx.paused == 0
                        and time.time() - ctx.last_trap_time > 5
                    ):
                        # Grab a trap
                        ctx.last_trap_time = time.time()
                        trap_pick = ctx.trap_queue[-1]
                        if trap_pick.item == 0xA38400:
                            # Stun trap, 0xA384 = 0xFF
                            await bizhawk.write(
                                ctx.bizhawk_ctx, [(0xA384, b"\xFF", "System Bus")]
                            )
                        elif trap_pick.item == 0xA96400:
                            # Timer trap
                            await bizhawk.write(
                                ctx.bizhawk_ctx, [(0xA964, b"\x01\x01", "System Bus")]
                            )
                        elif trap_pick.item == 0xA91A00:
                            # Death trap
                            await bizhawk.write(
                                ctx.bizhawk_ctx, [(0xA91A, b"\x09", "System Bus")]
                            )
                        else:
                            # Grease trap
                            await bizhawk.write(
                                ctx.bizhawk_ctx, [(0xA61C, b"\x22", "System Bus")]
                            )
                        # Mark one more trap as activated
                        ctx.traps_activated += 1
                        await bizhawk.write(
                            ctx.bizhawk_ctx,
                            [
                                (
                                    0xA4FB,
                                    ctx.traps_activated.to_bytes(2, "little"),
                                    "System Bus",
                                )
                            ],
                        )
                # Handle death_link
                if ctx.slot_data["death_link"]:
                    await ctx.update_death_link(True)
                if "DeathLink" in ctx.tags:
                    # Read lives for deathlink
                    read_result = await bizhawk.read(
                        ctx.bizhawk_ctx, [(0xA809, 1, "System Bus")]
                    )
                    if ctx.last_local_lives == -1:
                        # var is still uninitiated
                        ctx.last_local_lives = read_result[0][0]
                    if ctx.last_local_lives < read_result[0][0]:
                        ctx.last_local_lives = read_result[0][0]
                    # Only handle deathlink send/receive if we are ingame
                    if ctx.demo_mode == 0 and ctx.game_mode == 3 and ctx.paused == 0:
                        # Compare lives for deathlink
                        if read_result[0][0] < ctx.last_local_lives:
                            # We died :(
                            await ctx.send_death(
                                f"{ctx.auth} died from a garlic overdose."
                            )
                            while ctx.local_last_death_link < ctx.last_death_link:
                                ctx.local_last_death_link = ctx.last_death_link
                            # Update lives counter
                            updating = True
                            while updating:
                                read_result = await bizhawk.read(
                                    ctx.bizhawk_ctx, [(0xA809, 1, "System Bus")]
                                )
                                if ctx.last_local_lives != read_result[0][0]:
                                    ctx.last_local_lives = read_result[0][0]
                                    updating = False
                        if ctx.local_last_death_link < ctx.last_death_link:
                            # Somebody else died, so we die too
                            ctx.local_last_death_link = ctx.last_death_link
                            await bizhawk.write(
                                ctx.bizhawk_ctx, [(0xA91A, b"\x09", "System Bus")]
                            )
                            # Update lives counter
                            updating = True
                            while updating:
                                read_result = await bizhawk.read(
                                    ctx.bizhawk_ctx, [(0xA809, 1, "System Bus")]
                                )
                                if ctx.last_local_lives != read_result[0][0]:
                                    ctx.last_local_lives = read_result[0][0]
                                    updating = False
                # Handle death_link
                if ctx.slot_data["death_link"]:
                    await ctx.update_death_link(True)
                if "DeathLink" in ctx.tags:
                    # Read lives for deathlink
                    read_result = await bizhawk.read(
                        ctx.bizhawk_ctx, [(0xA809, 1, "System Bus")]
                    )
                    if ctx.last_local_lives == -1:
                        # var is still uninitiated
                        ctx.last_local_lives = read_result[0][0]
                    if ctx.last_local_lives < read_result[0][0]:
                        ctx.last_local_lives = read_result[0][0]
                    # Only handle deathlink send/receive if we are ingame
                    if ctx.demo_mode == 0 and ctx.game_mode == 3 and ctx.paused == 0:
                        # Compare lives for deathlink
                        if read_result[0][0] < ctx.last_local_lives:
                            # We died :(
                            await ctx.send_death(
                                f"{ctx.auth} died from a garlic overdose."
                            )
                            while ctx.local_last_death_link < ctx.last_death_link:
                                ctx.local_last_death_link = ctx.last_death_link
                            # Update lives counter
                            updating = True
                            while updating:
                                read_result = await bizhawk.read(
                                    ctx.bizhawk_ctx, [(0xA809, 1, "System Bus")]
                                )
                                if ctx.last_local_lives != read_result[0][0]:
                                    ctx.last_local_lives = read_result[0][0]
                                    updating = False
                        if ctx.local_last_death_link < ctx.last_death_link:
                            # Somebody else died, so we die too
                            ctx.local_last_death_link = ctx.last_death_link
                            await bizhawk.write(
                                ctx.bizhawk_ctx, [(0xA91A, b"\x09", "System Bus")]
                            )
                            # Update lives counter
                            updating = True
                            while updating:
                                read_result = await bizhawk.read(
                                    ctx.bizhawk_ctx, [(0xA809, 1, "System Bus")]
                                )
                                if ctx.last_local_lives != read_result[0][0]:
                                    ctx.last_local_lives = read_result[0][0]
                                    updating = False
                # Resync-Loop finished
                if sync_required:
                    ctx.traps_activated = len(ctx.trap_queue)
                    await bizhawk.write(
                        ctx.bizhawk_ctx,
                        [
                            (
                                0xA4FB,
                                ctx.traps_activated.to_bytes(2, "little"),
                                "System Bus",
                            )
                        ],
                    )
                    await bizhawk.write(
                        ctx.bizhawk_ctx, [(0xA4FA, b"\x01", "System Bus")]
                    )
                # Handle 0 bosses required
                if not ctx.syrup_open and ctx.slot_data["bosses_required"] == 0:
                    # We received the required ammount of boss tokens to fight the final boss
                    await bizhawk.write(
                        ctx.bizhawk_ctx, [(0xA427, b"\x01", "System Bus")]
                    )
                    ctx.syrup_open = True
                # Desync
                if len(ctx.items_received) < local_received:
                    # Force resync
                    await bizhawk.write(
                        ctx.bizhawk_ctx, [(0xA4FA, b"\x00", "System Bus")]
                    )

                # Send level id data to tracker
                if ctx.event_update:
                    # In Map
                    if ctx.game_mode >= 0x02:
                        await ctx.send_msgs(
                            [
                                {
                                    "cmd": "Set",
                                    "key": f"warioland_curlevelid_{ctx.team}_{ctx.slot}",
                                    "default": 0,
                                    "want_reply": False,
                                    "operations": [
                                        {
                                            "operation": "replace",
                                            "value": ctx.block_level_id,
                                        }
                                    ],
                                }
                            ]
                        )
                    # In Overworld
                    else:
                        await ctx.send_msgs(
                            [
                                {
                                    "cmd": "Set",
                                    "key": f"warioland_curlevelid_{ctx.team}_{ctx.slot}",
                                    "default": 0,
                                    "want_reply": False,
                                    "operations": [
                                        {"operation": "replace", "value": ctx.ow_id}
                                    ],
                                }
                            ]
                        )
                    ctx.event_update = False
            except bizhawk.RequestFailedError:
                # Exit handler and return to main loop to reconnect
                pass
