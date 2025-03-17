from itertools import product

import requests
from bs4 import BeautifulSoup

URL = r"https://www.citilink.ru/catalog/smartfony/?ref=mainmenu_plate"

HEADERS = {
    "User-agent": "Mozila/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "ru-RU, ru, q=0.9"
}
try:
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser") #pars HTML
    products = soup.find_all("div", class_="app-catalog-qzffme-Layout--StyledLayout ev46q5b0")
    if not products:
        print("qwerty")
except requests.exceptions.RequestException as rex:
    print(f"ошибка при запросе: {rex}")
except AttributeError:
    print("Некоторые элементы не найдены!")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser") #pars HTML
    products = soup.find_all("div", class_="app-catalog-qzffme-Layout--StyledLayout ev46q5b0")

    for product in products:
        title = product.find("a", class_="app-catalog-1g0fl7h-Anchor--Anchor-Anchor--StyledAnchor ejir1360").text.strip()
        link = "https://www.dns-shop.ru" + product.find("a", class_="product-title")["href"]

        print(f"{title} - {price}")
        print(f"Ссылка: {link}\n")
else:
    print("Ошибка загрузки страницы!")


