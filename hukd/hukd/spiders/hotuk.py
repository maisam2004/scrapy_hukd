import scrapy
import csv
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from hukd.items import HukdItem

class HotukSpider(scrapy.Spider):
    name = "hotuk"
    allowed_domains = ["hotukdeals.com"]
    start_urls = ["https://hotukdeals.com/new","https://www.hotukdeals.com/deals-new?page=2"]
    
    #rules = [Rule(LinkExtractor(allow=))]
 

    def parse(self, response):
        deal = HukdItem()
        deal['title'] = response.xpath('//article//strong/a/text()').getall()
        deal['price_tag']=response.css('.thread-price::text').getall()
        deal['seller']=response.css('.cept-merchant-name::text').getall()
        
        
        yield deal
    
"""   def process_deal(self,deal):
        rows = zip(deal['title'],deal['price_tag'],deal['seller'])
        with open('deals.csv','a',newline='',encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Title','Price','Seller'])

            for row in rows:
                writer.writerow(row)

        return deal
         """
      