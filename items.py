# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose,TakeFirst
from w3lib.html  import remove_tags


class PeriodicElementItem(scrapy.Item):
    # define the fields for your item here like:
    symbol = scrapy.Field(
        input_processor=MapCompose(remove_tags,str.strip),
        output_processor=TakeFirst()

    )
    name = scrapy.Field(
        input_processor=MapCompose(remove_tags,str.strip),
        output_processor=TakeFirst()
    )
    atomic_number = scrapy.Field(
        input_processor=MapCompose(remove_tags,str.strip,int),
        output_processor=TakeFirst()
    )
    atomic_mass = scrapy.Field(
        input_processor=MapCompose(remove_tags,str.strip,float),
        output_processor=TakeFirst()
    )
    chemical_group = scrapy.Field(
        input_processor=MapCompose(remove_tags,str.strip),
        output_processor=TakeFirst()
    )
   
