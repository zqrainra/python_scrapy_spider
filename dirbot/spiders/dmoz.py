#_*_coding:utf-8_*_
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from dirbot.items import Website,Content,Article,Url
from scrapy.http import Request
import re

class DmozSpider(CrawlSpider):
    name = "dmoz"
    allowed_domains = ["eastmoney.com"]
    start_urls = [
        "http://www.eastmoney.com/",
    ]
    rules= (
        Rule(LinkExtractor(allow=("stock.eastmoney.com/news.*",),restrict_xpaths=('//div[@id="gsjd_lc_conts"]/div/ul/li[position() >= 1 and position() <= 3]'), unique=True), callback = 'parse_item', follow = False),
        # Rule(LinkExtractor(allow=("stock.eastmoney.com/news.*",),restrict_xpaths=('//div[@id="gsjd_lc_conts"]/div/ul/li[1]'), unique=True), callback = 'parse_item', follow = False),
    )
    # def parse(self, response):
    #     """
    #     The lines below is a spider contract. For more info see:
    #     http://doc.scrapy.org/en/latest/topics/contracts.html
    #
    #     @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
    #     @scrapes name
    #     """
    #     sel = Selector(response)
    #     sites = sel.xpath('//div[@id="gsjd_lc_conts"]/div/ul/li')
    #     items = []
    #
    #     for i in range(3):
    #         # for j in sites[i].xpath('a'):
    #         #     url = j.xpath('@href').extract()
    #         #     name = j.xpath('strong/text()').extract()
    #         #     if len(name) == 0:
    #         #         name = j.xpath('text()').extract()
    #         #
    #         #     item = Article()
    #         #     item['title'] = name
    #         #     item['url'] = url
    #         #     items.append(item)
    #
    #         urls = sites[i].xpath('a/@href').extract()
    #         for url in urls:
    #             # item = Url()
    #             # item['url'] = j
    #             # items.append(item)
    #             yield Request(url,callback='self.parse_item')
    #         # for url in items:
    #         #     yield Request(url,callback=self.parse_item)
    #     # return items


    def parse_item(self,response):
        item = Content()
        items = []
        item['title'] = response.xpath('//div[@class="newText new"]/h1/text()').extract()
        item['abstract'] = response.xpath('//div[@class="c_review"]/text()').extract()
        item['ptime'] = response.xpath('//div[@class="Info"]/span[1]/text()').extract()
        item['image_urls'] = response.xpath('//div[@class="Info"]/span/img/@src').extract()
        contents = response.xpath('//div[contains(@id,"ContentBody")]/p//text()')
        tmp_content = ''
        for i in contents:
            tmp_content += i.extract()

        # m = re.match(r'(.*)\u5927\u52bf\u7814\u5224>>>.*',tmp_content)
        m = re.split(ur'[\u3400-\u9FFF]{4}>>>',tmp_content)
        if len(m[0]) == 0:
            item['content'] = m[1]
        else:
            item['content'] = m[0]
        # item['content'] = m.groups()[0]
        if len(item) != 0:
            items.append(item)

        return items


