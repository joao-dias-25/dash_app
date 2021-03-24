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


df2 = Api.df_mk
dfi = Api.df_i


layout = html.Div(id='container')

@app.callback(Output('container', "children"),
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
    fig.add_trace(go.Scatter(x=df.index, y=df['mk_ethereum'] / df['mk_bitcoin'],
                             mode='lines',
                             name='ratio Ethereum/Bitcoin'), row=1, col=1)
    for coin in coins:
        fig.add_trace(go.Scatter(x=df.index, y=df[f'mk_{coin}']/df['mk_bitcoin'],
                             mode='lines',
                             name=f'ratio {coin}/btc'), row=1, col=1)

    for coin in coins:
        fig.add_trace(go.Scatter(x=df.index, y=df[f'mk_{coin}']/df['mk_ethereum'],
                             mode='lines',
                             name=f'ratio {coin}/eth'), row=1, col=2)

    # Add image
    fig.add_layout_image(
        dict(
            source="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/1024px-Bitcoin.svg.png",
            xref="paper",
            yref="paper",
            x=0.05,
            y=1,
            sizex=1,
            sizey=1,
            # sizing="stretch",
            opacity=0.5,
            layer="below"),

    )
    fig.add_layout_image(
        dict(
            source="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Ethereum_logo_2014.svg/1200px-Ethereum_logo_2014.svg.png",
            xref="paper",
            yref="paper",
            x=0.7,
            y=1,
            sizex=1,
            sizey=1,
            # sizing="stretch",
            opacity=0.5,
            layer="below"),

    )

    fig.update_layout(template="simple_white")



    return html.Div([dbc.Row([dbc.Col([
                dcc.Dropdown(id='order-drop'
                       , options=[
                {'label': i, 'value': i} for i in lista
            ],
                       value='cardano',
                       clearable=False
                       ),

                    dcc.Graph(
                  id='meu-graph',
                  figure=fig)
                         ]) #end of the column
                        ]) #end of the row
                        ]) #end of the div