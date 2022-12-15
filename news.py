import requests
from bs4 import BeautifulSoup

def check_news():
    base = "https://rg.ru/tema/ekonomika"
    html = requests.get(base).text
    soup = BeautifulSoup(html, "lxml")
    div = soup.findAll("div","PageRubricContent_listItem__rjCcF")
    href = soup.find("div","PageRubricContent_listItem__rjCcF").find("a").get("href")


    list_news = []
    href_list = []
    look_news_list = []
    test = []

    for news in div:
        list_news.append(news.text)


    for link in div:
        href_list.append("rg.ru" + link.find("a").get("href"))


    for i in range(5):
        look_news_list.append("\n")
        look_news_list.append(list_news[i])
        look_news_list.append("\n")
        look_news_list.append(href_list[i])

    test = " ".join(str(x)for x in look_news_list)
                                
    return test 


#print(check_news())

    

#text = [print(i) for i in check_news()]


    



    



#print(div)







