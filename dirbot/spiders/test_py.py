#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2016-05-24
__author__ = 'Bob'

def parse_item(self,response):
    sel = response.xpath('//div[@id="ContentBody"]/p')
    d = ''
    for i in sel:
        p_t = i.xpath('text()')
        p_s = i.xpath('strong')
        p_a = i.xpath('span/a')
        p_a_t = i.xpath('span/a/text()')
        p_s_s = i.xpath('strong/span/text()')
        if len(p_a_t) != 0:
            res = i.extract()
            for j in p_a:
                res = res.replace(j.extract()[0],j.xpath('text()').extract()[0])
            d += res
            # d += i.extract().replace(p_a.extract()[0],p_a_t.extract()[0])
        elif len(p_s_s) != 0:
            pass
        elif len(p_s) != 0:
            d += i.extract()[0]
        elif len(p_t) != 0:
            d += i.extract()[0]
