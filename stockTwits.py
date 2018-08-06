
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
    #totalSentiment = 0
    result = '\n'

    
    for index in range (0,len(stockTwits_data['messages'])):
        message= (((stockTwits_data['messages'][index]['body']).encode('utf-8')) + '\n')
        result = result + str(index+1) + ". " + message
        index+=1
    return result
    '''
    for index in range (0,len(stockTwits_data['messages'])):
        message= (stockTwits_data['messages'][index]['entities']['sentiment']) + '\n'
        result = message
    return result
        
    
    for index in range (0,len(stockTwits_data['messages'])):
        sentiment= (stockTwits_data['messages'][index]['entities']['sentiment'])
        if sentiment  "u'basic': u'Bullish'}":
            totalSentiment = totalSentiment -1
        elif sentiment == "u'Bullish":
            totalSentiment = totalSentiment +1
        print sentiment
    return totalSentiment
'''

def get_stockTwitsSentiment(symbol):
    stockTwits = requests.get('https://api.stocktwits.com/api/2/streams/symbol/' + symbol + '.json')
    stockTwits_json_str = stockTwits.content
    stockTwits_data = json.loads(stockTwits_json_str)
    sentiment = '\n'

    
    for index in range (0,len(stockTwits_data['messages'])):
        message= (str(stockTwits_data['messages'][index]['entities']['sentiment']).encode('utf-8')) + '\n'
        sentiment = sentiment + str(index+1) + ". " + message
        index+=1
    return sentiment
