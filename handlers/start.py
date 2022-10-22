from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from src.ext.utils import get_json


router = Router()

@router.message(Command(commands=["start"]))
async def start_command(message: Message) -> None:
    texts = get_json("start")

    for text in texts["hello"]:
        await message.answer(text=text)