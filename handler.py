from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Hello! This is the start command.")


@router.message(Command("help"))
async def start_handler(message: Message):
    await message.answer("To any questions, you can tell @rublivskyi")

@router.message(Command("all"))
async def start_handler(message: Message):
    await message.answer("All commands")