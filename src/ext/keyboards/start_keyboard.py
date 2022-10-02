from re import L
from typing import List

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_keyboard() -> ReplyKeyboardMarkup:
    keyboard_list: List[List[KeyboardButton]]  = [
        [
            KeyboardButton(text="Общение"),
            KeyboardButton(text="Одиночество")
        ],
        [
            KeyboardButton(text="Конфликты"),
            KeyboardButton(text="Выгорание")
        ],
        [
            KeyboardButton(text="Бабочки в животе")
        ],
        [
            KeyboardButton(text="Другое")
        ]
    ]

    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=keyboard_list,
        resize_keyboard=True,
        input_field_placeholder="Выбери проблему..."
    )
    return keyboard