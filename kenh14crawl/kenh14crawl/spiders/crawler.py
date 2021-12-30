import scrapy
from bs4 import BeautifulSoup
from datetime import datetime
import pandas

# Content crawler
class CrawlerSpider(scrapy.Spider):

    name = 'kenh14_content_crawler'
    root_site = "https://kenh14.vn/"
    allowed_domains = 'kenh14.vn'
    # custom_settings = {'CLOSESPIDER_PAGECOUNT': 5}
    
    # Puts the source links in the correct folder !
    all_df = pandas.read_csv('./12_9_kenh14.csv')
    start_urls = all_df.link.tolist()
#     start_urls = ['https://kenh14.vn/hot-kim-jong-kook-se-xuat-hien-tai-running-man-viet-lam-nguoi-truy-duoi-dan-cast-tai-han-quoc-20211114220622497.chn']
#
    def parse(self, response,**kwargs):

        response_content = response.body
        soup = BeautifulSoup(response_content,"html.parser")

        try:
            news_id = response.url[-21:-4]
        except:
            news_id = None
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
            news_content = ' '.join(response.xpath('//*[@id="k14-detail-content"]/div[2]/div/div/div[1]/div[2]/div[6]/p//text()').getall()).strip()
        except:
            news_content=None   
        try:      
            title = soup.find("h1",{'class':'kbwc-title'}).text.strip()
        except:
            title=None
        try:
            news_time = soup.find("span",{'class':'kbwcm-time'}).text
            news_time = datetime.strptime(news_time,"%H:%M %d/%m/%Y")
        except:
            news_time=None
        try:
            news_author=soup.find("span",{'class':'kbwcm-author'}).text
        except:
            news_author=None
        try:
            news_source=soup.find("span",{'class':'kbwcm-source'}).text
        except:
            news_source=None


        item = Kenh14Item()
        item['news_id'] = news_id
        item['topic'] = topic
        item['subtopic'] = subtopic
        item['title'] = title
        item['sapo'] = sapo
        item['news_content'] = news_content
        item['news_time'] = news_time
        item['news_author'] = news_author
        item['news_source'] = news_source
        item['homepage'] = 'kenh14'
        item['url'] = response.url
        return item

class SoHaCrawlerSpider(scrapy.Spider):

    name = 'soha_content_crawler'
    allowed_domains = 'soha.vn'
    # custom_settings = {'CLOSESPIDER_PAGECOUNT': 5}
    
    # Puts the source links in the correct folder !
#     all_df = pandas.read_csv('./12_9_kenh14.csv')
#     start_urls = all_df.link.tolist()
    start_urls = ['https://soha.vn/nhat-ban-co-thu-tuong-moi-chim-bo-cau-diem-dam-bien-ac-mong-cua-trung-quoc-thanh-hien-thuc-2021092918581706.htm',
                  'https://soha.vn/nhat-ban-co-thu-tuong-moi-chim-bo-cau-diem-dam-bien-ac-mong-cua-trung-quoc-thanh-hien-thuc-2021092918581706.htm',
                  'https://soha.vn/nhat-ban-co-thu-tuong-moi-chim-bo-cau-diem-dam-bien-ac-mong-cua-trung-quoc-thanh-hien-thuc-2021092918581706.htm',
                ]
        
    def parse(self, response,**kwargs):

        response_content = response.body
        soup = BeautifulSoup(response_content,"html.parser")

        try:
            news_id=response.url[-21:-4]
        except:
            news_id=None
        try:
            topic=soup.find("nav",{'id':'sohaSubCategories'}).find_all('a')[0].text
        except:
            topic=None
        try:
            subtopic=soup.find("nav",{'id':'sohaSubCategories'}).find('a').text
        except:
            subtopic=None
        try:
            title=soup.find("h1",{'class':'news-title'}).text.strip()
        except:
            title=None
        try:
            sapo=soup.find("h2",{'class':'news-sapo'}).text.strip()
        except:
            sapo=None
        try:
            contents = []
            for tmp_tag in soup.find("div",{'class':'clearfix news-content'}).find_all('p'):
                if not tmp_tag.find('a') and not tmp_tag.find('p',{'class':""}) and not tmp_tag.has_attr('data-placeholder'):
                    tmp_tmp_text = tmp_tag.text.strip()
                    if tmp_tmp_text[-1]!='.':
                        contents.append(tmp_tmp_text+".")
                    else:
                        contents.append(tmp_tmp_text)
            news_content=' '.join(contents)
        except:
            news_content=None
        try:
            news_time=datetime.strptime(soup.find("time",{'class':'op-published'}).text,"%d/%m/%Y %H:%M")
        except:
            news_time=None
        try:
            news_author=soup.find("div",{'class':'news-info'}).find("b",{'data-field':"author"}).text.strip()
        except:
            news_author=None
        try:
            if soup.find("p",{'class':'bottom-info'}):
                news_source=soup.find("p",{'class':'bottom-info'}).text.strip()
            else:
                news_source=soup.find("div",{'class':'bottom-info clearfix'}).find("span",{'class':"link-source-text-name"}).text.strip()    
        except:
            news_source=None


        item = Kenh14Item()
        item['news_id'] = news_id
        item['topic'] = topic
        item['subtopic'] = subtopic
        item['title'] = title
        item['sapo'] = sapo
        item['news_content'] = news_content
        item['news_time'] = news_time
        item['news_author'] = news_author
        item['news_source'] = news_source
        item['homepage'] = 'soha'
        item['url'] = response.url
        return item


class Kenh14Item(scrapy.Item):
    news_id = scrapy.Field()
    topic = scrapy.Field()
    subtopic = scrapy.Field()
    title = scrapy.Field()
    sapo = scrapy.Field()
    news_content = scrapy.Field()
    news_time = scrapy.Field()
    news_author = scrapy.Field()
    news_source = scrapy.Field()
    homepage = scrapy.Field()
    url = scrapy.Field()  