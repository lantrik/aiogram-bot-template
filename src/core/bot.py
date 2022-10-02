import logging

from aiogram import (
    Bot as AIObot,
    Dispatcher
)

from src.handlers import include_all_routers

from src.config import Privacy


class Bot(AIObot):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(token=Privacy.token, *args, **kwargs)

        self.dispatcher = Dispatcher()

    def set_commands(self) -> Dispatcher.include_router:
        router = include_all_routers()

        return self.dispatcher.include_router(router)
        

    async def start(self) -> Dispatcher.start_polling:
        await self.delete_webhook(drop_pending_updates=True)

        return await self.dispatcher.start_polling(self)