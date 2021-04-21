def get_text(url):
    import requests, bs4
    r = requests.get(url)
    BS = bs4.BeautifulSoup(r.text, "lxml")
    y = BS.find_all("p")[0].text
    return y


def get_p(url):
    import requests, bs4
    r = requests.get(url)
    BS = bs4.BeautifulSoup(r.text, "lxml")
    y = BS.find_all("li")[0].text
    return y