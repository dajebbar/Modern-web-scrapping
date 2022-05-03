import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.cigabuy.com']
    start_urls = ['http://www.cigabuy.com/']

    def parse(self, response):
        pass
