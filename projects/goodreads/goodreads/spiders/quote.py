import scrapy
# import item loader
from scrapy.loader import ItemLoader
# import GoodreadsItem class
from goodreads.items import GoodreadsItem


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['www.goodreads.com']
    start_urls = ['https://www.goodreads.com/quotes']

    def parse(self, response):
        quotes = response.xpath("//div[@class='quoteDetails']")
        for quote in quotes:
            loader = ItemLoader(item=GoodreadsItem(), selector=quote, response=response)
            loader.add_xpath("author_img", ".//a[@class='leftAlignedImage']/img/@src")
            loader.add_xpath("text", "normalize-space(.//div[@class='quoteText'])")
            loader.add_xpath("author_name", "normalize-space(.//span[@class='authorOrTitle'])")
            loader.add_xpath("tags", ".//div[@class='greyText smallText left']/a")
            loader.add_xpath("likes", ".//a[@class='smallText']")

            yield loader.load_item()

            # yield {
            #     'author_img': quote.xpath(".//a[@class='leftAlignedImage']/img/@src").get(),
            #     'text': quote.xpath("normalize-space(.//div[@class='quoteText']/text())").get(),
            #     'author_name': quote.xpath("normalize-space(.//span[@class='authorOrTitle']/text())").get(),
            #     'tags': quote.xpath(".//div[@class='greyText smallText left']/a/text()").getall(),
            #     'likes': quote.xpath(".//a[@class='smallText']/text()").get(),
            # }

        next_page = response.xpath("//a[@rel='next']/text()").get()
        if next_page:
            url = f'https://www.goodreads.com/quotes?page={next_page}'
            yield scrapy.Request(
                url=url,
                callback=self.parse,

            )
