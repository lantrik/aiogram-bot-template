from logging import getLogger

from typing import Any, Union

from aiogram import (
    Router,
    Dispatcher,
    Bot as AIOBot
)

from src.privacy import Privacy


log = getLogger()

class Bot(AIOBot):
    def __init__(self, token: str = Privacy.bot_token, **kwargs: Any) -> None:
        super().__init__(token, **kwargs)

        self.dp: Dispatcher = Dispatcher()

    def include_router(self, router: Union[Router, str]) -> None:
        log.info("Подключение роутеров...")
        
        self.dp.include_router(router)

    async def start(self) -> None:
        log.info("Подключение бота...")

        await self.delete_webhook(drop_pending_updates=True)
        
        await self.dp.start_polling(self)