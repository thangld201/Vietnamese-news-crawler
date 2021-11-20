import scrapy
from bs4 import BeautifulSoup

class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    root_site = "https://kenh14.vn/"
    allowed_domains = 'kenh14.vn'
    with open('/content/kenh14_beta_links.txt', 'r') as f:
        start_urls = f.read().split("\n")
        start_urls.pop()
        start_urls = list(set(start_urls))
        
    def parse(self, response,**kwargs):

        news_id = response.url[-21:-4]
        response_content = response.content
        soup = BeautifulSoup(response_content,"html.parser")

        try:
            topic = soup.find("ul",{'class':'kbws-list fl'}).find_all('a')[0].text
        except:
            topic=None
        try:
            subtopic = soup.find("li", {"class":"kbwsli active"}).find('a').text
        except:
            subtopic=None   
        try:
            sapo = soup.find("h2",{'class':'knc-sapo'}).text.strip()
        except:
            sapo=None   
        try:
            news_content = ' '.join(response.xpath('//*[@id="k14-detail-content"]/div[2]/div/div/div[1]/div[2]/div[6]/p//text()'))
        except:
            news_content=None   
        try:      
            title = soup.find("h1",{'class':'kbwc-title'}).text.strip()
        except:
            title=None
            
        item = Kenh14Item()
        item['news_id'] = news_id
        item['topic'] = topic
        item['subtopic'] = subtopic
        item['title'] = title
        item['sapo'] = sapo
        item['content'] = news_content.strip()
        item['url'] = response.url


class Kenh14Item(scrapy.Item):
    news_id = scrapy.Field()
    topic = scrapy.Field()
    subtopic = scrapy.Field()
    title = scrapy.Field()
    sapo = scrapy.Field()
    news_content = scrapy.Field()
    url = scrapy.Field()


















