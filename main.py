from config import *
import telebot
from telebot import types

bot = telebot.TeleBot(TOKEN)

user_states = {}


@bot.message_handler(commands=['start'])
def start_command(message):
    '''handle a command /start'''
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    user_name = message.from_user.first_name
    # buttons 
    button_main_menu = types.KeyboardButton(main_menu)
    button_help = types.KeyboardButton(help)
    button_info = types.KeyboardButton(info)
    markup.row(button_main_menu)
    markup.row(button_help, button_info)
    
    # kAzAnTiP 2010 🤘
    bot.send_message(
        message.chat.id,
        welcome_text(user_name),
        reply_markup = markup
    )

@bot.message_handler(func = lambda message: message.text in button_text.values())
def button_handler(message):
    if (message.text == main_menu):
        bot.send_message(
            message.chat.id, 
            'main menu'
        )
    if (message.text == info):
        bot.send_message(
            message.chat.id,
            info_text,
            parse_mode = 'HTML'
        )


bot.infinity_polling()