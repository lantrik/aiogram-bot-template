from src.core import Bot

from aiogram import Router
from aiogram.types import Message

from .keyboards import problem_keyboard

bot = Bot()

router = Router()

@router.message(commands=["start"])
async def start_command(message: Message) -> None:
    await bot.send_chat_action(chat_id=message.chat.id, action='TYPING')
    await message.answer("Привет!")

    await bot.send_chat_action(chat_id=message.chat.id, action='TYPING')
    await message.answer("Для начала, можешь выбрать одну из тем, которые тебя беспокоят? 😣")

    await bot.send_chat_action(chat_id=message.chat.id, action='TYPING')
    await message.answer(
        "Главное — помни, что не только ты можешь столкнуться с трудностями, они бывают у всех.",
        reply_markup=problem_keyboard()
        )
