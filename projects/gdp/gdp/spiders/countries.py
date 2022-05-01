import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/']

    def parse(self, response):
        pass
