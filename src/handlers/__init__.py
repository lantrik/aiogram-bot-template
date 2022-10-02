from typing import List

from aiogram import Router

from . import (
    start,
    echo
)


handlers: List = [
    start.router,
    echo.router
]


def include_all_routers() -> Router:
    router: Router = Router()

    for handler in handlers:
        router.include_router(handler)

    return router
