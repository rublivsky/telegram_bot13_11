import os
import yt_dlp as ydl
from aiogram import types
from aiogram.types import InputFile
from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message

from bot import router, bot
from config import DOWNLOAD_PATH

async def download_video(url, path):
    options = {
        'format': 'best',
        'outtmpl': path + '/%(title)s.%(ext)s',
        'progress_hooks': [lambda d: print(f"Downloading {d['filename']} - {d['_percent_str']} completed.")],
        'noplaylist': True
    }

    with ydl.YoutubeDL(options) as ydl_instance:
        info_dict = ydl_instance.extract_info(url, download=True)
        video_title = info_dict.get("title", "video")
        video_ext = info_dict.get("ext", "mp4")
        return os.path.join(path, f"{video_title}.{video_ext}")

@router.message(Command('start'))
async def start(message: types.Message):
    await message.answer("Отправьте ссылку на видео с YouTube.")

@router.message()
async def handle_video_link(message: types.Message):
    url = message.text
    await message.answer("Загрузка видео...")
    
    video_path = await download_video(url, DOWNLOAD_PATH)
    
    with open(video_path, "rb") as video_file:
        video_input = InputFile(video_file)
        await bot.send_video(message.chat.id, video=video_input, caption="Ваше видео!")

@router.message(Command("file"))
async def send_file(message: types.Message):
    pass