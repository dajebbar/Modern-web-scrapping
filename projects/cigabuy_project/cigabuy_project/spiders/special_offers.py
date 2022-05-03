import scrapy



class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.cigabuy.com']
    # start_urls = ['https://www.cigabuy.com/specials.html']

    # def start_requests(self):
    #     yield scrapy.Request(
    #         url='https://www.cigabuy.com/specials.html',
    #         callback=self.parse,
    #         headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'}
    #         )

    def start_requests(self):
        yield scrapy.Request(url='https://web.archive.org/web/20190324163700/http://www.tinydeal.com/specials.html', callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        })

    def parse(self, response):
        wrapers = response.xpath("//ul[@class='productlisting-ul']/div[@class='p_box_wrapper']/div")
        
        for wraper in wrapers:
            product_title = wraper.xpath(".//a[@class='p_box_title']/text()").get()
            product_link = wraper.xpath(".//a[@class='p_box_img']/@href").get()
            product_img = wraper.xpath(".//a[@class='p_box_img']/img/@data-original").get()
            product_stars = wraper.xpath(".//div[@class='p_box_star']/a/@href").get()
            original_price = wraper.xpath(".//div[@class='p_box_price cf']/span[@class='normalprice fl']/text()").get()
            promo_price = wraper.xpath(".//div[@class='p_box_price cf']/span[@class='productSpecialPrice fl']/text()").get()

            yield {
                'product_title': product_title,
                'product_link': product_link, 
                'product_img': product_img,
                'product_stars': product_stars,
                'original_price': original_price,
                'promo_price': promo_price,
                'User-Agent': response.request.headers['User-Agent']
            }
        
        next_page = response.xpath("//a[@class='pageNum']/@href").get()
        # if next_page:
        #     yield scrapy.Request(
        #         url=next_page, 
        #         callback=self.parse,
        #         headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'},
        #         )

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
            })
               