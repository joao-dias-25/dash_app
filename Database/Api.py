import dash_bootstrap_components as dbc
import pandas as pd
from dash.dependencies import Input, Output

import urllib3
from urllib3 import request

# to handle certificate verification
import certifi

# to manage json data
import json
#import requests


# handle certificate verification and SSL warnings:
# reference https://urllib3.readthedocs.io/en/latest/user-guide.html#ssl
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())

# get data from the API; replace url with target source
url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=max&interval=daily'
r = http.request('GET', url)

# decode json data into a dict object
data = json.loads(r.data.decode('utf-8'))

df1 = pd.DataFrame(data['prices'], columns=['time', 'price'])
df2=pd.DataFrame(data['total_volumes'], columns=['time', 'volume'])
df3=pd.DataFrame(data['market_caps'], columns=['time', 'marketcap'])
df = df1.merge(df2,on='time').merge(df3,on='time')
df['time']= pd.to_datetime(df['time'], unit='ms')
df.set_index('time', inplace=True)