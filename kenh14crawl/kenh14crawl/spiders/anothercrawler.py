import scrapy
import re
from bs4 import BeautifulSoup
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# Another link crawler

class AnothercrawlerSpider_2021(CrawlSpider):
    name = 'anothercrawler_2021'
    allowed_domains = ['kenh14.vn']

#     with open('/content/kenh14_beta_links.txt', 'r') as f:
#         start_urls = f.read().split("\n")
#         start_urls.pop()
#         start_urls = list(set(start_urls))
    start_urls = ['https://kenh14.vn/hot-kim-jong-kook-se-xuat-hien-tai-running-man-viet-lam-nguoi-truy-duoi-dan-cast-tai-han-quoc-20211114220622497.chn']

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

    start_urls=['https://kenh14.vn/cac-idol-tiet-lo-cong-ty-cua-ho-quy-dinh-nhu-the-nao-ve-chuyen-hen-ho-cua-ga-nha-20190102165633746.chn']
        
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

    
    
