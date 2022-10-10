from aiogram import Router
from aiogram.types import Message
from aiogram.filters.text import Text


router = Router()

@router.message(commands=["start"])
async def start_command(message: Message) -> None:
    await message.answer("Привет, что тебя тревожит? Я постараюсь помочь тебе!")