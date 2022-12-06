import requests
import random
from bs4 import BeautifulSoup as b
import telebot

url = 'https://www.anekdot.ru/'
api_key = '5102384184:AAEqMVhcihjtBsVsK3Idk7vqilX6FHK8Pbg'


def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anektods = soup.findAll('div', class_='text')
    return [i.text for i in anektods]


list_of_jokes = parser(url)
random.shuffle(list_of_jokes)
bot = telebot.TeleBot(api_key)


@bot.message_handler(commands=['start'])
def hello(massage):
    bot.send_message(
        massage.chat.id,
        'Привет, чтобы посмеяться введи любую цифру:')


@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '11' or message.text.lower() in '22' or message.text.lower() in '33' or message.text.lower() in '44' or message.text.lower() in '55' or message.text.lower() in '66' or message.text.lower() in '77' or message.text.lower() in '88' or message.text.lower() in '99' or message.text.lower() in '1234567890'or message.text.lower() in '100':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Введите число от 1 до 100 :')


bot.polling()
