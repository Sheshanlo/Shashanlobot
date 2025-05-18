import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand
from aiogram.enums import ParseMode
from aiohttp import web
import os

# Получаем токен из переменных среды
BOT_TOKEN = os.getenv("7715851506:AAGBHSajIKsivQ5tvZpnVjqsSX9WhqMxWv8")
WEBHOOK_HOST = 'https://sheshanloassistant.onrender.com'
WEBHOOK_PATH = f'/webhook'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Ассистент готов к работе, Хозяин.")

# Настройка webhook при старте
async def on_startup(app: web.Application):
    await bot.set_webhook(WEBHOOK_URL)

# Удаление webhook при выключении
async def on_shutdown(app: web.Application):
    await bot.delete_webhook()

# Хендлер для входящих webhook-запросов
async def handle_webhook(request):
    body = await request.read()
    update = types.Update.model_validate_json(body.decode("utf-8"))
    await dp.feed_update(bot, update)
    return web.Response()

# Создание веб-сервера
def create_app():
    app = web.Application()
    app.router.add_post(WEBHOOK_PATH, handle_webhook)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    return app

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    web.run_app(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
