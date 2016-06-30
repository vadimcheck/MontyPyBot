# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot("238364651:AAGx-QLdnwiDMDPFa7_Io9l2Nzzj8qj-EOg")
ids = ['feromonpapa', 2, 3]
authorized_users = []

if 'feromonpapa' in ids:
    # uid - id пользователя в telegram
    authorized_users.append('feromonpapa')

# Используем этот декоратор перед всеми функциями где нужна авторизация
def check_auth(func):
    def wrapper(uid):
        if uid in authorized_users:
             func()
        else:
            pass


if __name__ == '__main__':
    bot.polling(none_stop=True)
@bot.message_handler(commands=['start'])

def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'Привет! Я MontyPybot!')

@bot.message_handler(commands=['auth'])
def send_auth(message):
    pass

@bot.message_handler(commands=['abs'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'abs(x) Модуль числа!')

@bot.message_handler(commands=['^'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'x ^ y Побитовое исключающее или')

@bot.message_handler(commands=['&'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'x & y Побитовое и')

@bot.message_handler(commands=['<<'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'Битовый сдвиг влево')

@bot.message_handler(commands=['**'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'x ** y	Возведение в степень')

@bot.message_handler(commands=['pow'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'pow(x, y[, z])	xy по модулю (если модуль задан)')

@bot.message_handler(commands=['%'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'x % y	Остаток от деления')

@bot.message_handler(commands=['|'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'x % y	Остаток от деления')

@bot.message_handler(commands=['>>'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'x >> y	Битовый сдвиг вправо')

@bot.message_handler(commands=['%'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'x | y	Побитовое или')

@bot.message_handler(commands=['~'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, '~x	Инверсия битов')

@bot.message_handler(commands=['int.bit_length()'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'Количество бит, необходимых для представления числа в двоичном виде, без учёта знака и лидирующих нулей.')

@bot.message_handler(commands=['int.to_bytes'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'int.to_bytes(length, byteorder, *, signed=False) - возвращает строку байтов, представляющих это число.')

@bot.message_handler(commands=['int.from_bytes'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'classmethod int.from_bytes(bytes, byteorder, *, signed=False) - возвращает число из данной строки байтов')





bot.polling()
