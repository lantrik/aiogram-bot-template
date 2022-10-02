from aiogram import Router
from aiogram.filters import ContentTypesFilter
from aiogram.types import Message


router = Router()

@router.message(ContentTypesFilter(content_types="text"))
async def echo(message: Message) -> None:
    await message.answer(message.text)