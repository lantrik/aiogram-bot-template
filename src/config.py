from typing import (
    List,
)

from aiogram import Router


class View:
    """Класс с информацией, отображающийся пользователю."""

class Backend:
    """Класс с системной информацией бота."""
    owners: List[int] = [
        1390707560 #lantrik
    ]
    debug: bool = False

class Privacy:
    """Класс с API-токенами."""
    bot_token: str = "TOKEN"