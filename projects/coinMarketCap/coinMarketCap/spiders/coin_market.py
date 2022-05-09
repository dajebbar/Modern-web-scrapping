import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CoinMarketSpider(CrawlSpider):
    name = 'coin_market'
    allowed_domains = ['coinmarketcap.com']
    start_urls = ['https://coinmarketcap.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='sc-16r8icm-0 escjiH']/a[@class='cmc-link']"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield {
            'name': response.xpath("//h2[@class='sc-1q9q90x-0 jCInrl h1']/text()").get(),
            'price': response.xpath("//div[@class='priceValue ']/span/text()").get(),
        }
