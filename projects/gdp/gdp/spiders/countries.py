import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt']

    def parse(self, response):
        countries = response.xpath("//tbody/tr")
        for country in countries:
            yield {
                'country_name': country.xpath(".//td[1]/a/text()").get(),
                'debt_to_gdp_ratio': country.xpath(".//td[2]/text()").get(),
                'population': country.xpath(".//td[3]/text()").get(),
            }
