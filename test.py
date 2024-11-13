# тест асинхроности
import asyncio
from datetime import datetime
import time

async def fetch_data1():
    print(f"{datetime.now().strftime('%H:%M:%S')} Начинаем запрос данных...1")
    await asyncio.sleep(2)  # Имитируем задержку ответа
    print(f"{datetime.now().strftime('%H:%M:%S')} Данные получены!1")

async def fetch_data():
    print(f"{datetime.now().strftime('%H:%M:%S')} Начинаем запрос данных...")
    await asyncio.sleep(5)  # Имитируем задержку ответа
    # time.sleep(5)
    print(f"{datetime.now().strftime('%H:%M:%S')} Данные получены!")

async def main():
    await asyncio.gather(fetch_data(), fetch_data1())

asyncio.run(main())
