# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from douban.settings import mongo_host, mongo_prot, mongo_db_collection, mongo_db_name


class DoubanPipeline:

    def __init__(self):
        host = mongo_host
        prot = mongo_prot
        dbname = mongo_db_name
        sheetname = mongo_db_collection

        client = pymongo.MongoClient(host=host, port=prot)
        mydb = client[dbname]
        self.post = mydb[sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
