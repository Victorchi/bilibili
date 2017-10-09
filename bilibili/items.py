# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    UpIntroduction=scrapy.Field()
    url=scrapy.Field()
    category1=scrapy.Field()
    category2=scrapy.Field()
