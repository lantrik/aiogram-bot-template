from typing import List

from aiogram import Router

from . import (
    start
)


routers: List[Router] = [
    start.router,
]

def set_routers() -> Router:
    new_router: Router = Router()

    for router in routers:
        new_router.include_router(router)

    return new_router