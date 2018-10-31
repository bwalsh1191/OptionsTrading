
'''
#this file is used for pulling stock data for a specific symbol using the stockTwits API
edit
'''

import json
import requests
import time, datetime
import date, stocksApi

#get all the messages from StockTwits for a given stock symbol
def get_stockTwitsBody(symbol):
    stockTwits = requests.get('https://api.stocktwits.com/api/2/streams/symbol/' + symbol + '.json')
    stockTwits_json_str = stockTwits.content
    stockTwits_data = json.loads(stockTwits_json_str)
    result = '\n'

    
    for index in range (0,30):
        message = ((stockTwits_data['messages'][index]['body']) + '\n')
        result = result + str(index+1) + ". " + message
        index+=1
    print(result)

#get all the sentiment scores from StockTwits
def get_stockTwitsSentiment(symbol):
    stockTwits = requests.get('https://api.stocktwits.com/api/2/streams/symbol/' + symbol + '.json')
    stockTwits_json_str = stockTwits.content
    stockTwits_data = json.loads(stockTwits_json_str)
    totalSentiment = 0
    posSent = 0
    negSent = 0
    sentRatio = 0

    #Calculating the sentiment score from stocktwits

    for index in range (0,30):
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
    

    #get the rest of the data for the files to write
    companyCurrentPrice = stocksApi.return_stock_data(symbol)
    time_stamp = date.getTimeStamp()
    day_of_week = date.getDayofWeek()
    
    #writing this data to a file to make a running record of the data sentiment bsaed on the symbol passed
    output = [time_stamp, day_of_week, symbol, posSent, negSent, totalSentiment, sentRatio, companyCurrentPrice]
    file_name = symbol.lower() + "_sentiment.txt"
    f = open("/Users/brian/Development/stock_env/OptionsTrading/stock__files/" + file_name, "a")
    f.write(str(output) + '\n')

    
'''
#write the data to the files
def write_file(symbol, posSent, negSent, totalSentiment, sentRatio):
    companyCurrentPrice = stocksApi.return_stock_data(symbol)
    time_stamp = date.getTimeStamp()
    day_of_week = date.getDayofWeek()
    output = [time_stamp, day_of_week, symbol, posSent, negSent, totalSentiment, sentRatio, companyCurrentPrice]
    file_name = symbol.lower() + "_sentiment.txt"
    f = open("/Users/brian/Development/stock_env/OptionsTrading/stock__files/" + file_name, "a")
    f.write(str(output) + '\n')

'''