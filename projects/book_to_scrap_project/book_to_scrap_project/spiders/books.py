import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    # start_urls = ['http://books.toscrape.com/']

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(
            url='http://books.toscrape.com/',
            headers={
                'User-Agent': self.user_agent
            }
        )

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='image_container']/a"), 
        callback='parse_item', 
        follow=True, 
        process_request='set_user_agent',
        ),

        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a"), 
        process_request='set_user_agent',
        ),
    )

    def set_user_agent(self, request, response):
        request.headers['User-Agent'] = self.user_agent
        return request

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
