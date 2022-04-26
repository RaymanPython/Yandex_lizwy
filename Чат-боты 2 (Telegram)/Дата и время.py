import time
import telebot

bot = telebot.TeleBot('5123580062:AAEcL4kGPRRPdZLhUlOzYe-xzKIl8OYTmrg')


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Используйте /time или /date.')


@bot.message_handler(commands=["time"])
def time(m, res=False):
    t = time.localtime()
    asctime = time.asctime(t)
    sp = asctime.split()
    bot.send_message(m.chat.id, f'Текущее время: {sp[3]}')


@bot.message_handler(commands=["date"])
def time(m, res=False):
    t = time.localtime()
    asctime = time.asctime(t)
    sp = asctime.split()
    bot.send_message(m.chat.id, f'Текущая дата: {sp[0]}_{sp[2]}_{sp[1]}_{sp[4]}')


bot.polling(none_stop=True, interval=0)
