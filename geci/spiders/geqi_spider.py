# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GeqiSpiderSpider(CrawlSpider):
    name = 'geqi_spider'
    allowed_domains = ['music.163.com']
    start_urls = ['https://music.163.com/#/search/m/?s=%E6%B1%AA%E5%B3%B0&type=1']

    rules = (
        Rule(LinkExtractor(allow=r'https://music.163.com/#/song\?id=\d+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath(".//em[@class = 'f-ff2']/text()").extract()
        item['author'] = response.xpath(".//div[@class = 'cnt']/p[1]//a/text()").extract()
        # item['lyric'] = response.xpath(".//div[@class = 'cnt']/div[@id = 'lyric-content']/text()") + response.xpath(".//div[@class = 'cnt']//div[@id = 'flag_more']/text()")
        # item['url'] = response.url
        # item['flag'] = "网易云音乐汪峰歌词"
        print(item)
        return item
#  首页的连接xpath：result .//div[@class = 'srchsongst']/div[contains(@class,'item f-cb h-flag')]