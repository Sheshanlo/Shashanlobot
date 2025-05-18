import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

# Установите ваш токен Telegram-бота
API_TOKEN = "7715851506:AAGBHSajIKsivQ5tvZpnVjqsSX9WhqMxWv8"

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Инициализируем бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def cmd_start(message: Message):
    await message.reply("Бот запущен. Введите команду.\nПримеры:\n/start - запуск\n/help - помощь")

@dp.message_handler(commands=["help"])
async def cmd_help(message: Message):
    await message.reply("Доступные команды:\n/start - запуск\n/help - помощь")

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
