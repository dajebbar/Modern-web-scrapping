import scrapy


class MeterSpider(scrapy.Spider):
    name = 'meter'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/']

    def parse(self, response):
        pass
