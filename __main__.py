from asyncio import run

from handlers import set_routers

from src.privacy import Privacy
from src.core import Bot, Logger


bot = Bot()

def main() -> None:
    router = set_routers()

    bot.include_router(router)

    run(bot.start())


if __name__ == "__main__":
    log = Logger()

    log.setup()
    main()