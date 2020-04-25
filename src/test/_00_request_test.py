import requests
import time
millsecond =time.time()
url = 'https://www.okex.me/v2/spot/markets/tickers?t=' + millsecond.__str__()
# Get方式获取网页数据
strhtml = requests.get(url)
print(strhtml.text)

