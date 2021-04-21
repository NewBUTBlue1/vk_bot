import json


def menu_kb():
    keyboard = {
        "one_time": False,
        "buttons": [
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Википедия"
                },
                "color": "secondary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Поиск товаров"
                },
                "color": "secondary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Отправить e-mail"
                },
                "color": "secondary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Игры"
                },
                "color": "primary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Приколы с Яндекс.Картами"
                },
                "color": "secondary"
            }, ]
        ]
    }
    keyboard = str(json.dumps(keyboard, ensure_ascii=False).encode('utf-8').decode('utf-8'))
    return keyboard


def menu_wiki():
    keyboard_wiki = {
        "one_time": False,
        "buttons": [
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Назад"
                },
                "color": "negative"
            }, ]
        ]
    }
    keyboard_wiki = str(json.dumps(keyboard_wiki, ensure_ascii=False).encode('utf-8').decode('utf-8'))
    return keyboard_wiki


def wiki_msg(url1):
    keyboard_wiki_msg = {
        "one_time": False,
        "inline": True,
        "buttons": [
            [{
                "action": {
                    "type": "open_link",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Открыть ссылку",
                    "link": url1
                }
            }, ]
        ]
    }
    keyboard_wiki_msg = str(json.dumps(keyboard_wiki_msg, ensure_ascii=False).encode('utf-8').decode('utf-8'))
    return keyboard_wiki_msg


def games_kb():
    keyboard_games = {
        "one_time": False,
        "buttons": [
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Города",
                }
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Назад"
                },
                "color": "negative"
            }, ]
        ]
    }
    keyboard_games = str(json.dumps(keyboard_games, ensure_ascii=False).encode('utf-8').decode('utf-8'))
    return keyboard_games


def cities_kb():
    keyboard_city = {
        "one_time": False,
        "buttons": [
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Прервать игру"
                },
                "color": "negative"
            }, ]
        ]
    }
    keyboard_city = str(json.dumps(keyboard_city, ensure_ascii=False).encode('utf-8').decode('utf-8'))
    return keyboard_city


def maps_kb():
    keyboard_map = {
        "one_time": False,
        "buttons": [
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Фрагмент карты по ее координатам"
                },
                "color": "positive"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Назад"
                },
                "color": "negative"
            }, ]
        ]
    }
    keyboard_map = str(json.dumps(keyboard_map, ensure_ascii=False).encode('utf-8').decode('utf-8'))
    return keyboard_map


def ins_map_kb():
    keyboard_ins_map = {
        "one_time": False,
        "buttons": [
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Назад"
                },
                "color": "negative"
            }, ]
        ]
    }
    keyboard_ins_map = str(json.dumps(keyboard_ins_map, ensure_ascii=False).encode('utf-8').decode('utf-8'))
    return keyboard_ins_map
