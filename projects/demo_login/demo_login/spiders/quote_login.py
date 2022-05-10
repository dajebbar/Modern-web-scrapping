import scrapy
from scrapy import FormRequest


class QuoteLoginSpider(scrapy.Spider):
    name = 'quote_login'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/login']

    def parse(self, response):
        csrf_token = response.xpath("//input[@name='csrf_token']/@value").get()
        yield FormRequest.from_response(
            response,
            formxpath="//form",
            formdata={
                'csrf_token': csrf_token,
                'user': 'admin',
                'password': 'admin',
            },
            callback=self.after_login,
        )
    
    def after_login(self, response):
        if response.xpath("//a[@href='/logout']/text()").get():
            print('Logged In')
