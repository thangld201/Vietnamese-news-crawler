import scrapy
import re
from bs4 import BeautifulSoup
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AnothercrawlerSpider(CrawlSpider):
    name = 'anothercrawler_2021'
    allowed_domains = ['kenh14.vn']

    with open('/content/kenh14_beta_links.txt', 'r') as f:
        start_urls = f.read().split("\n")
        start_urls.pop()
        start_urls = list(set(start_urls))

    base_urls = 'http://kenh14.vn/'

    rules = [Rule(LinkExtractor(allow=['.chn','-2021']),
                      callback='parse_link_kenh14', follow=True)]

    def parse_link_kenh14(self, response, **kwargs):
        item = Kenh14Link()
        try:
            item['link'] = response.url
        except:
            item['link'] = None
        return item


class AnothercrawlerSpider_2020(CrawlSpider):
    name = 'anothercrawler_2020'
    allowed_domains = ['kenh14.vn']

    start_urls=['https://kenh14.vn/heechul-tiet-lo-ly-do-do-800-trieu-vao-game-thay-vi-mua-dong-ho-hieu-nghe-tuong-vo-ly-nhung-lai-rat-thuyet-phuc-20200101180458723.chn']
        
    base_urls = 'http://kenh14.vn/'

    rules = [Rule(LinkExtractor(allow=['.chn','-2020']),
                      callback='parse_link_kenh14', follow=True)]

    def parse_link_kenh14(self, response, **kwargs):
        item = Kenh14Link()
        try:
            item['link'] = response.url
        except:
            item['link'] = None
        return item


class AnothercrawlerSpider_2019(CrawlSpider):
    name = 'anothercrawler_2019'
    allowed_domains = ['kenh14.vn']

    start_urls=['https://kenh14.vn/clip-660-giay-diem-lai-het-nhung-su-kien-noi-bat-nhat-nam-2019-20191223233829707.chn']
        
    base_urls = 'http://kenh14.vn/'

    rules = [Rule(LinkExtractor(allow=['.chn','-2019']),
                      callback='parse_link_kenh14', follow=True)]

    def parse_link_kenh14(self, response, **kwargs):
        item = Kenh14Link()
        try:
            item['link'] = response.url
        except:
            item['link'] = None
        return item

class Kenh14Link(scrapy.Item):
    link = scrapy.Field()

    
    