from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader


class Hotel(Item):
    name = Field()
    price = Field()
    desc = Field()


def parse_hotel(response):
    sel = Selector(response)
    item = ItemLoader(Hotel(), sel)

    item.add_xpath('name', "//h1[@id='HEADING']/text()")

    price = "//div[contains(@class, 'bookableOffer')][1]/@data-pernight"
    if sel.xpath(price):
        item.add_xpath('price', price)
    else:
        item.add_xpath('price', "//a[contains(@class, 'bookableOffer')][1]/@data-pernight")

    desc = "//div[contains(@data-ssrev-handlers, 'Description')]//p[1]"
    if sel.xpath(desc):
        item.add_xpath('desc', desc + "/text()")
    else:
        item.add_xpath('desc', "//div[contains(@data-ssrev-handlers, 'Description')]/div/div[1]/text()")

    yield item.load_item()


class TripAdvisor(CrawlSpider):
    name = 'XatakaSpider'
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/80.0.3987.149 Safari/537.36 "
    }
    start_urls = ['https://www.tripadvisor.es/Hotels-g187514-Madrid-Hotels.html']
    download_delay = 2
    rules = (Rule(LinkExtractor(allow=r'/Hotel_Review-', restrict_xpaths="//div[contains(@class, 'listing_title')]"),
                  follow=True, callback="parseHotel"),)
