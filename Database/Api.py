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


coins=['bitcoin','ethereum','cardano','binancecoin','polkadot','monero']
stablecoins=['tether','usd-coin', 'binance-usd','dai','paxos-standard','husd', 'ampleforth']
coins_data={}
stablecoins_data={}

for coin in coins:
    # get data from the API; replace url with target source
    url = f'https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency=usd&days=max&interval=daily'
    r = http.request('GET', url)
    # decode json data into a dict object
    data = json.loads(r.data.decode('utf-8'))
    coins_data.update({coin: data})

for coin in stablecoins:
    # get data from the API; replace url with target source
    url = f'https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency=usd&days=max&interval=daily'
    r = http.request('GET', url)
    # decode json data into a dict object
    data = json.loads(r.data.decode('utf-8'))
    stablecoins_data.update({coin: data})



def merge_data(moedas):
    df=pd.DataFrame(coins_data[moedas[0]]['market_caps'], columns=['time', 'marketcap_bitcoin'])
    for moeda in moedas[1::]:
        df1=pd.DataFrame(coins_data[moeda]['market_caps'], columns=['time', f'marketcap_{moeda}'])
        df=df.merge(df1,on='time', how='left')
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    df.set_index('time', inplace=True)
    return df
df = merge_data(coins)

df['combine_mk']=df.sum(axis=1)
df['ratio_eth_btc']= df['marketcap_ethereum']/df['marketcap_bitcoin']
df['ratio_ada_eth']= df['marketcap_cardano']/df['marketcap_ethereum']
df['ratio_xmr_eth']= df['marketcap_monero']/df['marketcap_ethereum']

def merge_inf(moedas):
    coins_inf = {}
    for moeda in moedas:
        url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={moeda}&order=market_cap_desc&per_page=100&page=1&sparkline=false'
        r = http.request('GET', url)

        # decode json data into a dict object
        data = json.loads(r.data.decode('utf-8'))
        coins_inf.update({moeda: data})
    df_info = pd.json_normalize(coins_inf, record_path=moedas[0])
    for moeda in moedas[1::]:
        df1 = pd.json_normalize(coins_inf, record_path=moeda)
        df_info = df_info.append(df1)
    return df_info

coin_info=merge_inf(coins)
stablecoins_info= merge_inf(stablecoins)

def merge_vol(moedas, data):
    df=pd.DataFrame(data[moedas[0]]['total_volumes'], columns=['time', f'volume_{moedas[0]}'])
    for moeda in moedas[1::]:
        df1=pd.DataFrame(data[moeda]['total_volumes'], columns=['time', f'volume_{moeda}'])
        df=df.merge(df1,on='time', how='left')
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    df.set_index('time', inplace=True)
    return df

df_vol=merge_vol(coins, coins_data)
dfstable_vol=merge_vol(stablecoins, stablecoins_data)