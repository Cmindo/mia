import pymongo
import dns

from scrapy.conf import settings
from scrapy.exceptions import DropItem

# totalrank logic
class MiaTotalPipeline(object):

    canada = ['/piu.countryImg/031.png']
    up = ['fa fa-caret-up']
    down = ['fa fa-caret-down']
    Lvtext = ['-']
    toint = ['test']
    blank = [' ']

    def process_item(self, itemtotal, spider):
        for data in self.toint:
            if data not in itemtotal['totalscore']:
                itemtotal['totalscore'] = int(itemtotal['totalscore'])
            if data not in itemtotal['totalrank']:
                itemtotal['totalrank'] = int(itemtotal['totalrank'])
        for data in self.canada:
            if data not in itemtotal['region']:
                raise DropItem("Not Canadian")
        for data in self.Lvtext:
            if data in itemtotal['totalchange']:
                itemtotal['totalchange'] = None
        for data in self.up:
            if data in itemtotal['tranksymbol']:
                symbolup = "+"
                itemtotal['totalchange'] = symbolup+itemtotal['totalchange']
        for data in self.down:    
            if data in itemtotal['tranksymbol']:
                symboldown = "-"
                itemtotal['totalchange'] = symboldown+itemtotal['totalchange']
        else:
            connection = pymongo.MongoClient("mongodb+srv://piucanada:prima123@piucanada-frwhn.azure.mongodb.net/test?retryWrites=true")
            self.collection = connection.piucanada.totalrank
            self.collection.insert(itemtotal)
            self.collection = connection.piucanada.totalrankhistory
            self.collection.insert(itemtotal)
            return itemtotal

# singlerank logic
class MiaSinglePipeline(object):

    canada = ['/piu.countryImg/031.png']
    up = ['fa fa-caret-up']
    down = ['fa fa-caret-down']
    Lvtext = ['-']
    toint = ['test']
    blank = [' ']

    def process_item(self, itemsingle, spider):
        for data in self.toint:
            if data not in itemsingle['singlescore']:
                itemsingle['singlescore'] = int(itemsingle['singlescore'])
            if data not in itemsingle['singlerank']:
                itemsingle['singlerank'] = int(itemsingle['singlerank'])
        for data in self.canada:
            if data not in itemsingle['region']:
                raise DropItem("Not Canadian")
        for data in self.Lvtext:
            if data in itemsingle['singlechange']:
                itemsingle['singlechange'] = None
        for data in self.up:
            if data in itemsingle['sranksymbol']:
                symbolup = "+"
                itemsingle['singlechange'] = symbolup+itemsingle['singlechange']
        for data in self.down:    
            if data in itemsingle['sranksymbol']:
                symboldown = "-"
                itemsingle['singlechange'] = symboldown+itemsingle['singlechange']
        else:
            connection = pymongo.MongoClient("mongodb+srv://piucanada:prima123@piucanada-frwhn.azure.mongodb.net/test?retryWrites=true")
            self.collection = connection.piucanada.singlerank
            self.collection.insert(itemsingle)
            self.collection = connection.piucanada.singlerankhistory
            self.collection.insert(itemsingle)
            return itemsingle

# doublerank logic
class MiaDoublePipeline(object):

    canada = ['/piu.countryImg/031.png']
    up = ['fa fa-caret-up']
    down = ['fa fa-caret-down']
    Lvtext = ['-']
    toint = ['test']

    def process_item(self, itemdouble, spider):
        for data in self.toint:
            if data not in itemdouble['doublescore']:
                itemdouble['doublescore'] = int(itemdouble['doublescore'])
            if data not in itemdouble['doublerank']:
                itemdouble['doublerank'] = int(itemdouble['doublerank'])
        for data in self.canada:
            if data not in itemdouble['region']:
                raise DropItem("Not Canadian")
        for data in self.Lvtext:
            if data in itemdouble['doublechange']:
                itemdouble['doublechange'] = None
        for data in self.up:
            if data in itemdouble['dranksymbol']:
                symbolup = "+"
                itemdouble['doublechange'] = symbolup+itemdouble['doublechange']
        for data in self.down:    
            if data in itemdouble['dranksymbol']:
                symboldown = "-"
                itemdouble['doublechange'] = symboldown+itemdouble['doublechange']
        else:
            connection = pymongo.MongoClient("mongodb+srv://piucanada:prima123@piucanada-frwhn.azure.mongodb.net/test?retryWrites=true")
            self.collection = connection.piucanada.doublerank
            self.collection.insert(itemdouble)
            self.collection = connection.piucanada.doublerankhistory
            self.collection.insert(itemdouble)
            return itemdouble

# exprank logic
class MiaEXPPipeline(object):

    canada = ['/piu.countryImg/031.png']
    up = ['fa fa-caret-up']
    down = ['fa fa-caret-down']
    Lvtext = ['-']
    toint = ['test']

    def process_item(self, itemexp, spider):
        for data in self.toint:
            if data not in itemexp['expscore']:
                itemexp['expscore'] = int(itemexp['expscore'])
            if data not in itemexp['exprank']:
                itemexp['exprank'] = int(itemexp['exprank'])
        for data in self.canada:
            if data not in itemexp['region']:
                raise DropItem("Not Canadian")
        for data in self.Lvtext:
            if data in itemexp['expchange']:
                itemexp['expchange'] = None
        for data in self.up:
            if data in itemexp['expranksymbol']:
                symbolup = "+"
                itemexp['expchange'] = symbolup+itemexp['expchange']
        for data in self.down:    
            if data in itemexp['expranksymbol']:
                symboldown = "-"
                itemexp['expchange'] = symboldown+itemexp['expchange']
        else:
            connection = pymongo.MongoClient("mongodb+srv://piucanada:prima123@piucanada-frwhn.azure.mongodb.net/test?retryWrites=true")
            self.collection = connection.piucanada.exprank
            self.collection.insert(itemexp)
            self.collection = connection.piucanada.exprankhistory
            self.collection.insert(itemexp)
            return itemexp