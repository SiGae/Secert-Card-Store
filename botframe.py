import telebot
import keyfile

bot = telebot.TeleBot(keyfile.key)


@bot.message_handler(commands=["ping"])
def check_price(message):
    bot.send_message(message.chat.id, "ping")


bot.polling()
