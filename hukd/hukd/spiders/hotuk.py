import scrapy


class HotukSpider(scrapy.Spider):
    name = "hotuk"
    allowed_domains = ["hotukdeals.com"]
    start_urls = ["https://hotukdeals.com"]

    def parse(self, response):
        pass
