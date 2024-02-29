from selenium import webdriver

URL_DIGITAL_OCEAN = "https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html"
URL_YANDEX_ACADEMI = "https://academy.yandex.ru/handbook/python/article/modul-requests"
URL_WIKI = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"



def get_html(url):
    try:
        driver = webdriver.Chrome
        driver.get(url)
        html = driver.page_source
        return html
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def main():
    while True:
        html = get_html(URL_DIGITAL_OCEAN)
        print(html)
        break

if __name__ == '__main__':
    main()