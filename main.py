from aiogram import Bot, Dispatcher, executor, types

BOT_TOKEN = "7715851506:AAGBHSajIKsivQ5tvZpnVjqsSX9Wh...""

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Ассаляму Аллейкум, Хозяин!")

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
