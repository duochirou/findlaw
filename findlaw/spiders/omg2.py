import scrapy
import json
import re
from scrapy.loader import ItemLoader

class BaiduSpider(scrapy.Spider):
    name = 'omg2'
    # 允许域名
    allowed_domains = ['baidu.com/']
    # 获取前50队伍Id
    tn = 50
    start_url = []
    for i in range(0, 50, 10):
        teamId_url = 'https://zhidao.baidu.com/uteam/ajax/rankdetail?' \
                     'type=0&pn=%d&rn=10&monthTime=1506787200&cid=103'%(tn)
        start_url.append(teamId_url)
    start_urls = start_url

    def parse(self, response):
        bodyStr = response.body.decode()
        bodyJson = json.loads(bodyStr)
        if bodyJson['errno'] == 0:
            print("gogogogogogo-------------------------------------")
        if 'data' in bodyJson['data']:
            teamList = bodyJson['data']['data']
            for teamInfo in teamList:
                teamId = teamInfo['teamId']
                # 根据teamId 爬取team所有回答
                url = 'https://zhidao.baidu.com/uteam/ajax/answer?' \
                      'teamId=%d&pn=0&rn=50&type=0'%(int(teamId))
                pn = 0
                item = BaiduItem()
                item['teamId'] = teamId
                request = scrapy.Request(url=url, callback=self.item_parse, dont_filter=True)
                request.meta['item'] = item
                request.meta['pn'] = pn
                yield request
        # pn = 0
        # item = BaiduItem()
        # item['teamId'] = 98221
        # request = scrapy.Request(url='https://zhidao.baidu.com/uteam/ajax/answer?teamId=98221&pn=0&rn=50', callback=self.item_parse, dont_filter=True)
        # request.meta['item'] = item
        # request.meta['pn'] = pn
        # yield request


    def item_parse(self, response):
        self.logger.info("Visited %s", response.url)
        item = response.meta['item']
        pn = response.meta['pn']
        # 每页内容爬取
        bodyStr = response.body.decode()
        bodyJson = json.loads(bodyStr)
        if bodyJson['errno'] == 0:
            print("gogogogogogo-------------------------------------")
        if 'data' in bodyJson:
            data = bodyJson['data']
            monthlyTotalWealth = data['monthlyTotalWealth']
            monthlyAnswerUserNum = data['monthlyAnswerUserNum']
            monthlyAnswerNum = data['monthlyAnswerNum']
            monthlyAnswerList = data['monthlyAnswerList']
            for element in monthlyAnswerList:
                item['qid'] = element['qid']
                item['qtitle'] = element['qtitle']
                item['rContent'] = element['rContent']
                item['isGood'] = element['isGood']
                yield item
        # 继续遍历下一页
        if pn<monthlyAnswerNum:
            pn += 50
            url = response.url.split('&')[0] + '&pn=' + str(pn) + '&' + response.url.split('&')[2]
            request = scrapy.Request(url=url, callback=self.item_parse, dont_filter=True)
            request.meta['item'] = item
            request.meta['pn'] = pn
            yield request
