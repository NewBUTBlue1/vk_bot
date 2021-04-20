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
                "color": "primary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Назад"
                },
                "color": "negative"
            }, ]
        ]
    }
    keyboard = str(json.dumps(keyboard, ensure_ascii=False).encode('utf-8').decode('utf-8'))
    return keyboard
