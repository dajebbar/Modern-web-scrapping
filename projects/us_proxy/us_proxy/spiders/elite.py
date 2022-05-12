import scrapy


class EliteSpider(scrapy.Spider):
    name = 'elite'
    allowed_domains = ['hidemy.name']
    start_urls = ['https://hidemy.name/en/proxy-list']

    def parse(self, response):
        table = response.xpath("//div[@class='table_block']/table")
        rows = table.xpath(".//tbody/tr")
        cols = [row.xpath(".//td/text()").getall() for row in rows]

        print(cols)

