import logging

from src.config import Backend


class Logger:
    EXTERNAL_LOGS = ("aiogram", "http",)
    LOG_LEVEL = logging.DEBUG if Backend.debug else logging.INFO
    LOG_FORMAT = ("{asctime} | {lineno:^3} | {filename:^16} | "
                  "{levelname:^8} | {message}")

    def __init__(self) -> None:
        self.log = logging.getLogger()

    def _stream_handler(self) -> logging.StreamHandler:
        """Возвращает основной регистратор для консоли."""
        formatter = logging.Formatter(self.LOG_FORMAT, style="{")

        handler = logging.StreamHandler()
        handler.setFormatter(formatter)

        return handler

    def _file_handler(self) -> logging.FileHandler:
        """Возвращает регистратор для файла."""
        formatter = logging.Formatter(self.LOG_FORMAT, style="{")

        handler = logging.FileHandler("bot.log", encoding="utf8")
        handler.setFormatter(formatter)

        return handler
    
    def _disable_logs(self) -> None:
        """Отключает посторонние логгеры."""
        level = logging.DEBUG if Backend.debug else logging.CRITICAL
        for log in self.EXTERNAL_LOGS:
            logging.getLogger(log).setLevel(level)
    
    def setup(self) -> None:
        """Установка и настройка регистраторов."""
        self.log.setLevel(self.LOG_LEVEL)
        self._disable_logs()
        
        self.log.addHandler(self._stream_handler())
        self.log.addHandler(self._file_handler())