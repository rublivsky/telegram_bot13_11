from aiogram import Router
from aiogram.types import Message, InputFile
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Hello! This is the start command. Use /download to start downloading a video.")

@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer("To download a video, send the command /download followed by the video URL.")

@router.message(Command("download"))
async def download_handler(message: Message):
    await message.answer("/////")