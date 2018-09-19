
'''
#this file is used for pulling stock data for a specific symbol
'''

import requests
import json


#pull a stocks symbol and print various data
def prnt_stock_data(symbol):
    stockAPI = 'https://api.iextrading.com/1.0/stock/market/batch?symbols=' + symbol + '&types=quote&range=1m&last=5'
    stockData = requests.get(stockAPI).json()

    companySymbol = stockData[symbol]['quote']['symbol']
    companyName = stockData[symbol]['quote']['companyName']
    companySector = stockData[symbol]['quote']['sector']
    companyOpen = stockData[symbol]['quote']['open']
    companyMarketCap = stockData[symbol]['quote']['marketCap']
    companyCurrentPrice = stockData[symbol]['quote']['latestPrice']
    companyChange = stockData[symbol]['quote']['change']

    companyDailyVariance = companyCurrentPrice - companyOpen
    companyMarketCap = "{:,}".format(companyMarketCap)

    print ("\n")
    print ("Symbol: " + str(companySymbol))
    print ("Name: " + str(companyName))
    print ("Sector: " + str(companySector))
    print ("Open Price: $" + str(companyOpen))
    print ("Current Price: $" + str(companyCurrentPrice))
    print ("Daily Variance: $" + str(companyDailyVariance))
    print ("Market Cap: $" + str(companyMarketCap))
    print ("Change: $" + str(companyChange))
    print ("\n")

def return_stock_data(symbol):
    stockAPI = 'https://api.iextrading.com/1.0/stock/market/batch?symbols=' + symbol + '&types=quote&range=1m&last=5'
    stockData = requests.get(stockAPI).json()
    companyCurrentPrice = stockData[symbol]['quote']['latestPrice']
    return companyCurrentPrice
