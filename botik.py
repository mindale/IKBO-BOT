import telebot
from telebot import types
bot = telebot.TeleBot("6443109191:AAESu0XmuLvFdFqzaYNGeiVrnr2gP6bk7-U")
@bot.message_handler(content_types=["text", "document", "audio"])
# basa_slov = {'privet':[], 'comands':[]}
# def main(message):
#     if message.text == 'Привет':#basa_slov['privet']:
#         bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, "Я могу: ")
#     elif message.text == "Включи":
#           keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
#           key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
#           keyboard.add(key_yes); #добавляем кнопку в клавиатуру
#           key_no= types.InlineKeyboardButton(text='Нет', callback_data='no');
#           keyboard.add(key_no);
#           question = "Ты хочешь стать програмистом?";
#           bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю.")
#     print(message.text, message.from_user.id)



@bot.message_handler(content_types=['text'])
@bot.message_handler(commands=['reg', 'register'])
def registration(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут? ")
        bot.register_next_step_handler(message, get_name())
    else:
        bot.send_message(message.from_user.id, text='Введите /reg')




    # keyboard = types.InlineKeyboardMarkup()
    # id = message.from_user.id
    # bot.send_message(message.from_user.id, "Введите ваше имя:")
    # bot.register_next_step_handler(message, message.text)
    # name = message.text
    # bot.send_message(message.from_user.id, "Введите вашу фамилию:")
    # bot.register_next_step_handler(message, message.text)
    # surname = message.text
    # bot.send_message(message.from_user.id, "Введите ваше отчество:")
    # bot.register_next_step_handler(message, message.text)
    # otch = message.text
    # bot.send_message(message.from_user.id, "Введите вашу группу")
    # bot.register_next_step_handler(message, message.text)
    # group = message.text
    # question = "Тебя зовут " + name + " " + surname + " " + otch + " ты из группы: " + group + " твой айди: " + id
    # bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    # key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    # keyboard.add(key_yes)
    # key_no = types.InlineKeyboardButton(text='Но', callback_data="no")
    # keyboard.add(key_no)

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_users.id, "Какая у тебя фамилия?")
    bot.register_next_step_handler(message, get_surname())
def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_users.id, "Какая у тебя фамилия?")
    bot.register_next_step_handler(message, get_otch())
def get_otch(message):
    global otch
    otch = message.text
    bot.send_message(message.from_users.id, "Какая у тебя фамилия?")
    bot.register_next_step_handler(message, get_group())
def get_group(message):
    global group
    keyboard = types.InlineKeyboardMarkup()
    id = message.from_user.id
    group = message.text
    bot.send_message(message.from_users.id, "Какая у тебя фамилия?")
    bot.register_next_step_handler(message, get_surname())
    question = "Тебя зовут " + name + " " + surname + " " + otch + " ты из группы: " + group + " твой айди: " + id
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Но', callback_data="no")
    keyboard.add(key_no)




@bot.callback_query_handler(func=lambda call:True)
def call_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Я запомнил тебя)")
        baza = {id: [name, surname, otch, group]}
    else:
        bot.send_message(call.message.chat.id, "Где я ультрамеганасрал?")
    print(id, baza[id])
# @bot.message_handler(comands=['help'])
# def cnopka(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     markup_2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     news = types.KeyboardButton("Новости")
#     dz = types.KeyboardButton("Домашка, контрольные, сессии")
#     vuz = types.KeyboardButton("Ты в вузе?")
#     dr = types.KeyboardButton("Ближайшее др")
#     rasp = types.KeyboardButton("Расписание")
#     markup.add(vuz)
#     markup_2.add(news)
#     bot.send_message(message.chat.id, "Первые новости: ", reply_markup=markup_2)
#     bot.send_message(message.chat.id, "Перейди на темную сторону", reply_markup=markup)


# @bot.callback_query_handler(func=lambda call: True)
# def call_worker(call):
#     if call.data == "news":
#         bot.send_message(call.message.chat.id, "Первый новости:")
bot.polling(none_stop=True, interval=0)