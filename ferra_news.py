
    print(articles)
    return articles

textart={}
def get_text_from_news(articles):
    for i in articles:
        n=articles.get(i).get("link")
        _browser.get(n)
        _title = _browser.find_element(By.CSS_SELECTOR, "#article_0 > article > div:nth-child(1) > div > div > div.jsx-2881489884.gbWBYuE8 > div > div:nth-child(1) > div.jsx-2997808805.VmIH81oF > div.jsx-2848471422.xrTCCraw > h1").text.strip()
        _subbody =_browser.find_element(By.CSS_SELECTOR, "#article_0 > article > div:nth-child(1) > div > div > div.jsx-2881489884.gbWBYuE8 > div > div:nth-child(1) > div.jsx-2997808805.VmIH81oF > div.jsx-2848471422.xrTCCraw > div").text.strip()
        _body=_browser.find_element(By.CSS_SELECTOR, "#article_0 > article > div:nth-child(1) > div > div > div.jsx-2881489884.gbWBYuE8 > div > div.jsx-1306788247 > div.jsx-3697113030.vikont > div > div").text.strip()
        _source = _browser.find_element(By.CSS_SELECTOR, "#article_0 > article > div:nth-child(1) > div > div > div.jsx-2881489884.gbWBYuE8 > div > div:nth-child(4) > div.jsx-2997808805.VmIH81oF > div:nth-child(2) > div.jsx-3984155050.Fvm5s7tb > div > div:nth-child(1) > a")
        _s = _source.get_attribute('href')
        _image = _browser.find_element(By.CLASS_NAME, "sX8xPdQU")
        _img = _image.get_attribute('src')

        textart.update({_title: {"fact": _subbody, "text":_body, "source":_s, "image":_img }})

    print(textart)
    return textart
        # return i


if __name__ == '__main__':
    articles_list = get_news_list_ferra()
    get_text_from_news(articles_list)
