import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['www.goodreads.com']
    start_urls = ['https://www.goodreads.com/quotes']

    def parse(self, response):
        quotes = response.xpath("//div[@class='quoteDetails']")
        for quote in quotes:
            yield {
                'author_img': quote.xpath(".//a[@class='leftAlignedImage']/img/@src").get(),
                'text': quote.xpath("normalize-space(.//div[@class='quoteText']/text())").get(),
                'author_name': quote.xpath("normalize-space(.//span[@class='authorOrTitle']/text())").get(),
                'tags': quote.xpath("//div[@class='greyText smallText left']/a/text()").getall(),
                'likes': quote.xpath("//a[@class='smallText']/text()").get(),
            }

        
