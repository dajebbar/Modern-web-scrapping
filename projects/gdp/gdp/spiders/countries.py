import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt']

    def parse(self, response):
        countries = response.xpath("//tbody/tr")
        for country in countries:
            country_link = country.xpath(".//td[1]/a/@href").get()
        
            yield response.follow(
                url=country_link,
                callback=self.parse_gdp,
                meta={
                    'country_name': country.xpath(".//td[1]/a/text()").get(),
                    'debt_to_gdp_ratio': country.xpath(".//td[2]/text()").get(),
                    'population': country.xpath(".//td[3]/text()").get(),

                }
            )
            # yield {
            #     'country_name': country.xpath(".//td[1]/a/text()").get(),
            #     'country_link': country.xpath(".//td[1]/a/@href").get(),
            #     'debt_to_gdp_ratio': country.xpath(".//td[2]/text()").get(),
            #     'population': country.xpath(".//td[3]/text()").get(),
            # }
    def parse_gdp(self, response):
        items = response.xpath("(//table[@class='jsx-2006211681 table is-striped is-hoverable is-fullwidth tp-table-body is-narrow'])[2]/tbody/tr")

        for item in items:
            year = item.xpath(".//td[1]/text()").get()
            growth_rate = item.xpath(".//td[3]/span/text()").get()

            yield {
                'country_name': response.request.meta['country_name'],
                'year': year,
                'debt_to_gdp_ratio': response.request.meta['debt_to_gdp_ratio'],
                'growth_rate' : growth_rate,
                'population': response.request.meta['population'],
                
            }
