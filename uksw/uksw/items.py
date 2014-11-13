# -*- coding: utf-8 -*-

from scrapy.item import Item, Field

class DataItem(Item):
    title = Field()
    abstract = Field()
    subject = Field()
    keywords = Field()
    id = Field()
    date = Field()



