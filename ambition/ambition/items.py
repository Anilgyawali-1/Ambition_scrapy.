# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class AmbitionItem(scrapy.Item):

    # define the fields for your item here like:

    company_name = scrapy.Field()
    ratings = scrapy.Field()
    nob = scrapy.Field()
    toc = scrapy.Field()
    ceo = scrapy.Field()
    ownership = scrapy.Field()
    headquarters = scrapy.Field()
    founded_in = scrapy.Field()
    ccn = scrapy.Field()
    description = scrapy.Field()

