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
    return "Hello world"



if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

#    print "Starting app on port %d" % port
    app.run(debug=False, port=port, host='0.0.0.0')
