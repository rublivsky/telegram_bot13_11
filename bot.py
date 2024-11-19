import asyncio
from aiogram.types import InputFile, Message, FSInputFile
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, types
import logging
# import yt_dlp as ydl

from config import TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    image_from_pc = FSInputFile("data/1.mp4")
    await message.answer_video(image_from_pc)



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
