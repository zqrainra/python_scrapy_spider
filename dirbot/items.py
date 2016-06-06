from scrapy.item import Item, Field
import scrapy

class Website(Item):

    name = Field()
    description = Field()
    url = Field()

class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)

class Article(scrapy.Item):
    title = Field()
    url = Field()

class Url(scrapy.Item):
    url = Field()

class Content(scrapy.Item):
    title = Field()
    abstract = Field()
    ptime = Field()
    content = Field()
    image_urls = Field()
    images = Field()

class ScrapscrapyItem(Item):
    # define the fields for your item here like:
    # name = Field()
    Heading = Field()
    Content = Field()
    Source_Website = Field()
    pass

class RiliItem(Item):
    predict_time = Field()
    state = Field()
    title = Field()
    importance = Field()
    before = Field()
    forecast = Field()
    reality = Field()
    effect = Field()
    autoid = Field()

class Xgsg(Item):
    content = Field()


