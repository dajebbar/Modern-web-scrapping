import scrapy


class EliteSpider(scrapy.Spider):
    name = 'elite'
    allowed_domains = ['hidemy.name']
    start_urls = ['http://hidemy.name/']

    def parse(self, response):
        pass
