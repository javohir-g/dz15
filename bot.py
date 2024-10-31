import telebot

bot = telebot.TeleBot(token='7927478236:AAEaWaz1v2rNK9W5Oc2cZ7PPRjDhaZZMUHk')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать!")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Справка:\n/start - Приветствие\n/help - Справочная информация")


bot.polling()
