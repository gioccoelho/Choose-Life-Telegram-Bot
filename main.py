import os
import telebot
import random

TELEGRAM_API = os.getenv('TELEGRAM_API')
bot = telebot.TeleBot(TELEGRAM_API)

messages = [
    'Choose a job',
    'Choose a career',
    'Choose a family',
    'Choose a big television',
    'Choose washing machines, cars, compact disc players and electrical tin openers',
    'Choose leisure wear and matching luggage',
    'Choose a three-piece suit on hire purchase in a range of fabrics',
    'Choose DIY and wondering who you are on a Sunday morning',
    'Choose sitting on that couch watching mind-numbing, spirit-crushing game shows, stuffing junk food into your mouth',
    'Choose rotting away at the end of it all, in a miserable home, nothing more than an embarassment to the selfish brats that you spawned to replace yourselves',
    'Choose your future',
    'Choose life',
]
    
@bot.message_handler(func=lambda message: True)
def send_message(message):
    print(f'@{message.chat.username} {message.chat.first_name} {message.chat.last_name}: {message.text}')
    if message.text == 'choose':
        bot_message = random.choice(messages)
    else:
        bot_message = 'You must type in \'choose\''
    bot.send_message(message.chat.id, bot_message)
    print(f'@chooselifebr_bot Choose Life: {bot_message}')

bot.polling()
