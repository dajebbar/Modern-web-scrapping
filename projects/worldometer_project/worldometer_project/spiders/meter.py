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
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")

        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            yearly_pct_change = row.xpath(".//td[3]/text()").get()
            yearly_change = row.xpath(".//td[4]/text()").get()
            migrants = row.xpath(".//td[5]/text()").get()
            median_age = row.xpath(".//td[6]/text()").get()
            fertility_rate = row.xpath(".//td[7]/text()").get()
            density = row.xpath(".//td[8]/text()").get()
            urban_pop_pct = row.xpath(".//td[9]/text()").get()
            urban_pop = row.xpath(".//td[10]/text()").get()
            share_world_pop = row.xpath(".//td[11]/text()").get()
            world_pop = row.xpath(".//td[12]/text()").get()
            global_rank = row.xpath(".//td[13]/text()").get()


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
