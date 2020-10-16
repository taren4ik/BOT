
import telebot
import os
from telebot import types
Token = os.environ['token']
bot = telebot.TeleBot(Token)
@bot.message_handler(content_types=['text'])

def send_text(message):
    if message.text == '/start':
        # Пишем приветствие
        #path = open('repos/Bot_One/Bot_One/env/picture/welcome.jpeg','rb')
        bot.send_photo(message.from_user.id,'https://cdn.fishki.net/upload/post/201312/04/1231124/8VfxuiL3w7EwtTe_DX5B2A-article.jpg')
        bot.send_message(message.from_user.id, "You are 18 year?")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()


        key_yes = types.InlineKeyboardButton(text='Yes', callback_data='yes_me')
        key_no = types.InlineKeyboardButton(text='No', callback_data='no_me')
        keyboard.row(key_yes, key_no)
        bot.send_message(message.from_user.id, text='Choose yor age', reply_markup=keyboard)
    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Write /start")

    else:

        bot.send_message(message.from_user.id, "I don't understand. Write /help.")


    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):

        # Если подтвержден возраст, то выподает ссылка

        if call.data == "yes_me":

            markup1 = types.InlineKeyboardMarkup()
            btn_my_site = types.InlineKeyboardButton(text='My site', url='https://redtube.com/pornostar')
            markup1.add(btn_my_site)            
            bot.send_message(message.chat.id, "Push button and go to site.", reply_markup=markup1)
           
            
                # Отправляем текст в Телеграм
                #bot.send_message(call.message.chat.id, msg)

        elif call.data == "no_me":
            msg = 'Sorry. Content for individuals +18'
            bot.send_message(call.message.chat.id, msg)

bot.polling(none_stop=True, interval=0)
