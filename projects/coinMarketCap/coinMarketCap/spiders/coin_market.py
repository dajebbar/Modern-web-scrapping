import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_cloudflare_middleware.middlewares import CloudFlareMiddleware

class CoinMarketSpider(CrawlSpider):
    name = 'coin_market'
    allowed_domains = ['coinmarketcap.com']
    # start_urls = ['https://coinmarketcap.com/']
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
    
    def start_requests(self):
        yield scrapy.Request(
            url='https://coinmarketcap.com/',
            callback=self.parse,
            headers={
                'User-Agent': self.user_agent,
            })
    
    rules = (
        Rule(LinkExtractor(
            restrict_xpaths="//div[@class='sc-16r8icm-0 escjiH']/a[@class='cmc-link']"), 
            callback='parse_item', 
            follow=True,
            process_request='set_user_agent',
        ),
    )

    def set_user_agent(self, request, response):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            'name': response.xpath("//h2[@class='sc-1q9q90x-0 jCInrl h1']/text()").get(),
            'price': response.xpath("//div[@class='priceValue ']/span/text()").get(),
            'rank': response.xpath("//div[@class='namePill namePillPrimary']/text()").get(),
        }
