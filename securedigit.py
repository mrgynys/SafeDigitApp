import telebot
from gpt import GPTManager

bot = telebot.TeleBot("6407401354:AAFwK3IXs_Nqra6rlWHsROxtYyFsBw7roC8", parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Чем я могу помочь?")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Я могу вам помочь в вашей личной информационной безопасности. Напишите ваш вопрос.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, GPTManager().send(message.text))


bot.infinity_polling()