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
    fig1 = make_subplots(rows=1, cols=1,
                        subplot_titles=['Total Marketcap <br>'+ f'<i>({len(coins)} coins selected)</i>'])

    fig3 = make_subplots(rows=1, cols=1,
                        subplot_titles=['Total Marketcap <br>'+f'<i>(Top {len(stablecoins)} Stablecoins)</i>'])

    # Add traces
    for coin in coins:
        fig1.add_trace(go.Scatter(x=df.index, y=df[f'mk_{coin}'],
                             mode='lines',
                             name= coin), row=1, col=1)

    fig1.add_trace(go.Scatter(x=df.index, y=df[[f'mk_{coin}' for coin in coins]].sum(axis=1),
                             mode='lines',
                             name='combine_mk'), row=1, col=1)

    for stablecoin in stablecoins:
        fig3.add_trace(go.Scatter(x=df_s.index, y=df_s[f'mk_{stablecoin}'],
                             mode='lines',
                             name= stablecoin), row=1, col=1)

    fig3.add_trace(go.Scatter(x=df_s.index, y=df_s[[f'mk_{coin}' for coin in stablecoins]].sum(axis=1),
                             mode='lines',
                             name='Stablecoins_mk'), row=1, col=1)

    fig2 = make_subplots(rows=1, cols=1,
                         subplot_titles=['Volume <br>'+ f'<i>({len(coins)} coins selected)</i>'])
    fig4 = make_subplots(rows=1, cols=1,
                         subplot_titles=['Volume <br>'+f'<i>(Top {len(stablecoins)} Stablecoins)</i>'])

    for coin in coins:
        fig2.add_trace(go.Scatter(x=df.index, y=df[f'volume_{coin}'],
                             mode='lines',
                             name= coin), row=1, col=1)

    for stablecoin in stablecoins:
        fig4.add_trace(go.Scatter(x=df_s.index, y=df_s[f'volume_{stablecoin}'],
                                  mode='lines',
                                  name=stablecoin), row=1, col=1)

    fig2.add_trace(go.Scatter(x=df.index, y=df[[f'volume_{coin}' for coin in coins]].sum(axis=1),
                             mode='lines',
                             name='combine_v'), row=1, col=1)

    fig4.add_trace(go.Scatter(x=df_s.index, y=df_s[[f'volume_{coin}' for coin in stablecoins]].sum(axis=1),
                             mode='lines',
                             name='Stablecoins_v'), row=1, col=1)

    fig1.update_layout(title = f'Data from Source: <a href="https://www.coingecko.com/">Coingecko</a>',
                        template="simple_white",margin=dict(
                                l=30, #left margin
                                r=20, #right margin
                                b=60, #bottom margin
                                t=100  #top margin
             ))
    fig2.update_layout(template="simple_white",margin=dict(
                                l=30, #left margin
                                r=20, #right margin
                                b=60, #bottom margin
                                t=60  #top margin
             ))
    fig3.update_layout(template="simple_white", margin=dict(
        l=30,  # left margin
        r=20,  # right margin
        b=60,  # bottom margin
        t=100  # top margin
    ))
    fig4.update_layout(template="simple_white", margin=dict(
        l=30,  # left margin
        r=20,  # right margin
        b=60,  # bottom margin
        t=60  # top margin
    ))

    fig1.update_yaxes(tickprefix='$')
    fig2.update_yaxes(tickprefix='$')
    fig3.update_yaxes(tickprefix='$')
    fig4.update_yaxes(tickprefix='$')

    return html.Div([dbc.Row([dbc.Col([
                    dcc.Graph(
                  id='meu-graph',
                  figure=fig1),
                    dcc.Graph(
                  id='meu-graph',
                  figure=fig2)
                         ]),dbc.Col([
                    dcc.Graph(
                  id='meu-graph',
                  figure=fig3),
                    dcc.Graph(
                  id='meu-graph',
                  figure=fig4)
                         ])
                    #end of the column
                        ]) #end of the row
                        ]) #end of the div


