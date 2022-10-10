from logging import getLogger

from typing import Any, Union, Optional

from aiogram import (
    Router,
    Dispatcher,
    Bot as AIOBot
)


log = getLogger()

class Bot(AIOBot):
    def __init__(self, token: str, **kwargs: Any) -> None:
        super().__init__(token, **kwargs)

        self.dp: Dispatcher = Dispatcher()

    def include_router(self, router: Union[Router, str]) -> Dispatcher.include_router:
        log.info("Подключение роутеров...")
        
        return self.dp.include_router(router)

    async def start(self) -> Dispatcher.start_polling:
        log.info("Подключение бота...")

        await self.delete_webhook(drop_pending_updates=True)

        return await self.dp.start_polling(self)