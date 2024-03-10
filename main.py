import asyncio
from src.handler import (
    papermc_runner,
    arclight_powered_runner,
    catserver_runner,
    leavesmc_runner,
    sponge_powered_runner,
    bungeecord_runner,
    pufferfish_runner,
    mohistmc_runner,
    getbukkit_runner,
    purpurmc_runner,
    fabric_runner,
    forge_runner,
)
from src.utils import SyncLogger, init_settings, argument_parser
from src import __version__
from src.api import start_production_server
import sys

available_core = """
ArclightPowered
├─Arclight
├─Lightfall
└─Lightfall Client
MohistMC
├─Banner
└─Mohist
SpigotMC
├─Spigot
└─BungeeCord
LeavesMC
└─Leaves
Pufferfish
├─Pufferfish
├─Pufferfish+
└─Pufferfish+ (Purpur)
SpongePowered
├─SpongeForge
└─SpongeVanilla
PaperMC
├─Paper
├─Folia
├─Travertine
├─Velocity
└─Waterfall
PurpurMC
└─Purpur
CatServer
CraftBukit
Vanilla
Fabric
Forge"""


async def update_default():
    tasks = [
        asyncio.create_task(papermc_runner()),
        asyncio.create_task(arclight_powered_runner()),
        asyncio.create_task(catserver_runner()),
        asyncio.create_task(sponge_powered_runner()),
        asyncio.create_task(bungeecord_runner()),
        asyncio.create_task(pufferfish_runner()),
        asyncio.create_task(mohistmc_runner()),
        asyncio.create_task(getbukkit_runner()),
        asyncio.create_task(purpurmc_runner()),
        asyncio.create_task(fabric_runner()),
        asyncio.create_task(forge_runner()),
        asyncio.create_task(leavesmc_runner()),
    ]
    for task in tasks:
        await task


if __name__ == "__main__":
    args = argument_parser.parse_args()

    if not any(value for _, value in args.__dict__.items()):
        argument_parser.error("No argument was specified.")

    if args.init:
        init_settings()
    if args.server:
        start_production_server()
    if args.version:
        print(__version__)
    if args.core_list:
        SyncLogger.success(available_core)
    if args.update:
        asyncio.run(update_default())

    sys.exit(0)
