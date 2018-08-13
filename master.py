import stocksapi as stockInfo
import stockTwits
import alyien
import json 
import requests



symbol = input("Enter a stock symbol: ").upper()

stockInfo.get_stock_data(symbol)
stockTwits.get_stockTwitsBody(symbol)
stockTwits.get_stockTwitsSentiment(symbol)



