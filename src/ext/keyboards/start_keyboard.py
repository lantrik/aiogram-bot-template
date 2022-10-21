from typing import List

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def problem_keyboard() -> ReplyKeyboardMarkup:
    keyboard_list: List[List[KeyboardButton]]  = [
        [
            KeyboardButton(text="Домашнее насилие"),
            KeyboardButton(text="Химическая зависимость")
        ],
        [
            KeyboardButton(text="Буллинг"),
            KeyboardButton(text="Бодишейминг")
        ],
        [
            KeyboardButton(text="Селфхарм"),
            KeyboardButton(text="Суицид")
        ],
        [
            KeyboardButton(text="Беременность"),
            KeyboardButton(text="Сексуальное насилие")
        ]
    ]

    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=keyboard_list,
        resize_keyboard=True,
        input_field_placeholder="Выбери одну из тем"
    )
    return keyboard