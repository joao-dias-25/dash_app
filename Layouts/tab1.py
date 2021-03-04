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

# import dataframe
from Database import Api



stablecoins=Api.stablecoins


df2 = Api.df_mk
df_s2 = Api.dfs_mk


layout = html.Div(
            id='table-paging-with-graph-container',
            #className="five columns"
        )

@app.callback(Output('table-paging-with-graph-container', "children"),
        [Input('time-drop', 'value')
        , Input('coin-drop', 'value')
        ])
def update_graph(time,lista):
    if str == type(time):
        df = df2
        df_s = df_s2
    else:
        df = df2.tail(time)
        df_s = df_s2.tail(time)

    coins = lista
    fig = make_subplots(rows=1, cols=2, subplot_titles=[f'Total Marketcap ({len(coins)}coins selected)',
                                                    f'Total Marketcap (Top {len(stablecoins)} Stablecoins)'])
    # Add traces

    for coin in coins:
        fig.add_trace(go.Scatter(x=df.index, y=df[f'{coin}'],
                             mode='lines',
                             name= coin), row=1, col=1)

    fig.add_trace(go.Scatter(x=df.index, y=df[coins].sum(axis=1),
                             mode='lines',
                             name='combine_market_cap'), row=1, col=1)

    for stablecoin in stablecoins:
        fig.add_trace(go.Scatter(x=df_s.index, y=df_s[f'{stablecoin}'],
                             mode='lines',
                             name= stablecoin), row=1, col=2)

    fig.add_trace(go.Scatter(x=df_s.index, y=df_s.sum(axis=1),
                             mode='lines',
                             name='stablecoins_market_cap'), row=1, col=2)

    return html.Div(dcc.Graph(
                  id='meu-graph',
                  figure=fig))


