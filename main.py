import pyTelegramBotAPI.telebot as telebot
import tokenbot
import handler
import tools
bot = telebot.TeleBot(tokenbot.whatnews)

@bot.message_handler(commands=['start'])
def send_commands(message):
    bot.send_message(tokenbot.id_chat, handler.start)

@bot.message_handler(commands=['help'])
def send_commands(message):
    bot.send_message(tokenbot.id_chat, handler.help)

@bot.message_handler(content_types="text")
def send_message(message):
    if (message.text in ["Курс","курс" ,"Exch", "exch"]):
        bot.send_message(tokenbot.id_chat, tools.exch())
    elif (message.text in ["Погода","погода", "weather", "Weather"]):
        bot.send_message(tokenbot.id_chat, tools.weather())
    else:
        bot.send_message(tokenbot.id_chat, message.from_user.first_name + ", you say than: " + message.text)
if __name__ == '__main__':
    bot.polling()
