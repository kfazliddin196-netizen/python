from telebot import telebot
bot=telebot.TeleBot('6862373349:AAGP--7zKiPiTqfxAcTtz2pPvHPqjjx6V-w')
@bot.message_handler(commands=['start'])
def start(message):
    name=str(message.from_user.first_name)
    bot.send_message(message.from_user.id,'dasturchi bo\'timizga xush kelibsiz'+name)
#bu yerda user /start bosganda Isminmi olib salom qo'shib yuboradi

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,'sizga qanday yordam kerak')
@bot.message_handler(content_types=['text'])
def send(message):
    text=message.text
    if text == 'Python':
        bot.send_message(message.from_user.id, 'Salom Python Programmist')
    elif text == 'Java':
        bot.send_message(message.from_user.id, 'Salom Java Programmist')
    elif text == 'Php':
        bot.send_message(message.from_user.id, 'Salom Php Programmist')
    elif text == 'C#':
        bot.send_message(message.from_user.id, 'Salom C# Programmist')
    else:
        bot.send_message(message.from_user.id, 'Uzur men sizni tanimadim 😑😂')



bot.polling(none_stop=True)  # bu botimiz ochib qolmasligi uchun!
