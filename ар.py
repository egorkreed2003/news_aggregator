from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime

now = datetime.now()
year = now.year
month = now.month
day = now.day

_browser = webdriver.Chrome()
_browser.implicitly_wait(5)

def get_news_list_telecomdaily():
    _url_snils = f"https://www.telecomdaily.ru/rubric/science"
    _browser.get(_url_snils)

    divs = _browser.find_elements(By.CLASS_NAME, 'news-teaser-h03b-wrapper')

    articles = {}
    for d in divs:
        try:
            a = d.find_element(By.TAG_NAME, 'a')
            _links = a.get_attribute('href')
            _title = d.find_element(By.CLASS_NAME, "annotation").text.strip()
            _date = d.find_element(By.CLASS_NAME, "created-at").text.strip()
            _category = d.find_element(By.CLASS_NAME, "rubrics").text.strip()
            if not _title:
                break
            articles.update({_title: {"date": _date, "link": _links, "category": _category}})
        except:
            pass

    print(articles)
    return articles



textart={}

def get_text_from_news(articles):
    for i in articles:
        n=articles.get(i).get("link")
        _browser.get(n)
        _title = _browser.find_element(By.CLASS_NAME, "title").text.strip()
        _source = _browser.find_element(By.CLASS_NAME, "first")
        _s = _source.get_attribute('href')
        _image = _browser.find_element(By.CLASS_NAME, "img-fluid")
        _img = _image.get_attribute('src')
        _body = _browser.find_element(By.CLASS_NAME, "content").text.strip()

        textart.update({_title: {"title": _title, "body":_body, "source":_s, "image":_img }})

    print(textart)
    return textart


if __name__ == '__main__':
    articles_list = get_news_list_telecomdaily()
    get_text_from_news(articles_list)