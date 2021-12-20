import scrapy
import re
from bs4 import BeautifulSoup


class SohaLinkcrawlerSpider_2021(scrapy.Spider):
    name = 'soha_linkcrawler_2021'
    allowed_domains = ['soha.vn']

    start_urls = ['https://soha.vn/nha-vo-dich-aff-cup-gap-viet-nam-o-ban-ket-co-khi-thai-lan-ho-con-thay-mung-20211219210123388.htm']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def parse_link(self, response):
        item = Kenh14Link()
        try:
            item['link'] = response.url
        except:
            item['link'] = None
        return item

    def parse(self, response,**kwargs):
        response_content = response.body
        soup = BeautifulSoup(response_content,"html.parser")
        
        links = re.findall("data-popup-url=\"\/([\w\d-]*.htm)", str(response_content))
        links = set(links)

        item = Kenh14Link()
        item['link'] = response.url
        yield item

        for link in links:
            full_link = link
            if not link.startswith('https:/'):
                full_link = "https://soha.vn/" + link
            if "-2021" in full_link:
                yield scrapy.Request(full_link,callback=self.parse)


class SohaLinkcrawlerSpider_2020(scrapy.Spider):
    name = 'soha_linkcrawler_2020'
    allowed_domains = ['soha.vn']

    start_urls = ['https://soha.vn/ten-lua-elbrus-lien-xo-danh-bai-he-thong-phong-thu-toi-tan-nhat-cua-my-20200110090925033.htm']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
            
    def parse_link(self, response):
        item = Kenh14Link()
        try:
            item['link'] = response.url
        except:
            item['link'] = None
        return item
    
    def parse(self, response,**kwargs):
        response_content = response.body
        soup = BeautifulSoup(response_content,"html.parser")
        
        links = re.findall("data-popup-url=\"\/([\w\d-]*.htm)", str(response_content))
        links = set(links)

        item = Kenh14Link()
        item['link'] = response.url
        yield item
        
        for link in links:
            full_link = link
            if not link.startswith('https:/'):
                full_link = "https://soha.vn/" + link
            yield scrapy.Request(full_link,callback=self.parse)


class SohaLinkcrawlerSpider_2019(scrapy.Spider):
    name = 'soha_linkcrawler_2019'
    allowed_domains = ['soha.vn']

    start_urls = ['https://soha.vn/nghe-thuat-phat-con-vo-cung-hieu-qua-ma-khong-lam-ton-thuong-den-long-tu-trong-cua-tre-cha-me-rat-nen-thuoc-nam-long-20190107113332307.htm']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
            
    def parse_link(self, response):
        item = Kenh14Link()
        try:
            item['link'] = response.url
        except:
            item['link'] = None
        return item
    
    def parse(self, response,**kwargs):
        response_content = response.body
        soup = BeautifulSoup(response_content,"html.parser")
        
        links = re.findall("data-popup-url=\"\/([\w\d-]*.htm)", str(response_content))
        links = set(links)

        item = Kenh14Link()
        item['link'] = response.url
        yield item
        
        for link in links:
            full_link = link
            if not link.startswith('https:/'):
                full_link = "https://soha.vn/" + link
            yield scrapy.Request(full_link,callback=self.parse)


class Kenh14Link(scrapy.Item):
    link = scrapy.Field()
