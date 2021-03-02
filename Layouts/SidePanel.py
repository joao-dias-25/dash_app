import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas
from dash.dependencies import Input, Output
from app import app

from Database import Api

df = Api.coins
df2 = Api.stablecoins
layout = html.Div([
    html.H1('Wine Dash')
    , dbc.Row([dbc.Col(
        html.Div([
            html.H2('Filters')
            , dcc.Checklist(id='filtro'
                            , options=[
                    {'label': 'um filtro', 'value': 'Y'}
                ])
            , html.Div([html.P()
                           , html.H5('Coins')
                           , dcc.Dropdown(id='coin-drop'
                                          , options=[
                        {'label': i, 'value': i} for i in df
                    ],
                                          value=['US'],
                                          multi=True
                                          )
                        ])
            , html.Div([html.P()
                           , html.H5('Province')
                           , dcc.Dropdown(id='province-drop',
                                          value=[],
                                          multi=True
                                          )])
            , html.Div([html.P()
                           , html.H5('Variety')
                           , dcc.Dropdown(id='variety-drop',
                                          value=[],
                                          multi=True
                                          )])
        ], style={'marginBottom': 50, 'marginTop': 25, 'marginLeft': 15, 'marginRight': 15}
        )  # end div
        , width=3)  # End col
        , dbc.Col(html.Div([
            dcc.Tabs(id="tabs", value='tab-1', children=[
                dcc.Tab(label='Data Table', value='tab-1'),
                dcc.Tab(label='Scatter Plot', value='tab-2'),
                dcc.Tab(label='Heatmap Plot', value='tab-3'),
            ])
            , html.Div(id='tabs-content')
        ]), width=9)
    ])  # end row

])  # end div
