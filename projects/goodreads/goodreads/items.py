# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GoodreadsItem(scrapy.Item):
    # Create Fields
    author_img = scrapy.Field()
    text = scrapy.Field()
    author_name = scrapy.Field()
    tags = scrapy.Field()
    likes = scrapy.Field()
