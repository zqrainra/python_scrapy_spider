#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2016-05-23
__author__ = 'Bob'

from scrapy.spiders import Spider
from dirbot.items import RiliItem
from scrapy.selector import Selector

class RiliSpider(Spider):
    name = 'rili'
    allowed_domains = ["kxt.com"]
    start_urls = [
        "http://www.kxt.com/rili",
    ]
    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//table[@id="Finance"]/tr[@class="rlDateItem"]')

