import scrapy
from scrapy.selector import Selector
from mia.items import MiaTotalItem
from mia.items import MiaSingleItem
from mia.items import MiaDoubleItem
from mia.items import MiaEXPItem
import datetime


# totalrank spider
class MiaSpiderTotal(scrapy.Spider):
    name = 'miatotal'
    start_urls = ['http://www.piugame.com/piu.xx/leaderboard/xx_total_rank.php']
    custom_settings = {'ITEM_PIPELINES':{'mia.pipelines.MiaTotalPipeline': 300}}
    
    def parse(self, response):
        players = response.xpath('//ul[@class="chart_body score clearfix"]/li')
        for player in players:
            itemtotal = MiaTotalItem()
            itemtotal['name'] = str(player.xpath('.//span[@class="chart_id"]/text()').get()).strip()
            itemtotal['level'] = str(str(player.xpath('.//div[@class="chart_lv"]/text()').get()).rstrip('\n')).strip()
            itemtotal['region'] = str(player.xpath('.//div[@class="chart_country"]//img/@src').get()).replace('\n','')
            itemtotal['date'] = datetime.datetime.now()
            itemtotal['totalrank'] = str(player.xpath('.//span[@class="rank_out"]/text()').get()).strip()
            itemtotal['tranksymbol'] = str(player.xpath('.//span[@class="updown_info"]//i/@class').get())
            itemtotal['totalchange'] = str(player.xpath('.//span[@class="updown_info"]//text()').get()).strip()
            itemtotal['totalscore'] = str(player.xpath('.//div[@class="chart_score"]/text()').get()).replace(',','')
            yield itemtotal

# singlerank spider
class MiaSpiderSingle(scrapy.Spider):
    name = 'miasingle'
    start_urls = ['http://www.piugame.com/piu.xx/leaderboard/xx_single_rank.php']
    custom_settings = {'ITEM_PIPELINES':{'mia.pipelines.MiaSinglePipeline': 300}}
    
    def parse(self, response):
        players = response.xpath('//ul[@class="chart_body score clearfix"]/li')
        for player in players:
            itemsingle = MiaSingleItem()
            itemsingle['name'] = str(player.xpath('.//span[@class="chart_id"]/text()').get()).strip()
            itemsingle['level'] = str(str(player.xpath('.//div[@class="chart_lv"]/text()').get()).rstrip('\n')).strip()
            itemsingle['region'] = str(player.xpath('.//div[@class="chart_country"]//img/@src').get()).replace('\n','')
            itemsingle['date'] = datetime.datetime.now()
            itemsingle['singlerank'] = str(player.xpath('.//span[@class="rank_out"]/text()').get()).strip()
            itemsingle['sranksymbol'] = str(player.xpath('.//span[@class="updown_info"]//i/@class').get())
            itemsingle['singlechange'] = str(player.xpath('.//span[@class="updown_info"]//text()').get()).strip()
            itemsingle['singlescore'] = str(player.xpath('.//div[@class="chart_score"]/text()').get()).replace(',','')
            yield itemsingle

# doublerank spider
class MiaSpiderDouble(scrapy.Spider):
    name = 'miadouble'
    start_urls = ['http://www.piugame.com/piu.xx/leaderboard/xx_double_rank.php']
    custom_settings = {'ITEM_PIPELINES':{'mia.pipelines.MiaDoublePipeline': 300}}
    
    def parse(self, response):
        players = response.xpath('//ul[@class="chart_body score clearfix"]/li')
        for player in players:
            itemdouble = MiaDoubleItem()
            itemdouble['name'] = str(player.xpath('.//span[@class="chart_id"]/text()').get()).strip()
            itemdouble['level'] = str(str(player.xpath('.//div[@class="chart_lv"]/text()').get()).rstrip('\n')).strip()
            itemdouble['region'] = str(player.xpath('.//div[@class="chart_country"]//img/@src').get()).replace('\n','')
            itemdouble['date'] = datetime.datetime.now()
            itemdouble['doublerank'] = str(player.xpath('.//span[@class="rank_out"]/text()').get()).strip()
            itemdouble['dranksymbol'] = str(player.xpath('.//span[@class="updown_info"]//i/@class').get())
            itemdouble['doublechange'] = str(player.xpath('.//span[@class="updown_info"]//text()').get())
            itemdouble['doublescore'] = str(player.xpath('.//div[@class="chart_score"]/text()').get()).replace(',','')
            yield itemdouble

# exprank spider
class MiaSpiderEXP(scrapy.Spider):
    name = 'miaexp'
    start_urls = ['http://www.piugame.com/piu.xx/leaderboard/xx_exp_rank.php']
    custom_settings = {'ITEM_PIPELINES':{'mia.pipelines.MiaEXPPipeline': 300}}
    
    def parse(self, response):
        players = response.xpath('//ul[@class="chart_body score clearfix"]/li')
        for player in players:
            itemexp = MiaEXPItem()
            itemexp['name'] = str(player.xpath('.//span[@class="chart_id"]/text()').get()).strip()
            itemexp['level'] = str(str(player.xpath('.//div[@class="chart_lv"]/text()').get()).rstrip('\n')).strip()
            itemexp['region'] = str(player.xpath('.//div[@class="chart_country"]//img/@src').get()).replace('\n','')
            itemexp['date'] = datetime.datetime.now()
            itemexp['exprank'] = str(player.xpath('.//span[@class="rank_out"]/text()').get()).strip()
            itemexp['expranksymbol'] = str(player.xpath('.//span[@class="updown_info"]//i/@class').get())
            itemexp['expchange'] = str(player.xpath('.//span[@class="updown_info"]//text()').get())
            itemexp['expscore'] = str(player.xpath('.//div[@class="chart_score exp"]/text()').get()).replace(',','')
            yield itemexp