import requests
from bs4 import BeautifulSoup

def get_exchage_money():
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
    new_list = []

    for value in div:
        valuer_list.append(value.find("td").find("a").getText())
        rate_list.append(value.findAll("td")[1].getText())

    for i in range(len(rate_list)):
        rate_list[i] = float(rate_list[i].replace(",", "."))

    valuer_list.append("RUB")
    rate_list.append("1.0")

    new_list = dict(zip(valuer_list,rate_list))

    return new_list
 
#get_money = get_exchage_money()

def calcul_money(get_money,value_1,value_2,sum_money):

    calcul_m = (float(get_money[value_1])/float(get_money[value_2]))*sum_money

    calcul_m = round(calcul_m,2)

    return (str(calcul_m))


#print(calcul_money(get_money,"EUR","USD",1000))



#print(calcul_money(money,message))
        
#em()
