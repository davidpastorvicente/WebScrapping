from scrapy.item import Field, Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

class News(Item):
    title = Field()
    desc = Field()

class Xataka(Spider):
    name = 'XatakaSpider'
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    start_urls = ['https://www.xataka.com']

    def parse(self, response):
        sel = Selector(response)
        print(sel)
        news = sel.xpath("//article[contains(@class, 'recent-abstract')]")
        print(news)
        for new in news:
            item = ItemLoader(News(), new)
            item.add_xpath('title', ".//h2/a/text()")
            item.add_xpath('desc', ".//p/text()")
            yield item.load_item()

