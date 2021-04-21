import smtplib
import requests
import wikipedia
from data.keyboards.scr import *
import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
from requests.exceptions import ReadTimeout
from scripts.table import data
from random import choice
from scripts.parser import get_p

token = "b192ac9e1f0ae17eee1dd0b74264e17c6ffb4bbfd4a1a684ab428f6b5d7d11208281a1e5214169db1088e"
vk_session = vk_api.VkApi(token=token)
s_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
users = eval(open('users.txt', mode='r+', encoding='utf-8').read())
wikipedia.set_lang("ru")

while True:
    while True:
        try:
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW:
                    msg = event.text
                    if event.from_user and not event.from_me:
                        if event.user_id not in list(users.keys()):
                            users[event.user_id] = {'act': 'menu'}
                            vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Функции бота: ',
                                                                'keyboard': menu_kb(), 'random_id': 0})
                        else:
                            if users[event.user_id]["act"] == "menu":
                                if msg.lower() == 'википедия':
                                    users[event.user_id]["act"] = "wiki"
                                    vk_session.method('messages.send',
                                                      {'user_id': event.user_id, 'message': 'Введите термин: ',
                                                       "keyboard": menu_wiki(), 'random_id': 0})
                                if msg.lower() == 'игры':
                                    users[event.user_id]["act"] = "games"
                                    vk_session.method('messages.send',
                                                      {'user_id': event.user_id, 'message': 'Ты перешел в меню игр',
                                                       "keyboard": games_kb(), 'random_id': 0})
                                if msg.lower() == "отправить e-mail":
                                    users[event.user_id]["act"] = "mail"
                                    vk_session.method('messages.send',
                                                      {'user_id': event.user_id,
                                                       'message': 'Введите email получателя: ', 'random_id': 0})
                                if msg.lower() == "приколы с яндекс.картами":
                                    users[event.user_id]["act"] = "maps"
                                    vk_session.method('messages.send',
                                                      {'user_id': event.user_id,
                                                       'message': 'Ты в меню Яндекс.Карт', "keyboard": maps_kb(),
                                                       'random_id': 0})
                            if users[event.user_id]["act"] == "maps":
                                if msg.lower() == "назад":
                                    users[event.user_id]["act"] = "menu"
                                    vk_session.method('messages.send',
                                                      {'user_id': event.user_id, 'message': 'Функции бота: ',
                                                       'keyboard': menu_kb(), 'random_id': 0})
                                else:
                                    if msg.lower() == "фрагмент карты по ее координатам":
                                        if msg.lower() == 'назад':
                                            users[event.user_id]["act"] = "maps"
                                            vk_session.method('messages.send',
                                                              {'user_id': event.user_id,
                                                               'message': 'Ты в меню Яндекс.Карт',
                                                               "keyboard": maps_kb(),
                                                               'random_id': 0})
                                        else:
                                            vk_session.method('messages.send',
                                                              {'user_id': event.user_id, 'message': 'Введите широту и '
                                                                                                    'долготу через '
                                                                                                    'пробел и с 6 '
                                                                                                    'знаками после '
                                                                                                    'запятой (пример '
                                                                                                    '65.000000)',
                                                               'keyboard': ins_map_kb(), 'random_id': 0})
                                            try:
                                                ll1 = str(msg).split()[0]
                                                ll2 = str(msg).split()[1]
                                                with open("img.png", "wb") as file:
                                                    resp = requests.get(f"https://static-maps.yandex.ru/1.x/?ll={ll1},{ll2}&spn=0.016457,0.00619&l=map")
                                                    file.write(resp.content)
                                            except ValueError:
                                                users[event.user_id]["act"] = "maps"
                                                vk_session.method('messages.send',
                                                                  {'user_id': event.user_id,
                                                                   'message': 'Вы ввели не число. Попробуйте сначала.',
                                                                   'keyboard': maps_kb(), 'random_id': 0})

                            if users[event.user_id]["act"] == "wiki":
                                if msg.lower() == "назад":
                                    users[event.user_id]["act"] = "menu"
                                    vk_session.method('messages.send',
                                                      {'user_id': event.user_id, 'message': 'Функции бота: ',
                                                       'keyboard': menu_kb(), 'random_id': 0})
                                else:
                                    if msg.lower() != 'википедия':
                                        try:
                                            x = wikipedia.page(msg)
                                            y = x.url
                                            vk_session.method('messages.send',
                                                            {'user_id': event.user_id, 'message': f'{x.content[:300]}...',
                                                             'keyboard': wiki_msg(y), 'random_id': 0})
                                        except wikipedia.exceptions.DisambiguationError as e:
                                            y = f'https://ru.wikipedia.org/wiki/{"_".join(msg.split())}'
                                            vk_session.method('messages.send',
                                                              {'user_id': event.user_id,
                                                               'message': f'Мы нашли список значений. Он в ссылке',
                                                               'keyboard': wiki_msg(y), 'random_id': 0})
                            if users[event.user_id]["act"] == "games":
                                if msg.lower() == "назад":
                                    users[event.user_id]["act"] = "menu"
                                    vk_session.method('messages.send',
                                                      {'user_id': event.user_id, 'message': 'Функции бота: ',
                                                       'keyboard': menu_kb(), 'random_id': 0})
                                elif msg.lower() == "города":
                                    if msg.lower() == 'прервать игру':
                                        users[event.user_id]["act"] = "games"
                                        isBreak = True
                                        vk_session.method('messages.send',
                                                          {'user_id': event.user_id, 'message': 'Ты перешел в меню игр',
                                                           "keyboard": games_kb(), 'random_id': 0})
                                    else:
                                        isBreak = False
                                        users[event.user_id]["act"] = "city"
                                        last_city = choice(data)
                                        vk_session.method('messages.send',
                                                          {'user_id': event.user_id,
                                                           'message': f'Я начинаю: {last_city}',
                                                           'keyboard': cities_kb(), 'random_id': 0})
                                        while not isBreak:
                                            city = msg.lower()
                                            if city[0] == last_city[-1] and city in data:
                                                for i in data:
                                                    if i[0] == city[-1]:
                                                        last_city = city
                                                        vk_session.method('messages.send',
                                                                          {'user_id': event.user_id,
                                                                           'message': last_city,
                                                                           'keyboard': cities_kb(), 'random_id': 0})
                                            else:
                                                vk_session.method('messages.send',
                                                                  {'user_id': event.user_id,
                                                                   'message':
                                                                       "Город не соответствует условию. Введите другой",
                                                                   'keyboard': cities_kb(), 'random_id': 0})
                    save = open('users.txt', mode='w', encoding='utf-8').write(str(users))
        except ReadTimeout:
            break
