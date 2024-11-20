import asyncio
from aiogram.types import InputFile, Message, FSInputFile, URLInputFile
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, types
import logging
import yt_dlp as ydl
import os

from config import TOKEN, PATH

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

video_title = ""
video_ext = ""

async def download_video(url, download_path):
    global video_title, video_ext
    options = {
        'format': 'best',  # выбираем лучший формат
        'outtmpl': download_path + '/%(title)s.%(ext)s',
        'progress_hooks': [lambda d: print(f"Downloading {d['filename']} - {d['_percent_str']} completed.")],
        'noplaylist': True
    }

    with ydl.YoutubeDL(options) as ydl_instance:
        info_dict = ydl_instance.extract_info(url, download=True)
        video_title = info_dict.get("title", "video")
        video_ext = info_dict.get("ext", "mp4")
        print(f"Video '{video_title}.{video_ext}' has been downloaded successfully!")


@dp.message(Command("download"))
async def start(message: types.Message):
    split_url = message.text.split(" ", 1)
    if len(split_url) < 2:
        await message.answer("Please provide a valid URL. Usage: /download <url>")
        return

    url = split_url[1]

    try:
        video_title, video_ext = await download_video(url, PATH)  # Adjusted function
        await message.answer(f"Successfully downloaded: {video_title}{video_ext}")

        # Send the video file
        video_path = os.path.join(PATH, f"{video_title}{video_ext}")
        video_file = FSInputFile(video_path)
        await message.answer_video(video_file)

    except Exception as e:
        await message.answer(f"Failed to download the video. Error: {str(e)}")
        await message.answer(f"{video_title}{video_ext}")

@dp.message(Command("save"))
async def start(message: types.Message):
# отправка уже скачаного файла с директории
    image_from_pc = FSInputFile("data/1.mp4") #requests to large (Telegram API limit 50 MB)
    result = await message.answer_video(
        image_from_pc,
        caption="Изображение из файла на компьютере"
    )

    image_from_url = URLInputFile("https://picsum.photos/seed/groosha/400/300")
    result = await message.answer_photo(
        image_from_url,
        caption="Изображение по ссылке"
    )
    
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
