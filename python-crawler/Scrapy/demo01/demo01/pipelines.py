# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BaiduPipeline:
    """爬取网页数据"""
    def process_item(self, item, spider):
        print(item,spider)
        return item
class BaiduMysqlPipeline:
    """存储网页数据到数据库"""
    def process_item(self,item,spider):
         return item