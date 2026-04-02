import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

# --- Твой токен Telegram бота ---
TOKEN = "8641636490:AAGbMwRjor0IP3FKa6uYwWzIrhLtaBXVEwM"

bot = Bot(token=TOKEN)
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

# --- Твой токен Telegram бота ---
TOKEN = "8641636490:AAGbMwRjor0IP3FKa6uYwWzIrhLtaBXVEwM"
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import os

# --- Получаем токен из переменных окружения ---
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- Соцсети с эмодзи ---
SOCIALS = {
    "📺 YouTube": "https://www.youtube.com/@1440shorts",
    "✈️ Telegram": "https://t.me/Ismal_1440",
    "📸 Instagram": "https://instagram.com/isma1l_erzi"
}

# --- Клавиатура (красиво по 2 в ряд) ---
def main_keyboard():
    buttons = [types.InlineKeyboardButton(text=name, url=link) for name, link in SOCIALS.items()]
    inline_keyboard = []
    for i in range(0, len(buttons), 2):
        inline_keyboard.append(buttons[i:i+2])
    inline_keyboard.insert(0, [types.InlineKeyboardButton(text="🔥 Обо мне", callback_data="about")])
    return types.InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

# --- Старт ---
@dp.message(Command(commands=["start"]))
async def start(message: types.Message):
    await message.answer(
        "🚀 Привет!\n\n"
        "Я блогер, здесь все мои ссылки 👇\n\n"
        "Жми кнопки ниже:",
        reply_markup=main_keyboard()
    )

# --- Callback "Обо мне" ---
@dp.callback_query(lambda c: c.data == "about")
async def about_callback(callback: types.CallbackQuery):
    await callback.message.answer(
        "🔥 Обо мне:\n\n"
        "Я блогер, создаю интересный и полезный контент 😎\n"
        "Подписывайся на мои соцсети и следи за новыми видео!"
    )
    await callback.answer()

# --- Ответ на любое сообщение ---
@dp.message()
async def echo(message: types.Message):
    await message.answer("😎 Напиши /start чтобы открыть меню")

# --- Запуск ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())