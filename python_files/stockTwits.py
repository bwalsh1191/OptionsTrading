
'''
#this file is used for pulling stock data for a specific symbol using the stockTwits API
edit
'''

import json
import requests
import time, datetime


def get_stockTwitsBody(symbol):
    stockTwits = requests.get('https://api.stocktwits.com/api/2/streams/symbol/' + symbol + '.json')
    stockTwits_json_str = stockTwits.content
    stockTwits_data = json.loads(stockTwits_json_str)
    result = '\n'

    
    for index in range (0,len(stockTwits_data['messages'])):
        message= ((stockTwits_data['messages'][index]['body']) + '\n')
        result = result + str(index+1) + ". " + message
        index+=1
    print(result)


def get_stockTwitsSentiment(symbol):
    stockTwits = requests.get('https://api.stocktwits.com/api/2/streams/symbol/' + symbol + '.json')
    stockTwits_json_str = stockTwits.content
    stockTwits_data = json.loads(stockTwits_json_str)
    totalSentiment = 0
    posSent = 0
    negSent = 0
    sentRatio = 0

    
    for index in range (0,len(stockTwits_data['messages'])):
        sent= str(stockTwits_data['messages'][index]['entities']['sentiment'])
        if(sent == "{'basic': 'Bullish'}"):
            posSent = posSent +1

        if(sent == "{'basic': 'Bearish'}"):
            negSent = negSent -1
        index+=1
    totalSentiment = posSent + negSent
    sentRatio = int((totalSentiment/len(stockTwits_data['messages']))*(100))
    print("The total Positive Sentiment is " + str(posSent) + ". The total Negative Sentiment is " + str(negSent)
    + ". Combined Sentiment Score is: " + str(totalSentiment) + " with a ratio sentiment ratio of: " + str(sentRatio) + "%" + '\n')

    
    #MAKE THIS CLEANER SO THE TWO FILES ARE SEPERATE
    stockAPI = 'https://api.iextrading.com/1.0/stock/market/batch?symbols=' + symbol + '&types=quote&range=1m&last=5'
    stockData = requests.get(stockAPI).json()
    companyCurrentPrice = stockData[symbol]['quote']['latestPrice']


    #output is used to store all the sentiment ratio and data  
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    output = [st, symbol,posSent, negSent, totalSentiment, sentRatio,companyCurrentPrice]





    #writing this data to a file to make a running record of the data sentiment bsaed on the symbol passed
    file_name = symbol + "_sentiment.txt"
    f = open("/Users/brian/Development/stock_env/OptionsTrading/stock__files/" + file_name, "a")
    f.write(str(output) + '\n')
