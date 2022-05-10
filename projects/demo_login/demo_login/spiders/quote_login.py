import scrapy


class QuoteLoginSpider(scrapy.Spider):
    name = 'quote_login'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        pass
