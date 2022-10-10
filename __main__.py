from asyncio import run

from handlers import set_routers

from src.config import Privacy
from src.core import Bot, Logger


bot = Bot(Privacy.bot_token)

def main() -> None:
    router = set_routers()

    bot.include_router(router)

    run(bot.start())


if __name__ == "__main__":
    Logger().setup()
    main()