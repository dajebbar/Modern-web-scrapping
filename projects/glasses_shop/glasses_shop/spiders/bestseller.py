import scrapy


class BestsellerSpider(scrapy.Spider):
    name = 'bestseller'
    allowed_domains = ['www.glassesshop.com']
    # start_urls = ['https://www.glassesshop.com/bestsellers/']

    def start_requests(self):
        yield scrapy.Request(
            url='https://www.glassesshop.com/bestsellers/',
            callback=self.parse,
            headers={
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
            }
        )

    def parse(self, response):
        glasses = response.xpath("//div[@class='col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item']")
        for glass in glasses:
             yield {
                'url': glass.xpath(".//div[@class='product-img-outer']/a/@href").get(),
                'img_url': glass.xpath(".//div[@class='product-img-outer']/a/img/@data-src").get(),
                'product_name': glass.xpath("normalize-space(.//div[@class='p-title-block']/div[@class='mt-3']/div[@class='row no-gutters']/div[@class='col-6 col-lg-6']/div[@class='p-title']/a/text())").get(),
                'price': glass.xpath("div[@class='p-title-block']/div[@class='mt-3']/div[@class='row no-gutters']/div[@class='col-6 col-lg-6']/div[@class='p-price']/div/span/text()").get(),
                'User-Agent': response.request.headers['User-Agent']
            }
        
        next_page = response.xpath("//ul[@class='pagination']/li/a[@class='page-link']/href").get()
        if next_page:
            scrapy.Request(
                url=next_page,
                callback=self.parse,
                headers={
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
            }
            )
