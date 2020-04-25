import json
#对象创建
class Market:
    def __init__(self,coinId,symbol,iconPath,currency):
        self.coinId = coinId
        self.symbol = symbol
        self.iconPath = iconPath
        self.currency = currency

market = Market(1,2,3,4);

#对象先传字典
myClassDict = market.__dict__
myClassJson = json.dumps(myClassDict)
print(market.iconPath)
print(myClassJson)

