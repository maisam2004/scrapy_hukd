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

        deal['title'] = [title.strip() for title in  deal['title']]
        deal['price_tag'] = [price_tag.strip() for price_tag in  deal['price_tag']]
        deal['seller'] = [seller.strip() for seller in  deal['seller']]
        return deal
       
    
class CreateCsvPipeline:    
    def process_item(self,deal,spider):
        rows = zip(deal['title'],deal['price_tag'],deal['seller'])
        with open('deals.csv','a',newline='',encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Title','Price','Seller'])

            for row in rows:
                writer.writerow(row)

        return deal
    


    '''
    just class of create class practice :
    class CreateCsvPipeline:
    def __init__(self):
        self.file = open('output.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['Title', 'Price', 'Seller'])

    def process_item(self, deal, spider):
        row = (deal['title'], deal['price_tag'], deal['seller'])
        self.writer.writerow(row)
        return deal

    def close_spider(self, spider):
        self.file.close()
    '''