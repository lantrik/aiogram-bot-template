from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()

@router.message(Command(commands=["start"]))
async def start_command(message: Message) -> None:
    await message.answer("Привет!")