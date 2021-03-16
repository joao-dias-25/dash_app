import pandas as pd
import urllib3
from urllib3 import request

# to handle certificate verification
import certifi

# to manage json data
import json
#import requests
import os
from os import environ


# handle certificate verification and SSL warnings:
# reference https://urllib3.readthedocs.io/en/latest/user-guide.html#ssl
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())



def rank_inf(order,limit):
    url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order={order}&per_page={limit}&page=1&sparkline=false'
    r = http.request('GET', url)

    # decode json data into a dict object
    data = json.loads(r.data)
    df_info = pd.json_normalize(data)
    return df_info

def rank_messari():
    url = 'https://data.messari.io/api/v1/assets?fields=id,slug,symbol,metrics/market_data/price_usd'
    r = http.request('GET', url)

    # decode json data into a dict object
    data = json.loads(r.data)
    df_info = pd.json_normalize(data, record_path='data')
    return df_info.slug.tolist()


df_rank=rank_inf('gecko_desc',10)


stablecoins = ['tether','usd-coin', 'binance-usd','dai','paxos-standard','husd', 'ampleforth']
btc_tokens = ['wrapped-bitcoin','renbtc','huobi-btc','sbtc','tbtc']
coins = [item for item in df_rank.id.tolist() if item not in (stablecoins + btc_tokens)]


def merge_data(moedas, days):
    coins_data = {}
    #retrive information from Api
    for coin in moedas:
        # get data from the API; replace url with target source
        url = f'https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency=usd&days={days}&interval=daily'
        r = http.request('GET', url)
        # decode json data into a dict object
        data = json.loads(r.data)#.decode('utf-8'))
        coins_data.update({coin: data})
    df=pd.DataFrame(coins_data[moedas[0]]['market_caps'], columns=['time', f'mk_{moedas[0]}'])
    for moeda in moedas[1::]:
        df1=pd.DataFrame(coins_data[moeda]['market_caps'], columns=['time', f'mk_{moeda}'])
        df=df.merge(df1,on='time', how='left')
    for moeda in moedas:
        df1=pd.DataFrame(coins_data[moeda]['total_volumes'], columns=['time', f'volume_{moeda}'])
        df=df.merge(df1,on='time', how='left')
    for moeda in moedas:
        df1=pd.DataFrame(coins_data[moeda]['prices'], columns=['time', f'{moeda}'])
        df=df.merge(df1,on='time', how='left')
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    df.set_index('time', inplace=True)

    return df

df_mk=merge_data(coins,'max')
dfs_mk=merge_data(stablecoins,'max')


def merge_inf(moedas):
    coins_inf = {}
    for moeda in moedas:
        url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={moeda}&order=market_cap_desc&per_page=100&page=1&sparkline=false'
        r = http.request('GET', url)

        # decode json data into a dict object
        data = json.loads(r.data)#.decode('utf-8'))
        coins_inf.update({moeda: data})
    df_info = pd.json_normalize(coins_inf, record_path=moedas[0])
    for moeda in moedas[1::]:
        df1 = pd.json_normalize(coins_inf, record_path=moeda)
        df_info = df_info.append(df1)
    return df_info

df_i=merge_inf(coins)
dfs_i=merge_inf(stablecoins)
df_btctokens=merge_inf(btc_tokens)


# nodes of number of nodes
def nodes_btc():
    url = 'https://bitnodes.io/api/v1/snapshots/'
    r = http.request('GET', url)
    data = json.loads(r.data)
    nodes=pd.json_normalize(data, record_path='results')
    nodes['date'] = pd.to_datetime(nodes['timestamp'], unit='s')
    nodes.set_index('date', inplace=True)
    return nodes

dfnodes_count = nodes_btc()

def nodes_coordenates():
    url = f'https://bitnodes.io/api/v1/snapshots/{dfnodes_count.timestamp[0]}/'
    r = http.request('GET', url)

    # decode json data into a dict object
    data = json.loads(r.data)
    df = pd.DataFrame.from_dict(data['nodes'],
                                orient='index',
                                dtype=None,
                                columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'])
    return df

dfnodes = nodes_coordenates()

def nodes_eth():
    url = 'https://api.etherscan.io/api?module=stats&action=nodecount&apikey=YourApiKeyToken'
    r = http.request('GET', url)
    data = json.loads(r.data)
    df=pd.DataFrame.from_dict(data)
    return df.result

def btc_stats():
    url = 'https://api.blockchain.info/stats'
    r = http.request('GET', url)

    # decode json data into a dict object
    data = json.loads(r.data)
    df = pd.DataFrame.from_dict(data,orient='index',columns=['bitcoin stats']).reset_index()
    return df

def secret_api():
    CONSUMER_KEY = environ['TEST_API_KEY']
    url = f'https://data-api.defipulse.com/api/v1/egs/api/ethgasAPI.json?api-key={CONSUMER_KEY}'
    r = http.request('GET', url)
    # decode json data into a dict object
    data = json.loads(r.data)
    df = pd.DataFrame.from_dict(data, orient='index', columns=['Ethereum Gas inf'])
    df = df.reset_index()
    df=df.drop(df.index[11])
    return df
