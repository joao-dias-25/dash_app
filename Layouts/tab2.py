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
coins=Api.coins
df_info=Api.df_i
dfs_info=Api.dfs_i
coin_vol2=Api.df_mk
#btc_tokens=['wrapped-bitcoin','renbtc','huobi-btc','sbtc','tbtc']
df_info_token=Api.df_btctokens



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



    fig2 = make_subplots(rows=2, cols=2,
                     specs=[[{'type':'domain'},{'type':'domain'}],
                            [{'type':'domain'},{'type':'xy'}]],
                     subplot_titles=['Coins Marketcap Dominance <br>'+ f'<i>({len(coins)} coins selected)</i>',
                                     'Stablecoins Marketcap Dominance <br>'+f'<i>(Top {len(stablecoins)} Stablecoins)</i>',
                                     'Bitcoins tokens (protocol dominance)',
                                     'Total of bitcoins on ethereum per protocol'])



    fig2.add_trace(go.Pie(labels=df_info.name, values=df_info.market_cap,
                      textinfo='label+percent', hole=.3,
                      )
               , row=1, col=1)

    fig2.add_trace(go.Pie(labels=dfs_info.name, values=dfs_info.market_cap,
                          textinfo='label+percent', hole=.3), row=1, col=2)

    fig2.add_trace(
        go.Bar(
            x=df_info_token.circulating_supply,
            y=df_info_token.name,
            marker=go.bar.Marker(
                color="rgb(253, 240, 54)",
                line=dict(color="rgb(0, 0, 0)",
                          width=2),

            ),
            orientation="h",
        ), row=2, col=2
    )

    fig2.add_trace(go.Pie(labels=df_info_token.name, values=df_info_token.circulating_supply,
                          textinfo='label+percent', hole=.3), row=2, col=1)



    fig2.update(layout_showlegend=False)
    fig2.update_traces( marker=dict( line=dict(color='#000000', width=2)))
    fig2.update_layout(height=900)

    return html.Div(#html.H6('Off-chain Volume')
                    dcc.Graph(
                      id='segundo-graph',
                      figure=fig2))
