import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class HotukSpider(scrapy.Spider):
    name = "hotuk"
    allowed_domains = ["hotukdeals.com"]
    start_urls = ["https://hotukdeals.com/new"]
    
    #rules = [Rule(LinkExtractor(allow=))]

    def parse(self, response):
        yield{
            'title-2nd':response.xpath('//article//strong/a/text()').get(),
            'price_tag':response.css('.thread-price::text').get(),
            'seller':response.css('.cept-merchant-name::text').get(),
            
        }
