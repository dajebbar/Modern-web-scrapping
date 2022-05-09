import scrapy
import json


class QuotesApiSpider(scrapy.Spider):
    name = 'quotes_api'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/api/quotes']

    def parse(self, response):
        resp = json.loads(response.body)
        quotes = resp.get('quotes')
        print(quotes)
        # print(response.body)
