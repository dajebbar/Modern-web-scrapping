import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/search/title/?groups=top_1000']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"))
    )

    def parse_item(self, response):
    #    print(response.url)
        yield {
            'title': response.xpath("//div[@class='sc-94726ce4-1 iNShGo']/h1/text()").get(),
            'year': response.xpath("(//span[@class='sc-8c396aa2-2 itZqyK'])[1]/text()").get(),
            'genre': response.xpath("(//li[@class='ipc-inline-list__item ipc-chip__text'])[1]/text()").get(),
            'public_permission': response.xpath("(//span[@class='sc-8c396aa2-2 itZqyK'])[2]/text()").get(),
            'duration_hr': response.xpath("(//li[@class='ipc-inline-list__item'])[3]/text()[1]").get(),
            'duration_min': response.xpath("(//li[@class='ipc-inline-list__item'])[3]/text()[4]").get(),
            'noted_imdb': response.xpath("//span[@class='sc-7ab21ed2-1 jGRxWM']/text()").get(),
            'movie_poster': response.urljoin(response.xpath("//a[@class='ipc-lockup-overlay ipc-focusable']/@href").get()),
            'play_trailer': response.urljoin(response.xpath("//a[@class='ipc-lockup-overlay sc-5ea2f380-2 gdvnDB hero-media__slate-overlay ipc-focusable']/@href").get()),
            'movie_url': response.url,
        }
