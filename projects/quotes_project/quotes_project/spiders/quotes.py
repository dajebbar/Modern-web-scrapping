from ast import arg
import scrapy
from scrapy_splash import SplashRequest


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    # start_urls = ['http://quotes.toscrape.com/']

    script = '''
            '''
    
    def start_requests(self):
        yield SplashRequest(
            url='http://quotes.toscrape.com/',
            callback=self.parse,
            endpoint='execute',
            args={
                'lua_source': self.script,
            }
        )

    def parse(self, response):
        for quote in response.xpath(""):
            yield {
                'text': quote.xpath("").get(),
                'author': quote.xpath("").get(),
                'tags': quote.xpath("").get(),
            }
        
        next_page = response.xpath("").get()
        if next_page:
            yield scrapy.Request(
                url=next_page,
                callback=self.parse,
            )
