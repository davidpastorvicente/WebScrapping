from scrapy.item import Field, Item
from scrapy.spiders import Spider
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup


class News(Item):
    title = Field()
    desc = Field()


class Xataka(Spider):
    name = 'XatakaSpider'
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/80.0.3987.149 Safari/537.36"
    }
    start_urls = ['https://www.xataka.com']

    def parse(self, response):
        soup = BeautifulSoup(response.body)
        news = soup.find_all('article', class_='recent-abstract')

        for new in news:
            item = ItemLoader(News(), response.body)
            item.add_value('title', new.find('h2').text)
            item.add_value('desc', new.find('p').text)
            yield item.load_item()
