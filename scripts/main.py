import smtplib
import wikipedia
from data.keyboards.scr import *
import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
from bs4 import BeautifulSoup
from requests.exceptions import ReadTimeout
import requests

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
                                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Введите термин: ', "keyboard": menu_wiki(), 'random_id': 0})
                                if msg.lower() == 'игры':
                                    users[event.user_id]["act"] = "games"
                                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Ты перешел в меню игр', "keyboard": games_kb(), 'random_id': 0})
                            if users[event.user_id]["act"] == "wiki":
                                if msg.lower() == "назад":
                                    users[event.user_id]["act"] = "menu"
                                    vk_session.method('messages.send',
                                                      {'user_id': event.user_id, 'message': 'Функции бота: ',
                                                       'keyboard': menu_kb(), 'random_id': 0})
                                else:
                                    if msg.lower() != 'википедия':
                                        x = wikipedia.page(msg)
                                        y = x.url
                                        vk_session.method('messages.send',
                                                          {'user_id': event.user_id, 'message': f'{x.content[:300]}...',
                                                           'keyboard': wiki_msg(y), 'random_id': 0})
                            if users[event.user_id]["act"] == "games":
                                if msg.lower() == "назад":
                                    users[event.user_id]["act"] = "menu"
                                    vk_session.method('messages.send',
                                                      {'user_id': event.user_id, 'message': 'Функции бота: ',
                                                       'keyboard': menu_kb(), 'random_id': 0})
                                elif msg.lower() == "города":
                                    pass
                    save = open('users.txt', mode='w', encoding='utf-8').write(str(users))
        except ReadTimeout:
            break
