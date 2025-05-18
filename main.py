import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import os

API_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=["start"])
async def send_welcome(message: Message):
    await message.reply("Ассаляму алейкум, Хозяин. Я готов к работе.")

@dp.message_handler(commands=["help"])
async def help_command(message: Message):
    await message.reply("Команды:\n/start — запуск\n/help — помощь")
/start — запуск
/help — помощь")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
