# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FindlawItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QA(scrapy.Item):
    qTitle = scrapy.Field()
    qTag = scrapy.Field()
    qText = scrapy.Field()
    aText = scrapy.Field()

