import scrapy
from matplotlib.pyplot import title


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        with open('example.html', 'wb') as f:
            f.write(response.body)

