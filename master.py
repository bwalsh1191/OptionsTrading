import stocksapi as stockInfo
import stockTwits
import alyien
import json 
import requests

symbol = raw_input("Enter a stock symbol: ").upper()

stockInfo.get_stock_data(symbol)
stMessages = stockTwits.get_stockTwitsBody(symbol)
stSentiment = stockTwits.get_stockTwitsSentiment(symbol)
#print stMessages
print stSentiment


