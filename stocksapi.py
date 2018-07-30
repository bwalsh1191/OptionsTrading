
'''
#this file is used for pulling stock data for a specific symbol
'''

from json import dumps
from requests import get
import random
symbol = raw_input("Enter a Symbol: ").upper()

#pull a stocks symbol

stockAPI = 'https://api.iextrading.com/1.0/stock/market/batch?symbols=' + symbol + '&types=quote,news,chart&range=1m&last=5'
stockData = get(stockAPI).json()

companySymbol = stockData[symbol]['quote']['symbol']
companyName = stockData[symbol]['quote']['companyName']
companySector = stockData[symbol]['quote']['sector']
companyOpen = stockData[symbol]['quote']['open']
companyClose= stockData[symbol]['quote']['close']

companyVariance = companyClose - companyOpen
print "\n"
print "Symbol: " + str(companySymbol)
print "Name: " + str(companyName)
print "Sector: " + str(companySector)
print "Open Price" + str(companyOpen)
print "Close Price" + str(companyClose)
print "Variance: " + str(companyVariance) 
print "\n"



'''with open('output.json', 'w') as ofile:
    ofile.write(dumps(sumamry_daily))
ofile.close()
'''
