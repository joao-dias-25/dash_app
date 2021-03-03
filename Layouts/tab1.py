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

coins=Api.coins

stablecoins=Api.stablecoins

df = Api.merge_data(coins,'max')
df_s = Api.merge_data(stablecoins,'max')


fig = make_subplots(rows=1, cols=2, subplot_titles=[f'Coins total Marketcap (Top {len(coins)})',
                                                    f'Stablecoins total Marketcap (Top {len(stablecoins)})'])
# Add traces

for coin in coins:
    fig.add_trace(go.Scatter(x=df.index, y=df[f'marketcap_{coin}'],
                             mode='lines',
                             name= coin), row=1, col=1)

fig.add_trace(go.Scatter(x=df.index, y=df['combine_mk'],
                             mode='lines',
                             name='combine_market_cap'), row=1, col=1)

for coin in stablecoins:
    fig.add_trace(go.Scatter(x=df_s.index, y=df_s[f'marketcap_{coin}'],
                             mode='lines',
                             name= coin), row=1, col=2)

fig.add_trace(go.Scatter(x=df_s.index, y=df_s['combine_mk'],
                             mode='lines',
                             name='stablecoins_market_cap'), row=1, col=2)

layout = html.Div(dcc.Graph(
                  id='example-graph',
                  figure=fig))