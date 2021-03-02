
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

fig = make_subplots(rows=1, cols=2)
# Add traces
fig.add_trace(go.Scatter(x=df.index, y=df['marketcap_x'],
                             mode='lines',
                             name='bitcoin'), row=1, col=1)
fig.add_trace(go.Scatter(x=df.index, y=df['marketcap_y'],
                             mode='lines',
                             name='ethereum'),row=1, col=1)
fig.add_trace(go.Scatter(x=df.index, y=df['marketcap'],
                             mode='lines',
                             name='cardano'),row=1, col=1)
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



#fig = px.line(df, x=df.index, y=["price",'volume','marketcap'])

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='A Dashboard',  style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.Div(children='A personalized dashboard ', style={
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
        figure=fig
    ),
    dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records')),

])

@app.callback(dash.dependencies.Output('display-value', 'children'), [dash.dependencies.Input('escolhas', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)

