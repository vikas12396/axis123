#!/usr/bin/env python

import urllib.request
import json
import os
import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['GET'])
def webhook():
	req = request.args.get('q')
	res = processRequest(req)
	return res

def processRequest(q):
	if "news" in q or "news updates" in q or "new stories" in q and "fetch" in q or "get" in q or "tell" in q :
		y = allnews()

	elif '/' in q or '+' in q or '*' in q or '-' in q:
		y = mathsans(q)

	return y

def allnews():
    url = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=5cab5d5971064472bb501bd1d73a7a2d'
    response = requests.get(url)
    r = response.json()
    k = json.dumps(r, indent=4)
    res = json.loads(k)
    i=0
    result = ""
    while i<5:
    	result += str(i)
    	result += res['articles'][i]['title']
    	result += res['articles'][i]['description']
    	result += "........"
    	i=i+1
    return result

def mathsans(q):
	url = 'http://api.mathjs.org/v1/?expr='+q
	p = requests.get(url).text
	return p

if __name__ == '__main__':
    app.run()
