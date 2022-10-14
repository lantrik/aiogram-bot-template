

class BotError(Exception):
    """Основное исключение бота."""

class CommandError(BotError):
    """Исключение при работе пользователя с командой"""