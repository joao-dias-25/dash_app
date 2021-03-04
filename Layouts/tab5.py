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


df2 = Api.df_mk


layout = html.Div(
            id='table-paging-ratio-graph-container'
                                                )

@app.callback(Output('table-paging-ratio-graph-container', "children"),
        [Input('time-drop', 'value')
        , Input('coin-drop', 'value')
        ])

def update_graph(time,lista):
    if str == type(time):
        df = df2

    else:
        df = df2.tail(time)

    coins = lista
    coins = [x for x in coins if (x != 'bitcoin' and x !='ethereum')]


    fig = make_subplots(rows=1, cols=2, subplot_titles=['Ratios against BTC', 'Ratios against ETH'])

    # Add traces
    fig.add_trace(go.Scatter(x=df.index, y=df['ethereum']/df['bitcoin'],
                             mode='lines',
                             name='ratio eth/btc'), row=1, col=1)

    for coin in coins:
        fig.add_trace(go.Scatter(x=df.index, y=df[f'{coin}']/df['ethereum'],
                             mode='lines',
                             name=f'ratio {coin}/eth'), row=1, col=2)



    return html.Div(dcc.Graph(
                  id='example-graph',
                  figure=fig))