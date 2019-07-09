# -*- coding: utf-8 -*-
import scrapy


class XiamiSpiderSpider(scrapy.Spider):
    name = 'xiami_spider'
    allowed_domains = ['xiami.com']
    url = 'https://www.xiami.com/api/search/searchSongs?_q=%7B%22key%22:%22%E6%B1%AA%E5%B3%B0%22,%22pagingVO%22:%7B%22page%22:{},%22pageSize%22:60%7D%7D&_s=2a3b62b114387d7b9b268e90bd88891d'

    def start_requests(self):
        for i in range():
            self.url.format(i)



    def parse(self, response):
        pass
