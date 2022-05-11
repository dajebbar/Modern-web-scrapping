# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import (
    MapCompose,
    TakeFirst,
    Join,
)
from w3lib.html import remove_tags

def remove_quotations(value):
    return value.replace(u"\u201d", '').replace(u"\u201c", '')
class GoodreadsItem(scrapy.Item):
    # Create Fields
    author_img = scrapy.Field()
    text = scrapy.Field(
        input_processor=MapCompose(
            str.strip,
            remove_quotations
        ),
        output_processor=TakeFirst()
    )
    author_name = scrapy.Field(
        input_processor=MapCompose(
            remove_tags
        ),
        output_processor=TakeFirst()
    )
    tags = scrapy.Field(
        input_processor=MapCompose(
            remove_tags
        ),
        output_processor=Join()
    )
    likes = scrapy.Field(
        input_processor=MapCompose(
            remove_tags
        ),
        output_processor=TakeFirst()
    )
