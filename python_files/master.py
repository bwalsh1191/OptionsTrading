import stocksApi as stockInfo
import stockTwits
import alyien
import json 
import requests, time
from datetime import datetime



#symbol = input("Enter a stock symbol: ").upper()


while True:

    symbols = ["AAPL", 'AMD','TSLA']
    sleep_time = 0
    num_of_week = datetime.today().weekday()

    if datetime.today().replace(hour=8, minute=30, second=0, microsecond=0) <= datetime.now() <= datetime.today().replace(hour=17, minute=30, second=0, microsecond=0)and num_of_week <= 4: 
        sleep_time = 60
    else: 
        sleep_time = 600

    for x in range(2):
        stockInfo.get_stock_data(symbols[x])
        stockTwits.get_stockTwitsBody(symbols[x])
        stockTwits.get_stockTwitsSentiment(symbols[x])
   
    time.sleep(sleep_time)


