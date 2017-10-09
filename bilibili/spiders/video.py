# -*- coding: utf-8 -*-
import scrapy
import requests
import re

class VideoSpider(scrapy.Spider):
    name = 'video'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/video/av2271112/']

    def parse(self, response):
        num = re.sub('.+/av|/$','',response.url)
        view_url = 'https://api.bilibili.com/x/web-interface/archive/stat?callback=jQuery1720735417825650772_1506562164' \
                   '551&aid={}&jsonp=jsonp'.format(num)
        title = response.xpath("//div[@id='viewbox_report']/div[1]/div[1]/h1/text()").extract_first()
        if self.CheckTile(title):
            pass
        up_introduction = response.xpath("//div [@id='v_desc']/text()").extract_first()
        category1 = response.xpath("//div[@id='viewbox_report']/div[1]/div[3]/span[1]/a/text()").extract_first()
        category2 = response.xpath("//div[@id='viewbox_report']/div[1]/div[3]/span[2]/a/text()").extract_first()
        time = response.xpath(".//*[@id='viewbox_report']/div[1]/div[3]/time/i/text()").extract_first()
        ItemView = self.View(view_url)
        print(title,up_introduction,category1,category2,time)
        print(ItemView)
        pass



    def View(self,url):
        '''解析json文件并且返回view对应的字符串'''
        ItemView = {}
        response = requests.get(url).text
        json = self.loadjson(response)
        ItemView['aid'] = json['data']['aid']
        ItemView['view'] = json['data']['view']
        ItemView['danmaku'] = json['data']['danmaku']
        ItemView['favorite'] = json['data']['favorite']
        ItemView['coin'] = json['data']['coin']
        ItemView['share'] = json['data']['share']
        return ItemView

    def loadjson(self,text):
        '''解析json并返回'''
        response = re.sub('.*\d\(|\)$', '', text)
        import json
        json = json.loads(response)
        return json

    def CheckTile(self, title):
        if title == None:
            return False
        else:
            return True