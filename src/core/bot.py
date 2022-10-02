from aiogram import (
    Bot as AIOBot,
    Dispatcher
)

from src.config import Privacy
from src.handlers import include_all_routers


class Bot(AIOBot):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(token=Privacy.token, *args, **kwargs)

        self.dispatcher = Dispatcher()

    def set_commands(self) -> Dispatcher.include_router:
        router = include_all_routers()

        return self.dispatcher.include_router(router)
        

    async def start(self) -> Dispatcher.start_polling:
        await self.delete_webhook(drop_pending_updates=True)

        return await self.dispatcher.start_polling(self)