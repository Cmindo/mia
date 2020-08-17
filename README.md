# About
Mia is a python script that scrapes player data for the arcade game "Pump it Up" (via Scrapy), stores desired results in MongoDB Cloud Atlas, then pushes the daily resutls to the Pump it Up (Canada) discord server on a daily basis.

Mia scrapes player data from four (4) webpages, where each webpage details an attribute of the player and their respective ranking in the world:
1. Total Rank - http://www.piugame.com/piu.xx/leaderboard/xx_total_rank.php
2. Single-mode Rank - http://www.piugame.com/piu.xx/leaderboard/xx_single_rank.php
3. Double-mode Rank - http://www.piugame.com/piu.xx/leaderboard/xx_double_rank.php
4. EXP Rank - http://www.piugame.com/piu.xx/leaderboard/xx_exp_rank.php

# Spider

There are a total of four (4) spiders for each attribute. Fortunately, these webpages are identical so parsing through remaining webpages was seamless once the initial spider worked as intended.

Aside from scraping player data, the spider has two important objectives:
1. Ensure scraped data was cleansed before sending to pipeline
2. Construct a schema for our MongoDB Database

```
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
```
The spider scrapes the following elements for each player then compiles it to `itemtotal`, which is then sent to the pipeline:
1. `name` - Name of the player (string)
2. `level` - The level of the player (string)
3. `region` - An image name representing the region of the player (string)
4. `date` - Current datetime scraped data (datetime)
5. `totalrank` - The rank of the player (int)
6. `tranksymbol` - An image element (up or down arrow) to indicate the directional change on the current day (string)
7. `totalchange` - How many ranks the player moved up/down by on the current day (int)
8. `totalscore` - The player's cumulative total score (int)

# Pipeline

The objective of the pipeline is to 1) further process the data, and 2) send results to MongoDB Cloud Atlas:

Data Processing:
- 

However, since we are only interested in Canadian players, we must drop scraped results where `itemtotal['region']` is not 

WIP

