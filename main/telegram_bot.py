import telebot
import requests


TOKEN = '5570969887:AAH8VgMc01rfdLkuHVdrJ1E3Pdi1ft3qTQc'

"""
1. Чтобы узнать свой id в телеграме зайдите к боту:  @username_to_id_bot и напишите ему свой ник ТГ
2. Подключитесь к боту https://t.me/roma_signalka_bot
"""
my_id = 1293474473  # id юзера в телеграмме
telegramBot = telebot.TeleBot(TOKEN)


def dialogue(phone_number, name, question, text):
    return requests.post(url=f'https://api.telegram.org/bot{TOKEN}/sendMessage',
                         data={'chat_id': my_id,
                               'text': f'*Поступила новая заявка:*\nИмя: {name}\n{phone_number}\n{question}\n{text}',
                               }
                         ).json()


def review(phone_number, name, text):
    return requests.post(url=f'https://api.telegram.org/bot{TOKEN}/sendMessage',
                         data={'chat_id': my_id,
                               'text': f'--Ура! Новый отзыв!:--\nИмя: {name}\n{phone_number}\nОтзыв: {text}',
                               }
                         ).json()
