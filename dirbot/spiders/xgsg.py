#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2016-05-31
__author__ = 'Bob'

from scrapy.spiders import Spider
from dirbot.items import Xgsg

class Xgsg(Spider):
    name = 'xgsg'
    allowed_domains = ["eastmoney.com"]
    start_urls = [
        "http://data.eastmoney.com/xg/xg",
    ]

    def parse(self, response):
        rel = response.xpath('//div[@class="contentBox"]')

        items = Xgsg()
        items['content'] = rel.extract()