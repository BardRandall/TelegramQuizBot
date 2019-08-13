import telebot
from model import *
from telebot import types


API_TOKEN = '617318489:AAGuwWvdS8KG5YUSoq9Us5s6FHOPOMmmdys'

bot = telebot.TeleBot(API_TOKEN)


chat_data = {}


def ask_question(chat, question):
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    for answer in question.answers:
        btn = types.KeyboardButton(answer)
        markup.add(btn)
    bot.send_message(chat_id=chat.chat_id, text=question.question, reply_markup=markup)


def start_game(message):
    chat_data[message.chat.id] = Chat(message.chat.id)
    bot.send_message(chat_id=message.chat.id, text='Привет! Давай сыграем в викторину')
    bot.send_message(chat_id=message.chat.id, text='Внимание... Первый вопрос')
    ask_question(chat_data[message.chat.id], chat_data[message.chat.id].get_current_question())


@bot.message_handler(commands=['start', 'help'])
def start(message):
    if message.chat.id in chat_data:
        return
    start_game(message)


@bot.message_handler(commands=['restart'])
def restart(message):
    if message.chat.id not in chat_data:
        return
    start_game(message)


@bot.message_handler(func=lambda message: True)
def handle_answers(message):
    chat = chat_data[message.chat.id]
    question = chat_data[message.chat.id].get_current_question()
    if message.text not in question.answers:
        bot.send_message(chat_id=message.chat.id, text='Выберите один из предложенных вариантов ответов')
        return
    if message.text == question.get_right_answer():
        bot.send_message(chat_id=message.chat.id, text='Верно!')
        if not chat.questions_left:
            bot.send_message(chat_id=message.chat.id, text='Игра окончена! Нажмите /restart чтобы начать заново',
                             reply_markup=types.ReplyKeyboardRemove(selective=False))
            return
        bot.send_message(chat_id=message.chat.id, text='Внимание! Следующий вопрос')
        next_question = chat.get_next_question()
        ask_question(chat, next_question)
    else:
        bot.send_message(chat_id=message.chat.id, text='Неверный ответ, попробуйте еще раз')


bot.polling()
