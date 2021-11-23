# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Kenh14CrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Kenh14Item(scrapy.Item):
    news_id = scrapy.Field()
    topic = scrapy.Field()
    subtopic = scrapy.Field()
    title = scrapy.Field()
    sapo = scrapy.Field()
    news_content = scrapy.Field()
    url = scrapy.Field()
    
class Kenh14Link(scrapy.Item):
    link = scrapy.Field()
