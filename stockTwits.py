
'''
#this file is used for pulling stock data for a specific symbol
'''

import json
import requests

def get_stockTwits(symbol):
    stockTwits = requests.get('https://api.stocktwits.com/api/2/streams/symbol/' + symbol + '.json')
    stockTwits_json_str = stockTwits.content
    stockTwits_data = json.loads(stockTwits_json_str)
    result = '\n'

    for index in range (0,10):
        message= (((stockTwits_data['messages'][index]['body']).encode('utf-8')) + '\n')
        result = result + str(index+1) + ". " + message
        index+=1
    return result
    



#stockTwits = 'https://api.stocktwits.com/api/2/streams/symbol/' + symbol + '.json'