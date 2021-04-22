import requests


def get_photo(ll1, ll2):
    with open("../data/img/image.png", "wb") as file:
        resp = requests.get(
            f"https://static-maps.yandex.ru/1.x/?ll={ll1},{ll2}&spn=0"
            f".016457,0.00619&l=map")
        file.write(resp.content)
