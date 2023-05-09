import requests
from bs4 import BeautifulSoup

pressesListHtml = requests.get("https://media.naver.com/press")
pressesListSoup = BeautifulSoup(pressesListHtml.content, "html.parser")

li = pressesListSoup.select("ul.Nlnb_menu_sublist li a")

# {'officeCode': 'officeName', '001': '연합뉴스'}
presses = dict()
categories = dict({'100':'정치','101':'경제', '102':'사회','103':'생활','104':'세계','105':'IT'})

for item in pressesListSoup.select("ul.press_list_only_logo li a"):
    pressName = item.select_one("img").attrs["alt"]
    pressCode = item.get_attribute_list("data-office-id")[0]

    presses[pressCode] = pressName

# 언론사 코드별로 정렬
presses = dict(sorted(presses.items()))

for i in presses:
    print("{} : {}".format(i,presses[i]))


pressKey = list(presses.keys())[0]
pressNewsListHtml = requests.get("https://media.naver.com/press/{}?sid={}".format(pressKey,'100'))
pressNewsListSoup = BeautifulSoup(pressNewsListHtml.content, "html.parser")

aList = pressNewsListSoup.select("ul.press_edit_news_list li a.press_edit_news_link")

def getLink(obj):
    return obj.get_attribute_list("href")[0]

links = list(map(getLink, aList))

for link in links:
    print(link)