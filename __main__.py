from asyncio import run

from aiobot.core import Bot, Logger


if __name__ == "__main__":
    Logger().setup()
    run(Bot().start())