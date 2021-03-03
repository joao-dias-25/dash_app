import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
from dash.dependencies import Input, Output
from app import app
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# import dataframe
from Database import Api

coins= Api.coins
df = Api.merge_data(coins,'max')

df['ratio_eth_btc']= df['marketcap_ethereum']/df['marketcap_bitcoin']
df['ratio_ada_eth']= df['marketcap_cardano']/df['marketcap_ethereum']
df['ratio_xmr_eth']= df['marketcap_monero']/df['marketcap_ethereum']
df['ratio_bnb_eth']= df['marketcap_binancecoin']/df['marketcap_ethereum']


fig = make_subplots(rows=1, cols=2, subplot_titles=['Ratios against BTC', 'Ratios against ETH'])

# Add traces
fig.add_trace(go.Scatter(x=df.index, y=df['ratio_eth_btc'],
                             mode='lines',
                             name='ratio eth/btc'), row=1, col=1)
fig.add_trace(go.Scatter(x=df.index, y=df['ratio_ada_eth'],
                             mode='lines',
                             name='ratio ada/eth'), row=1, col=2)
fig.add_trace(go.Scatter(x=df.index, y=df['ratio_xmr_eth'],
                             mode='lines',
                             name='ratio xmr/eth'), row=1, col=2)
fig.add_trace(go.Scatter(x=df.index, y=df['ratio_bnb_eth'],
                             mode='lines',
                             name='ratio bnb/eth'), row=1, col=2)

layout = html.Div(dcc.Graph(
                  id='example-graph',
                  figure=fig))