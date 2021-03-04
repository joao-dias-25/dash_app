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


df_info=Api.df_i
coin_vol2=Api.df_v


layout = html.Div(
            id='table-paging-volume-graph-container',
            #className="five columns"
        )

@app.callback(Output('table-paging-volume-graph-container', "children"),
        [Input('time-drop', 'value')
        , Input('coin-drop', 'value')
        ])
def update_graph(time,lista):
    coins = lista

    #df_info = Api.merge_inf(coins)

    if str == type(time):
        coin_vol = coin_vol2
    else:
        coin_vol = coin_vol2.tail(time)



    fig2 = make_subplots(rows=1, cols=2,
                     specs=[[{'type':'xy'},{'type':'domain'}]],
                     subplot_titles=['Volume', 'Current Dominance'])

    fig2.add_trace(go.Pie(labels=df_info.name, values=df_info.market_cap,
                      textinfo='label+percent', hole=.3,
                      )
               , row=1, col=2)
    fig2.update(layout_showlegend=False)


    for coin in coins:
        fig2.add_trace(go.Scatter(x=coin_vol.index, y=coin_vol[f'volume_{coin}'],
                             mode='lines',
                             name= coin), row=1, col=1)



    fig2.update_traces( marker=dict( line=dict(color='#000000', width=2)))

    return html.Div(dcc.Graph(
                  id='segundo-graph',
                  figure=fig2))