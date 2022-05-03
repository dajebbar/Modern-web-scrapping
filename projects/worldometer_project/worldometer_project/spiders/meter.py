import scrapy


class MeterSpider(scrapy.Spider):
    name = 'meter'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath("//table[@id='example2']/tbody/tr/td/a")
        for country in countries:
            country_name = country.xpath(".//text()").get()
            country_link = country.xpath(".//@href").get()

            yield response.follow(
                url=country_link,
                callback=self.country_parse,
                meta={
                    'country_name': country_name,
                }
            )

    def country_parse(self, response):
        pass
