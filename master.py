import stocksapi as stockInfo
import stockTwits
import alyien
import json 
import requests
import Flask



#symbol = raw_input("Enter a stock symbol: ").upper()

#stockInfo.get_stock_data(symbol)
#stMessages = stockTwits.get_stockTwitsBody(symbol)
#stSentiment = stockTwits.get_stockTwitsSentiment(symbol)
#print stMessages
#print stSentiment
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

