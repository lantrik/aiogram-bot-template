from asyncio import run

from aiobot.core import Bot, Logger


bot = Bot()

log = Logger()

if __name__ == "__main__":
    log.setup()

    bot.include_routers()
    run(bot.start())