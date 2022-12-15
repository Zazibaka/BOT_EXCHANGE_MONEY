import telebot
from telebot import types
import config
import requests
import news
import value_rate as vr

#from telegram.ext import Update,CommandHandler,se
import exchange as ex
 
bot = telebot.TeleBot(config.TOKEN)

# Обрабатываются все сообщения содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start','help'])
def handle_start_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Rate ")
    btn2 = types.KeyboardButton("Exchange ")
    btn3 = types.KeyboardButton("News")
    
    markup.add(btn1,btn2,btn3, )
    bot.send_message(message.chat.id, f"Welcome, {message.chat.username}\n"
                     "Я валютный бот! 🤖\n"
                     "Я помогу узнать актуальный курс! 💸\n"
                     "Посчитать нужную тебе сумму! 💰\n "
                     "Расскажу актуальные новости! 📰\n ", reply_markup=markup)
 
#Создаем функционал кнопок.
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Rate"):
     
        bot.send_message(message.chat.id, text ="Актуальный курс валют")
        bot.send_message(message.chat.id, vr.value_rate())
       
    if(message.text == "Exchange"):
        chat_id = message.chat.id
        text = message.text
        msg = bot.send_message(chat_id, "Обмен валюты: USD EUR GBP CHF JPY\n"
                                        "Укажите вид валюты и нужную сумму\n"
                                        "Пример: USD EUR 1000 ")
        bot.register_next_step_handler(msg,value_exchange)
 
        

    if(message.text == "News"):
        bot.send_message(message.chat.id, text = "Акутальные новости финансового рынка: ")
        bot.send_message(message.chat.id,news.check_news())

def value_exchange(message):
    chat_id = message.chat.id
    text = message.text
    try:
        value_1,value_2,sum_money  = text.split(" ")
        if value_1 == value_2:
            bot.send_message(message.chat.id, text = "Валюта обмена совпадает")
            func(message)
            
        else:
            money = ex.get_exchage_money()
            new_text = ex.calcul_money(money,value_1,value_2,int(sum_money))
            msg = bot.send_message(message.chat.id, f"Cумма к получению: {new_text} {value_2}")

    except ValueError as VE:
        bot.send_message(message.chat.id, f"Ошибка ввода запроса...\n"
                                            "Вы пропустили одно из значений")
    except KeyError:
        bot.send_message(message.chat.id, f"Ошибка ввода данных...\n"
                                            "Вы указали неверное значение валюты")
        

        
        
        
bot.polling(none_stop=True)
