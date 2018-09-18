'''
this file is used for pulling stock data for a specific symbol using the alpha vantage API
'''

import json
import requests
import time, datetime

api_key = '4HNDQOUQ2A1G90RW'
symbol = 'AAPL'


#def get_alphaVantage(symbol):
alphaVantage = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=' + symbol + '&apikey=' + api_key)
alphaVantage_json_str = alphaVantage.content
alphaVantage_data = json.loads(alphaVantage_json_str)
result = '\n'

'''   
for index in range (0,len(alphaVantage_data['Monthly Time Series'])):
    message= ((alphaVantage_data['messages'][index]['body']) + '\n')
    result = result + str(index+1) + ". " + message
    index+=1
print(result)

'''
#this is a pain in the ass
print(alphaVantage_data['Monthly Time Series']['2018-09-14']['1. open'])

