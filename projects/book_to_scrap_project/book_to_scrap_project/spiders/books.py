import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='image_container']/a"), 
        callback='parse_item', 
        follow=True
        ),
    )

    def parse_item(self, response):
        yield {
            'title': response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get(),
            'book_img': response.urljoin(response.xpath("//div[@class='item active']/img/@src").get()),
            'upc': response.xpath("//tr[1]/td/text()").get(),
            'price_(excl.tax)': response.xpath("//tr[3]/td/text()").get(),
            'price_(incl.tax)': response.xpath("//tr[4]/td/text()").get(),
            'tax': response.xpath("//tr[5]/td/text()").get(),
            'Availability': response.xpath("//tr[6]/td/text()").get(),
            'num_of_reviews': response.xpath("//tr[7]/td/text()").get(),
        }
