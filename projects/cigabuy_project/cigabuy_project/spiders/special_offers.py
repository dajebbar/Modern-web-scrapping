import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.cigabuy.com']
    start_urls = ['https://www.cigabuy.com/specials.html']

    def parse(self, response):
        wrapers = response.xpath("//div[@class='p_box_wrapper']/div")
        stars = response.xpath("//div[@class='p_box_star']")
        prices = response.xpath("//div[@class='p_box_price cf']")
        for wraper in wrapers:
            product_title = wraper.xpath(".//a[@class='p_box_title']/text()").get()
            product_link = wraper.xpath(".//a[@class='p_box_img']/@href").get()
            product_img = wraper.xpath(".//a[@class='p_box_img']/img/@data-original").get()

            yield{
                'product_name': product_title,
                'link': product_link,
                'product_img': product_img,
            }
        for star in stars:
            product_stars = star.xpath(".//a/@href").get()

            yield{
                'product_stars': product_stars,
            }
        for price in prices:
            product_price = price.xpath(".//text()").get()
            
            yield {
                'product_price': product_price,
                }
