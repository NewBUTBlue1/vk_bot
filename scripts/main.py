import smtplib
from data.keyboards.scr import menu_kb
import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
from bs4 import BeautifulSoup
import requests

token = "b192ac9e1f0ae17eee1dd0b74264e17c6ffb4bbfd4a1a684ab428f6b5d7d11208281a1e5214169db1088e"
vk_session = vk_api.VkApi(token=token)
s_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            msg = event.text.lower()
            if event.from_user and not event.from_me:
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Функции бота: ', 'keyboard': menu_kb(), 'random_id': 0})
