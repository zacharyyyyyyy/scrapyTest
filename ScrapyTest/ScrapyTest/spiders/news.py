# -*- coding: utf-8 -*-
import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['/china.huanqiu.com/article']
    start_urls = ['http://china.huanqiu.com/article/index.html?agt=15438']

    def parse(self, response):
        title=response.xpath('//div[@class="fallsFlow"]/ul/li/h3/a/text()').extract()
        content=response.xpath('//div[@class="fallsFlow"]/ul/li/h5/text()').extract()
        for i in range(0,len(content)):
            print('标题： %s '% title[i])
            print('内容： %s '% content[i])
            print('\n')

        ThisPage=response.xpath('//div[@class="pageBox"]/div/span/text()').extract()
        print("第 %s 页"%ThisPage[0])

