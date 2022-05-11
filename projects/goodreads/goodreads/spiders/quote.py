import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['www.goodreads.com']
    start_urls = ['https://www.goodreads.com/']

    def parse(self, response):
        pass
