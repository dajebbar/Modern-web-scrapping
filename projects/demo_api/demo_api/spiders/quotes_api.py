import scrapy


class QuotesApiSpider(scrapy.Spider):
    name = 'quotes_api'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        pass
