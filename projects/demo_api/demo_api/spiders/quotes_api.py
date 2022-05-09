import scrapy


class QuotesApiSpider(scrapy.Spider):
    name = 'quotes_api'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/api/quotes']

    def parse(self, response):
        pass
