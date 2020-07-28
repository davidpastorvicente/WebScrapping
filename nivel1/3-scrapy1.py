from scrapy.item import Field, Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

class Question(Item):
    id = Field()
    title = Field()
    #desc = Field()

class StackOverflow(Spider):
    name = "StackQuestions"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    start_urls = ['https://www.stackoverflow.com/questions']

    def parse(self, response):
        sel = Selector(response)
        quests = sel.xpath("//div[@class='question-summary']")
        id = 0
        for quest in quests:
            item = ItemLoader(Question(), quest)
            item.add_value('id', id)
            item.add_xpath('title', './/h3/a/text()')
            #item.add_xpath('desc', './/div[@class="excerpt"]/text()')
            id += 1
            yield item.load_item()