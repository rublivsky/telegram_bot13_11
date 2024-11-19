import asyncio
from aiogram import Bot, Dispatcher
import logging
from aiogram import Router

from config import TOKEN

logging.basicConfig(level=logging.INFO)

router = Router(name=__name__)
bot = Bot(token=TOKEN)
dp = Dispatcher()

DOWNLOAD_PATH = 'data/'

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
