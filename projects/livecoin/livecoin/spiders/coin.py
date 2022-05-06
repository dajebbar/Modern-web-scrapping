import scrapy
from scrapy_splash import SplashRequest

class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['www.livecoin.net/en']
    # start_urls = ['http://www.livecoin.net/']

    script = '''
                function main(splash, args)
                splash.private_mode_enable: false
                
                url = args.url
                assert(splash:go(url))
                assert(splash:wait(1))
                
                rur_tab = assert(splash:select_all(".filterPanelItem__2z5Gb"))
                rur_tab[5] = mouse_click()
                assert(splash:wait(1))
                splash:set_viewport_full()
                return {
                    html = splash:html(),
                    png = splash:png(),
                }
                end
            '''
    def start_requests(self):
        yield SplashRequest(
            url='http://www.livecoin.net/en',
            callback=self.parse,
            endpoint='execute',
            args={
                'lua_source': self.script,
            }
        ) 

    def parse(self, response):
    #    print(response.body)
        for currency in response.xpath("//div[contains(@class, 'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
            yield {
                'currency pair': currency.xpath(".//div[1]/div/text()").get(),
                'volume(24h)': currency.xpath(".//div[2]/span/text()").get()
            }
