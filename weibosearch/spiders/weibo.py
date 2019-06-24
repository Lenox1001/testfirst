# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider,FormRequest

class WeiboSpider(scrapy.Spider):
    name = "weibo"
    allowed_domains = ["weibo.cn"] #过滤爬取的域名
    search_urls = 'https://weibo.cn/search/mblog'
    max_page = 2

    def start_request(self):
        keyword = '000001' #修改成000001测试，原本是抑郁症
        url = '{url}?keyword={keyword}',format(url=self.search_url,keyword=keyword)
        for page in range(self.max_page+1):
            data = {
                'mp': str(self.max_page),
                'page': str(page)
            }
            yield FormRequest(url, callback=self.parse_index, formdata=data)

    def parse_index(self, response):
        print(response.text)