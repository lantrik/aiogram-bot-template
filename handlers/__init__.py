from typing import List

from aiogram import Router

from . import (
    start
)


routers: List[Router] = [
    start.router,
]

def set_routers() -> Router:
    combined_router: Router = Router()

    for router in routers:
        combined_router.include_router(router)

    return combined_router