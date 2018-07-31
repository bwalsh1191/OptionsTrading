'''

import json
import urllib
import requests

APPLICATION_ID = 'f416731b'
APPLICATION_KEY = 'bb711c92b4c7fb19c07a31cf85cb1f4d'

def call_api(endpoint, parameters):
  url = 'https://api.aylien.com/api/v1/' + endpoint
  headers = {
      "Accept":                             "application/json",
      "Content-type":                       "application/x-www-form-urlencoded",
      "X-AYLIEN-TextAPI-Application-ID":    APPLICATION_ID,
      "X-AYLIEN-TextAPI-Application-Key":   APPLICATION_KEY
      
  }
  
  

POST https://eastus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment HTTP/1.1
Host: eastus.api.cognitive.microsoft.com
Ocp-Apim-Subscription-Key: 123456

{
  "documents": [
    {
      "language": "en",
      "id": "1",
      "text": "Hello world. This is some input text that I love."
    },
   
  ]
}
'''