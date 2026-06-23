
import telebot
bot=telebot.TeleBot('6401957447:AAHsgpjY8re7uywbEnb7Jo32qAWmTqKiAwc')
@bot.message_handler(commands=['start'])
def start(message):
    name=str(message.from_user.first_name)
    bot.send_message(message.from_user.id,'salom'+name)
#bu yerda user /start bosganda Isminmi olib salom qo'shib yuboradi

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,'sizga qanday yordam kerak')
@bot.message_handler(content_types=['text'])
def send(message):
    text=message.text
    if text == 'Fazliddin':
        bot.send_message(message.from_user.id, 'Siz bilan tanishganimdan xursandman')
    elif text == 'Yigitiz bormi':
        bot.send_message(message.from_user.id, 'Yigitim yo\'q')
    elif text == 'Man bilan gaplashasizmi':
        bot.send_message(message.from_user.id, 'bilmasam')
    elif text == 'Qatta turasiz':
        bot.send_message(message.from_user.id, 'Nazarbek')
    elif text=='Qaysi Maktabda o\'qisiz':
        bot.send_message(message.from_user.id,'8-Maktabda o\'qirdim xozir kolejda o\'qiman o\'zizchi😉')
    elif text=='Man ham ko\'lejda o\'qiman':
        bot.send_message(message.from_user.id,'hm')
    else:
        bot.send_message(message.from_user.id, 'Uzur men sizni tanimadim 😑😂')
bot.polling(none_stop=True)  # bu botimiz ochib qolmasligi uchun!
