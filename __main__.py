import logging

from asyncio import run

from src.core import Bot


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

bot = Bot()

def main() -> None:
    bot.set_commands()

    run(bot.start())


if __name__ == "__main__":
    main()