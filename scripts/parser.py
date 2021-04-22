def get_product(url):
    import requests, bs4
    r = requests.get(url)
    BS = bs4.BeautifulSoup(r.text, "lxml")
    return BS.find('div', {"class": "mnr-c.pla-unit"})