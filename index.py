
# -*- coding: utf-8 -*-

# Run this app with `python index.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from app import app
from app import server
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# import dataframe
from Database import Api


colors = {
    'background': '#111111',
    'text': '#7FDBFF'}


df = Api.df
df_info=Api.coin_info
coin_vol=Api.df_vol
coins=Api.coins
stable_vol=Api.dfstable_vol
stablecoins=Api.stablecoins
stablecoins_info=Api.stablecoins_info

fig = make_subplots(rows=1, cols=2)
# Add traces

for coin in coins:
    fig.add_trace(go.Scatter(x=df.index, y=df[f'marketcap_{coin}'],
                             mode='lines',
                             name= coin), row=1, col=1)

#fig.update_layout(barmode='group',
 #                bargap=0)
fig.add_trace(go.Scatter(x=df.index, y=df['combine_mk'],
                             mode='lines',
                             name='combine_market_cap'), row=1, col=1)

fig.add_trace(go.Scatter(x=df.index, y=df['ratio_eth_btc'],
                             mode='lines',
                             name='ratio eth/btc'), row=1, col=2)
fig.add_trace(go.Scatter(x=df.index, y=df['ratio_ada_eth'],
                             mode='lines',
                             name='ratio ada/eth'), row=1, col=2)
fig.add_trace(go.Scatter(x=df.index, y=df['ratio_xmr_eth'],
                             mode='lines',
                             name='ratio xmr/eth'), row=1, col=2)
fig2 = make_subplots(rows=1, cols=4,
                     specs=[[{'type':'domain'}, {'type':'xy'}, {'type':'xy'},{'type':'domain'}]])
fig2.add_trace(go.Pie(labels=df_info.name, values=df_info.market_cap, textinfo='label+percent'), row=1, col=1)

for coin in coins:
    fig2.add_trace(go.Scatter(x=coin_vol.index, y=coin_vol[f'volume_{coin}'],
                             mode='lines',
                             name= coin), row=1, col=2)

for stablecoin in stablecoins:
    fig2.add_trace(go.Scatter(x=stable_vol.index, y=stable_vol[f'volume_{stablecoin}'],
                             mode='lines',
                             name= stablecoin), row=1, col=3)
fig2.add_trace(go.Pie(labels=stablecoins_info.name, values=stablecoins_info.market_cap, textinfo='label+percent'), row=1, col=4)
#cores = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'lightblue']
#fig2.update_traces(hole=.4,  marker=dict(colors=cores, line=dict(color='#000000', width=2)))

fig2.update(layout_showlegend=False)
fig2.update_layout(
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='dominance', x=0, y=0.5, font_size=16, showarrow=False),
                 dict(text='stablecoins', x=0.48, y=0.5, font_size=16, showarrow=False)])


#fig = px.line(df, x=df.index, y=["price",'volume','marketcap'])

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='A Dashboard',  style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.Div(children='on crypto currencies', style={
        'textAlign': 'center',
        'color': colors['text'],

    }),
    dcc.Dropdown(
        id='escolhas',
        options=[{'label': i, 'value': i} for i in ['1 option', '2 option', '3 option']],
        value='2 option'
    ),
    html.Div(id='display-value'),

    html.Br(),
    html.Div(id='my-output'),

    dcc.Graph(
        id='example-graph',
        figure=fig2
    ),
    dcc.Graph(
        id='segundo-graph',
        figure=fig
    ),
    dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df_info.columns],
    data=df_info.to_dict('records')),

])

@app.callback(dash.dependencies.Output('display-value', 'children'), [dash.dependencies.Input('escolhas', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)

