import stocksapi as stockInfo
import stockTwits
import alyien
import json 
import requests, time



symbol = input("Enter a stock symbol: ").upper()

while True: 
#runs this code every 60 seconds to constantly update
    stockInfo.get_stock_data(symbol)
    stockTwits.get_stockTwitsBody(symbol)
    stockTwits.get_stockTwitsSentiment(symbol)

    time.sleep(60)



