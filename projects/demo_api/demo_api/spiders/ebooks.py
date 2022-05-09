import scrapy
import json


class EbooksSpider(scrapy.Spider):
    name = 'ebooks'
    allowed_domains = ['openlibrary.org']
    start_urls = ['https://openlibrary.org/subjects/picture_books.json?limit=12&offset=12']

    def parse(self, response):
        resp = json.loads(response.body)
        ebooks = resp.get('works')

        for ebook in ebooks:
            yield {
                'title': ebook.get('title'),
                'authors': ebook.get('authors')[-1].get('name'),
                'subjects': ebook.get('subject'),
                # 'collections': ebook.get('ia_collection'),

            }
