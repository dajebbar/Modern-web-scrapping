import scrapy


class IncreaseViewSpider(scrapy.Spider):
    name = 'increase_view'
    allowed_domains = ['free-proxy-list.net']
    start_urls = ['http://free-proxy-list.net/']

    def parse(self, response):
        pass
