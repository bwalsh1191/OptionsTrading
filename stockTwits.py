
'''
#this file is used for pulling stock data for a specific symbol using the stockTwits API
edit
'''

import json
import requests


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

    
    for index in range (0,len(stockTwits_data['messages'])):
        sent= str(stockTwits_data['messages'][index]['entities']['sentiment'])
        if(sent == "{'basic': 'Bullish'}"):
            posSent = posSent +1

        if(sent == "{'basic': 'Bearish'}"):
            negSent = negSent -1
        index+=1
    totalSentiment = posSent + negSent
    print("The total Positive Sentiment is " + str(posSent) + ". The total Negative Sentiment is " + str(negSent)
    + ". Combined Sentiment Score is: " + str(totalSentiment) + '\n')
