from aiogram.types import (
    Message,
    ReplyKeyboardRemove
)
from aiogram import Router
from aiogram.filters.text import Text

from src.ext.keyboards import start_keyboard


router = Router()

@router.message(commands=["start"])
async def start_command(message: Message) -> None:
    await message.answer(
        "Привет, что тебя тревожит? Я постараюсь помочь тебе!",
        reply_markup=start_keyboard()
    )

@router.message(Text(text="Общение", text_ignore_case=True))
async def callback(message: Message) -> None:
    await message.answer("ок.", reply_markup=ReplyKeyboardRemove())

@router.message(Text(text="Одиночество", text_ignore_case=True))
async def callback(message: Message) -> None:
    await message.answer("ок.", reply_markup=ReplyKeyboardRemove())

@router.message(Text(text="Конфликты", text_ignore_case=True))
async def callback(message: Message) -> None:
    message.answer("ок., reply_markup= ", reply_markup=ReplyKeyboardRemove())

@router.message(Text(text="Выгорание", text_ignore_case=True))
async def callback(message: Message) -> None:
    await message.answer("ок.", reply_markup=ReplyKeyboardRemove())

@router.message(Text(text="Бабочки в животе", text_ignore_case=True))
async def callback(message: Message) -> None:
    await message.answer("ок.", reply_markup=ReplyKeyboardRemove())

@router.message(Text(text="Другое", text_ignore_case=True))
async def callback(message: Message) -> None:
    await message.answer("ок.", reply_markup=ReplyKeyboardRemove())