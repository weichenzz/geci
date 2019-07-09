# -*- coding: utf-8 -*-
import scrapy
import json

class WangyiSpiderSpider(scrapy.Spider):
    name = 'wangyi_spider'
    allowed_domains = ['music.163.com']
    url = "https://music.163.com/weapi/cloudsearch/get/web?csrf_token=60bdcfbb9673799f0f74317c5872a566"

    def start_requests(self):
        #网易云音乐是通过post请求来获取的，需要传加密的params以及加密的encSecKey参数
        #todo 传参添加一下
        url = self.url
        yield scrapy.Request(url, callback=self.parse, dont_filter=True, meta={'num' : 0, 'base_url' : "https://music.163.com/#{postfix}"})


    def parse(self, response):
        num = response.meta.get('num', 0)
        base_url = response.meta.get('base_url')
        info = json.loads(response.text)
        lyrics_urls = response.xpath(".//div[@class = 'sn']//a[not(@class)]/@href")
        num = num + len(lyrics_urls)
        number = info['result']['songCount']
        for lyrics_url in lyrics_urls:
            #拼接提取歌词的url
            to_lyrics__url = base_url.format(postfix = lyrics_url)
            #访问歌词的url
            yield scrapy.Request(to_lyrics__url,callback=self.parse_detail, dont_filter=True)
            #break

        if num < int(number):
            yield scrapy.Request(self.url,callback=self.parse,dont_filter=True,meta={'num' : num, 'base_url' : "https://music.163.com/#{postfix}"})

    def parse_detail(self, response):
        item = {}
        item['name'] = response.xpath(".//em[@class='f-ff2']/text()")
        item['author'] = response.xpath(".//div[@class = 'cnt']/p[1]//a/text()").extract()
        item['lyric'] = response.xpath(".//div[@class = 'cnt']/div[@id = 'lyric-content']/text()").join(response.xpath(".//div[@class = 'cnt']//div[@id = 'flag_more']/text()"))
        item['url'] = response.url
        item['flag'] = "网易云音乐汪峰歌词"

        #print(item)
        yield item




