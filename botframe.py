import telebot
import keyfile
import app
import app_2

bot = telebot.TeleBot(keyfile.key)


@bot.message_handler(commands=["card"])
def check_price(message):
    i = 1
    crawling = app.craw()
    while i <= 5:
        msg = crawling[i]
        msg = msg[4:]
        msg = msg.replace(")$", ") $").replace("￦", " ￦").split()
        bot.send_message(message.chat.id, "국가 : " + msg[0] + "\nUSD : " + msg[2] + "\n오늘 가격 : "+ msg[3])
        i += 1


@bot.message_handler(commands=["fakebow"])
def fire_egg(message):
    bot.send_message(message.chat.id, "주요 정체구간 정보" + app_2.easter_egg())


bot.polling()
