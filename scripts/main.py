import requests
import wikipedia
from data.keyboards.scr import *
import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
from requests.exceptions import ReadTimeout
from scripts.table import data
from random import choice
from scripts.map_method import get_photo

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
                            users[event.user_id] = {'act': 'menu', 'ct': '', 'ct_used': []}
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
                                            users[event.user_id]["act"] = "maps_send"
                            if users[event.user_id]["act"] == "maps_send":
                                if msg.lower() != "назад":
                                    if msg.lower() != "фрагмент карты по ее координатам":
                                        try:
                                            ll1 = str(msg).split()[0]
                                            ll2 = str(msg).split()[1]
                                            if 2 < len(ll1) < 9:
                                                if 2 < len(ll2) < 9:
                                                    ll2 += '0' * (9 - len(ll2))
                                                elif len(ll2) <= 2:
                                                    ll2 += '.000000'
                                                ll1 += '0' * (9 - len(ll1))
                                            elif len(ll1) <= 2:
                                                if 2 < len(ll2) < 9:
                                                    ll2 += '0' * (9 - len(ll2))
                                                elif len(ll2) <= 2:
                                                    ll2 += '.000000'
                                                ll1 += '.000000'
                                            get_photo(ll1, ll2)
                                            a = vk_session.method("photos.getMessagesUploadServer")
                                            b = requests.post(a['upload_url'],
                                                              files={
                                                                  'photo': open('../data/img/image.png', 'rb')}).json()
                                            c = vk_session.method('photos.saveMessagesPhoto',
                                                                  {'photo': b['photo'], 'server': b['server'],
                                                                   'hash': b['hash']})[
                                                0]
                                            d = "photo{}_{}".format(c["owner_id"], c["id"])
                                            vk_session.method("messages.send",
                                                              {"user_id": event.user_id,
                                                               "message": "Вот твой фрагмент: ", "attachment": d,
                                                               "random_id": 0})
                                        except ValueError:
                                            users[event.user_id]["act"] = "maps"
                                            vk_session.method('messages.send',
                                                              {'user_id': event.user_id,
                                                               'message': 'Вы ввели не число. Попробуйте сначала.',
                                                               'keyboard': maps_kb(), 'random_id': 0})
                                        except vk_api.exceptions.ApiError:
                                            vk_session.method('messages.send',
                                                              {'user_id': event.user_id,
                                                               'message': 'Внутренняя ошибка',
                                                               'keyboard': maps_kb(), 'random_id': 0})
                                else:
                                    users[event.user_id]["act"] = "menu"
                                    vk_session.method('messages.send',
                                                      {'user_id': event.user_id, 'message': 'Функции бота: ',
                                                       'keyboard': menu_kb(), 'random_id': 0})
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
                                                              {'user_id': event.user_id,
                                                               'message': f'{x.content[:300]}...',
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
                                    users[event.user_id]["act"] = "goroda"
                                    users[event.user_id]["ct"] = choice(data)
                                    vk_session.method('messages.send',
                                                      {'user_id': event.user_id,
                                                       'message': f'Я начну {users[event.user_id]["ct"]}',
                                                       'keyboard': cities_kb(), 'random_id': 0})
                            elif users[event.user_id]["act"] == "goroda":
                                if msg.lower() == 'прервать игру':
                                    users[event.user_id]["ct_used"].clear()
                                    users[event.user_id]["act"] = "games"
                                    vk_session.method('messages.send',
                                                      {'user_id': event.user_id, 'message': 'Ты перешел в меню игр',
                                                       "keyboard": games_kb(), 'random_id': 0})
                                else:
                                    temp = []
                                    city, k, k1 = msg, -1, -1
                                    if users[event.user_id]['ct'][-1] in 'ъьы':
                                        k = -2
                                    if city.lower()[0] == users[event.user_id]["ct"][k] and city in data and city \
                                            not in users[event.user_id]["ct_used"]:
                                        users[event.user_id]["ct_used"].append(city)
                                        if city[-1] in 'ъьы':
                                            k1 = -2
                                        for i in data:
                                            if i.lower()[0] == city[k1]:
                                                temp.append(i)
                                        for j in temp:
                                            if j in users[event.user_id]["ct_used"]:
                                                del (temp[temp.index(j)])
                                        if temp:
                                            new_city = choice(temp)
                                            users[event.user_id]["ct_used"].append(new_city)
                                            vk_session.method('messages.send',
                                                              {'user_id': event.user_id, 'message': new_city,
                                                               "keyboard": cities_kb(), 'random_id': 0})
                                            users[event.user_id]["ct"] = new_city
                                        else:
                                            users[event.user_id]["act"] = 'games'
                                            vk_session.method('messages.send',
                                                              {'user_id': event.user_id, 'message': "Ты выиграл",
                                                               "keyboard": games_kb(), 'random_id': 0})
                                    elif city in users[event.user_id]["ct_used"]:
                                        vk_session.method('messages.send',
                                                          {'user_id': event.user_id, 'message': "Город уже был назван",
                                                           "keyboard": cities_kb(), 'random_id': 0})
                                    else:
                                        vk_session.method('messages.send',
                                                          {'user_id': event.user_id, 'message': 'Неправильное '
                                                                                                'название города',
                                                           "keyboard": cities_kb(), 'random_id': 0})
                    save = open('users.txt', mode='w', encoding='utf-8').write(str(users))
        except ReadTimeout:
            break
