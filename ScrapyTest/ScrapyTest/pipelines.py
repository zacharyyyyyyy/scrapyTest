# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import logging


class ScrapytestPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='',
            db='scrapytest',
            charset='utf8',
            use_unicode=True
        )
        self.cursor=self.connect.cursor()

    def process_item(self, item, spider):
        logging.info('success!!!!!!!!!!!!!!!')
        try:
            for i in range(0,len(item['title'])):
                 self.cursor.execute(
                    "insert into news(title,content) value (%s ,%s)"  , (item['title'][i],item['content'][i])
                 )
                 print('正在插入本页数据的第 ' + str(i+1) +"条")

        except Exception as error:
            raise error
        print("插入数据完成")
        self.connect.commit()
        return item

    def close_spider(self, spider):
        self.connect.close()
        self.cursor.close()