import telebot
import random
import config

bot = telebot.TeleBot(config.TOKEN)
 
@bot.message_handler(commands=['hi'])
def welcome(message):
    bot.send_message(message.chat.id, "привет {0.first_name}, я Наташа кошка".format(message.from_user, bot.get_me()))

@bot.message_handler(commands=['piss'])
def send(message):
    bot.send_message(message.chat.id, "я пописала".format(message.from_user, bot.get_me()))

@bot.message_handler(commands=['poo'])
def send(message):
    bot.send_message(message.chat.id, "я покакала".format(message.from_user, bot.get_me()))

@bot.message_handler(commands=['feed'])
def send(message):
    bot.send_message(message.chat.id, "главное что мы поели".format(message.from_user, bot.get_me()))

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'залупа':
        bot.reply_to(message, "это очень забавно)")
    if message.text.lower() == 'наташа ты альт?':
        bot.reply_to(message, "я альт")
    if message.text.lower() == 'наташа ты стрейт?':
        bot.reply_to(message, "я альт")
    if message.text.lower() == 'наташа кто твой хозяин?':
        bot.reply_to(message, "@klimenko1906")
    if message.text.lower() == 'кто стрейт':
        bot.send_message(message.chat.id, 'кто стрейт выйдите нахуй')
    if message.text.lower() == 'жареная картошка топ':
        bot.send_message(message.chat.id, 'согласна')
    if message.text.lower() == 'доброе утро':
        bot.send_message(message.chat.id, 'доброе')
    if message.text.lower() == 'спокойной ночи':
        bot.send_message(message.chat.id, 'споки')
    if message.text.lower() == 'всем спокойной ночи':
        bot.reply_to(message, "споки")
    if message.text.lower() == 'всем споки':
        bot.reply_to(message, "спокойной ночи {0.first_name}".format(message.from_user, bot.get_me()))
    if message.text.lower() == 'споки':
        bot.send_message(message.chat.id, 'спокойной ночи')
    if message.text.lower() == 'я спать':
        bot.reply_to(message, "спокойной ночи {0.first_name}".format(message.from_user, bot.get_me()))

bot.polling(none_stop=True)
