from typing import (
    List,
)


class View:
    """Класс с информацией, отображающийся пользователю."""


class Backend:
    """Класс с системной информацией бота."""
    owners: List[int] = [
        1390707560 #lantrik
    ]

    debug: bool = False

    modules: List[str] = [
        "modules/*",
        "modules/panels/*",
        "aiobot/core/errors.py"
    ]