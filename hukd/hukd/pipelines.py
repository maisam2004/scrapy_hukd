# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class HukdPipeline:
    def process_item(self, deal, spider):
        if not deal['title'] or not deal['price_tag'] or not deal['seller']:
            raise DropItem('Missing something')

        return deal

class Cleaning_data:
    def process_item(self,deal,spider):
        deal['title'] = deal['title'].strip()
        deal['price_tag'] = deal['price_tag'].strip()
        deal['seller'] = deal['seller'].strip()
        return deal
    
    
    
class Create_csv:    
    def process_deal(self,deal):
        rows = zip(deal['title'],deal['price_tag'],deal['seller'])
        with open('deals.csv','a',newline='',encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Title','Price','Seller'])

            for row in rows:
                writer.writerow(row)

        return deal