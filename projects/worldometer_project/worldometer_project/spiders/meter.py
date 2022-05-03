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
        country_name = response.request.meta['country_name']
        rows = response.xpath("")


        yield {
            'country': country_name,
            'year': year,
            'population': population,
            'yearly_%_change': yearly_pct_change,
            'yearly_change': yearly_change,
            'migrants(net)': migrants,
            'median_age': median_age,
            'fetility_rate': fertility_rate,
            'density': density,
            'urban_pop_%': urban_pop_pct,
            'urban_pop': urban_pop,
            'country_share_of_world_pop' : share_world_pop,
            'world_pop': world_pop,
            f'{country_name}_global_rank': global_rank,

        }
