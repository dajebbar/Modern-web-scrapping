import scrapy
import json
from scrapy.exceptions import CloseSpider


class EbooksSpider(scrapy.Spider):
    name = 'ebooks'
    allowed_domains = ['openlibrary.org']
    start_urls = ['https://openlibrary.org/subjects/picture_books.json?limit=12']

    INCREMENTED = 12
    offset = 0

    def parse(self, response):
        if response.status == 500:
            raise CloseSpider('Reached last page...')

        resp = json.loads(response.body)
        ebooks = resp.get('works')

        for ebook in ebooks:
            yield {
                'title': ebook.get('title'),
                'authors': ebook.get('authors')[-1].get('name'),
                'subjects': ebook.get('subject'),
                # 'collections': ebook.get('ia_collection'),

            }
        
        self.offset += self.INCREMENTED
        yield scrapy.Request(
            url=f'https://openlibrary.org/subjects/picture_books.json?limit=12&offset={self.offset}',
            callback=self.parse,
            )
