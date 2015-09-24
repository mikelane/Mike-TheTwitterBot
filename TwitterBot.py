#!/usr/bin/env python3

"""
Short description

Longer description
"""

__author__ = "Mike Lane"
__copyright__ = "Copyright 2015, Michael Lane"
__license__ = "GPL"
__version__ = "3.0"
__email__ = "mikelane@gmail.com"

import os
from TwitterAPI import TwitterAPI
import nltk


consumer_key = os.environ["MTTB_API_KEY"]
consumer_secret = os.environ["MTTB_API_SECRET"]
access_token_key = os.environ["MTTB_ACCESS_TOKEN"]
access_token_secret = os.environ["MTTB_ACCESS_TOKEN_SECRET"]

api = TwitterAPI(
    consumer_key,
    consumer_secret,
    access_token_key,
    access_token_secret
)

# r = api.request('statuses/update', {'status':'Tweeting from python!'})
# print(r.text)
