from logging import getLogger

from typing import Any, List

from os import listdir
from os.path import isfile

from pathlib import Path

from importlib import import_module

from aiogram import (
    Dispatcher,
    Bot as AIOBot
)

from aiobot import Privacy, Backend, __version__


log = getLogger()

class Bot(AIOBot):
    def __init__(self, token: str = Privacy.bot_token, **kwargs: Any) -> None:
        super().__init__(token, **kwargs)

        self.dp: Dispatcher = Dispatcher()

    def include_routers(self, modules: List[str] = Backend.modules) -> None:
        for module in modules:
            if module.endswith("*"):
                module = module.replace("*", "")

                for element in listdir(module):
                    if element.startswith("_"):
                        continue

                    path = Path(module, element)

                    if isfile(path):
                        path = path.as_posix().replace("/", ".")[:-3]

                        try:
                            module = import_module(path)

                            self.dp.include_router(module.router)
                            log.info(f"{module.__name__} установлен.")

                        except Exception as exception:
                            continue
                    
            elif module.endswith(".py"):
                path = module.replace("/", ".")[:-3]

                try:
                    module = import_module(path)
                    
                    self.dp.include_router(module.router)
                    log.info(f"{module.__name__} установлен.")
                
                except Exception as exception:
                    continue

    async def start(self) -> None:
        log.info("Подключение бота...")

        await self.delete_webhook(drop_pending_updates=True)
        
        await self.dp.start_polling(self)