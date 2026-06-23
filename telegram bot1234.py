import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.callback_query import CallbackQuery
import sqlite3

# Bot tokeningiz
TOKEN = '7610424429:AAG1q3cH67RLXq0C5-vifg6b2KoZ9gzF4ow'
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Kanal ID
channel_id = '@MEHIROQIBAT_Z_V_R'  # Kanal ID formatini to'g'ri kiriting

# Ma'lumotlar bazasi sozlamalari
def initialize_database():
    try:
        conn = sqlite3.connect('bot_data.db')
        cursor = conn.cursor()

        # Subscribers jadvali yaratish
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS subscribers (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                last_name TEXT
            )
        ''')

        conn.commit()
    except sqlite3.Error as e:
        print(f"Ma'lumotlar bazasi xatoligi: {e}")
    finally:
        conn.close()

# Inline tugmalarni yaratish
def inline_buttons():
    builder = InlineKeyboardBuilder()
    builder.button(text="Kanalimiz", url="https://t.me/MEHIROQIBAT_Z_V_R")
    builder.button(text="A'zo bo'ldim", callback_data="subdone")
    builder.adjust(1)
    return builder.as_markup()

# Foydalanuvchini bazaga qo'shish
def add_user_to_db(user_id, username, first_name, last_name):
    try:
        conn = sqlite3.connect('bot_data.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR IGNORE INTO subscribers (user_id, username, first_name, last_name)
            VALUES (?, ?, ?, ?)
        ''', (user_id, username, first_name, last_name))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Ma'lumotlar bazasi xatoligi: {e}")
    finally:
        conn.close()

# Start komandasi
@dp.message(Command("start"))
async def start_command(message: types.Message):
    add_user_to_db(
        user_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    await message.answer("Kanalimizga a'zo bo'ling", reply_markup=inline_buttons())

# A'zo bo'lganini tekshirish
@dp.callback_query(lambda callback: callback.data == "subdone")
async def check_sub(callback: CallbackQuery):
    try:
        user_status = await bot.get_chat_member(chat_id=channel_id, user_id=callback.from_user.id)
        if user_status.status != 'left':
            await callback.message.answer("Kanalga a'zo bo'lganingiz uchun rahmat!")
        else:
            await callback.message.answer(
                "Iltimos, avval kanalimizga a'zo bo'ling.",
                reply_markup=inline_buttons()
            )
    except Exception as e:
        await callback.message.answer("Xatolik yuz berdi.")
        print(f"Callback xatoligi: {e}")

# Xabarni qayta ishlash
@dp.message()
async def handle_message(message: types.Message):
    try:
        user_status = await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)
        if user_status.status != 'left':
            # Foydalanuvchidan kelgan komandani olish
            command = message.text.lower()

            # Faqat javob berish
            if command == "sh":
                await message.answer("Siz 'sh' komandasi yubordingiz.")
            elif command == "r":
                await message.answer("Siz 'r' komandasi yubordingiz.")
            else:
                await message.answer("Iltimos, 'sh' yoki 'r' deb yozing.")
        else:
            await message.answer("Kanalimizga a'zo bo'ling.", reply_markup=inline_buttons())
    except Exception as e:
        await message.answer("Xabarni qayta ishlashda xatolik yuz berdi.")
        print(f"Xabarni qayta ishlash xatoligi: {e}")

# Asosiy ishga tushirish
async def main():
    initialize_database()
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Polling xatoligi: {e}")

if __name__ == '__main__':
    asyncio.run(main())
