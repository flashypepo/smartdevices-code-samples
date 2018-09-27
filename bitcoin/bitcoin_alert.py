"""
Bitcoin alert
- retrieves bitcoin-price and, in future, alert me by some means.

pre-condition: device connected to the internet.

Based upon: https://www.hackster.io/rahulkumarsingh/crypto-alert-system-using-bolt-iot-d62df1
2018-0829 PePo new, desktop version. College 4 example.
 Usage: execute from Terminal, after prompt $:
    $ python3 bitcoin-alert
     (Ctrl-C to stop program)
"""
try:
    import urequests as requests
except:
    import requests

import json
import time

# 2017-1230 add local time
import datetime

# confgurations
BITCOIN_PRICES_URL = "https://min-api.cryptocompare.com/data/price"
BITCOIN_STORAGE = "bitcoinprices.txt"

def gettoday():
    today = datetime.datetime.today()
    # convert the ISO8601 string to a datetime object
    return today.strftime("%d.%m.%Y,%H:%M:%S")

# API: https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR,USD
def price_check():
    url = BITCOIN_PRICES_URL
    querystring = "?fsym=BTC&tsyms=EUR,USD"
    response = requests.get(url + querystring)
    response = json.loads(response.text)
    euro_price = response['EUR']
    usd_price = response['USD']
    return euro_price, usd_price

# save record in filename, returns number of written-chars
def saverecord(record,filename=BITCOIN_STORAGE):
    with open(filename, 'a') as f:
        nr = f.write(record+'\n')
        f.closed
    return nr

# execute getting bitcoin prices and store it in file
# default time interval: 30 seconds
def run(dt=30):
    while True:
        market_europrice, market_usdprice = price_check()
        #print ("Market price is euro", market_europrice, ", usd", market_usdprice)

        #''' add local time
        today = gettoday()
        print ("{0}: Market price is €{1:7.2f} (${2:7.2f})".format(today, market_europrice,market_usdprice))

        # save record
        record = ("{0},Market,{1:7.2f},{2:7.2f}".format(today, market_europrice,market_usdprice))
        nr = saverecord (record)
        print("Written to file {0} characters".format(nr))

        # wait before getting next data
        time.sleep(dt)

#get bitcoin-price every 10 minutes
try:
    run(600) # 10 minutes
except Exception as e:
    print("Interrupted: exception=", e)
    #pass
