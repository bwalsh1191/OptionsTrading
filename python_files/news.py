
'''
#this file is used for pulling news about stocks
'''

import json
import requests

def get_news():
    news = requests.get('https://google.com')
    news_json_str = news.content
    news_data = json.loads(news_json_str)
    result = '\n'

    for index in range (0,6):
        title = (((news_data['articles'][index]['title']).encode('utf-8')) + '\n')
        result = result + str(index+1) + ") " + title 
        index+=1
    



