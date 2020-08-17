import scrapy
from scrapy.item import Item, Field

# totalrank items for pipeline
class MiaTotalItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field()
    level = scrapy.Field()
    region = scrapy.Field()
    date = scrapy.Field()
    totalrank = scrapy.Field()
    totalchange = scrapy.Field()
    tranksymbol = scrapy.Field()
    totalscore = scrapy.Field()

# singlerank items for pipeline
class MiaSingleItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field()
    level = scrapy.Field()
    region = scrapy.Field()
    date = scrapy.Field()
    singlerank = scrapy.Field()
    singlechange = scrapy.Field()
    sranksymbol = scrapy.Field()
    singlescore = scrapy.Field()

# doublerank items for pipeline
class MiaDoubleItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field()
    level = scrapy.Field()
    region = scrapy.Field()
    date = scrapy.Field()
    doublerank = scrapy.Field()
    doublechange = scrapy.Field()
    dranksymbol = scrapy.Field()
    doublescore = scrapy.Field()

# exprank items for pipeline
class MiaEXPItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field()
    level = scrapy.Field()
    region = scrapy.Field()
    date = scrapy.Field()
    exprank = scrapy.Field()
    expchange = scrapy.Field()
    expranksymbol = scrapy.Field()
    expscore = scrapy.Field()
