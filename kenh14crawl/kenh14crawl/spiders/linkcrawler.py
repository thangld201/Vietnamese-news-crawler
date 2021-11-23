import scrapy
import re
from bs4 import BeautifulSoup

class LinkcrawlerSpider(scrapy.Spider):
    name = 'linkcrawler'
    allowed_domains = ['kenh14.vn']

    with open('/content/kenh14_beta_links.txt', 'r') as f:
        start_urls = f.read().split("\n")
        start_urls.pop()
        start_urls = list(set(start_urls))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
            
    def parse(self, response,**kwargs):
        response_content = response.body
        soup = BeautifulSoup(response_content,"html.parser")
        
        links = re.findall("data-popup-url=\"\/([\w\d-]*.chn)", str(response_content))
        links = set(links)

        for link in links:
            full_link = link
            if not link.startswith('https:/'):
                full_link = "https://kenh14.vn/" + link
            if self.part=="3" and ("-2021" in full_link):
                yield response.follow(full_link,callback=self.parse_link)
            elif self.part=="2" and ("-2020" in full_link):
                yield response.follow(full_link,callback=self.parse_link)
            elif ("-2019" in full_link):
                yield response.follow(full_link,callback=self.parse_link)
    
    def parse_link(self, response):
        item = Kenh14Link()
        try:
            item['link'] = response.url
        except:
            item['link'] = None
        return item


class Kenh14Link(scrapy.Item):
    link = scrapy.Field()