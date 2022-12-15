import requests
from bs4 import BeautifulSoup

def value_rate():
    word = []
    base = "https://www.banki.ru/products/currency/"
    html = requests.get(base).text
    soup = BeautifulSoup(html, "lxml")
    div = soup.find("div",class_="cb-current-rates").findAll("tr",class_="cb-current-rates__list__item")

#Поиск значение валюты!
    table = soup.find("div",class_="cb-current-rates").find("tr",class_="cb-current-rates__list__item").find("td").find("a").getText()

#Поиск стоймости валюты!
    valuer_rate = soup.find("div",class_="cb-current-rates").find("tr",class_="cb-current-rates__list__item").findAll("td")[1].getText()

    valuer_list = []
    rate_list = []
    valuer_list_test = []

    for value in div:
        valuer_list.append(value.find("td").find("a").getText() + ":")
        valuer_list.append(value.findAll("td")[1].getText()+"\n")

    valuer_list_test = "".join(str(x)for x in valuer_list)

    return valuer_list_test

