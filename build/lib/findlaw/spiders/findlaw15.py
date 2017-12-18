# -*- coding: utf-8 -*-
# -*- coding:UTF-8 -*-
import scrapy
#from findlaw.items import QA
import time

# class Findlaw15Spider(scrapy.Spider):
#     #download_delay = 2
#     name = 'findlaw15'
#     allowed_domains = ['china.findlaw.cn']
#     year = ['2017']
#     month = ['01', '02']
#     start_urls = []
#     for y in year:
#         for m in month:
#             url = ['http://china.findlaw.cn/ask/p15_d', y, m, '_t01/']
#             start_url = ''.join(url)
#             start_urls.append(start_url)
#     # start_urls = ['http://china.findlaw.cn/ask/p64_d201701_t01/',
#     #               'http://china.findlaw.cn/ask/p64_d201701_t01_page2/']
#
#     def parse(self, response):
#         for href in response.css('.result-list .result-lawyer-item a::attr(href)').extract():
#             request = scrapy.Request(url=href, callback=self.parse_page, dont_filter=True)
#             yield request
#
#         # next page
#         current_url = response.url
#         next_url = response.css('.pagination-item.active+a::attr(href)').extract_first()
#         #last_url = response.css('.pagination-item:last-child::attr(href)').extract_first()
#         if next_url != None and next_url != current_url:
#             #time.sleep(60)
#             yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse, dont_filter=True)
#
#     def parse_page(self, response):
#         self.logger.info("Visited %s", response.url)
#         # item = QA()
#         # item['qTitle'] = response.css('.question-title::text').extract_first()
#         # item['qText'] = response.css('.question-text::text').extract_first()
#         # item['qTag'] = response.css('.question-tops span::text').extract()[2]
#         # #
#         # item['aText'] = response.css('.answer-text::text').extract()
#         # yield item
#         yield {'qTitle': response.css('.question-title::text').extract_first(),
#                'qText' : response.css('.question-text::text').extract_first(),
#                'qTag' : response.css('.question-tops span::text').extract()[2],
#                'aText' : response.css('.answer-text::text').extract(),
#                }
# test IP
class FindlawSpider(scrapy.Spider):
    name = 'findlaw15'
    allowed_domains = []

    def start_requests(self):

        url = 'http://ip.chinaz.com/getip.aspx'

        for i in range(10000):
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self,response):
        print(response.text)
