from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader


class Article(Item):
    name = Field()
    price = Field()
    desc = Field()


class Amazon(CrawlSpider):
    name = "Amazon Laptops"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/80.0.3987.149 Safari/537.36",
        "CLOSESPIDER_PAGECOUNT": 20
    }
    download_delay = 1
    allowed_domains = ['amazon.es']
    start_urls = ["https://www.amazon.es/s?k=adaptador+usb+c"]
    rules = (
        Rule(LinkExtractor(allow=r'&page='), follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@data-component-type='s-search-result']//h2"),
             follow=True, callback='parseArticle')
    )

    def cleanText(self, txt):
        return txt.replace('\n', '').replace('\r', '').replace('\t', '').replace('\xa0', ' ').strip()

    def parseArticle(self, response):
        item = ItemLoader(Article(), response)
        item.add_xpath('name', "//span[@id='productTitle']/text()", MapCompose(self.cleanText))
        item.add_xpath('price', "//span[@id='price_inside_buybox']/text()", MapCompose(self.cleanText))
        item.add_xpath('desc', "//div[@id='productDescription']/p/text()", MapCompose(self.cleanText))
        yield item.load_item()
