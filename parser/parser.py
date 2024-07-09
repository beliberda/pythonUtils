from selenium import webdriver
from LxmlSoup import LxmlSoup
import requests



URL_DIGITAL_OCEAN = "https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html"
URL_YANDEX_ACADEMI = "https://academy.yandex.ru/handbook/python/article/modul-requests"
URL_WIKI = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

# получаем html в виде текста
html = requests.get(URL_DIGITAL_OCEAN).text
# Далее создаём экземпляр объекта LxmlSoup в который передаём переменную html. 
# Это нужно, так как LxmlSoup является классом хранящим в себе нужные нам методы для извлечения информации из html кода.
soup = LxmlSoup(html)
title = soup.find_all('p', class_="verse")

print(title[0])


# def get_html(url):
#     try:
#         driver = webdriver.Chrome
#         driver.get(url)
#         html = driver.page_source
#         return html
#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()

# def main():
#     while True:
#         html = get_html(URL_DIGITAL_OCEAN)
#         print(html)
#         break

# if __name__ == '__main__':
#     main()