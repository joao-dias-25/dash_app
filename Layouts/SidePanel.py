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

layout = html.Div([
        dbc.Row([dbc.Col(
        html.Div([
           # html.H5('Options'),

             html.Div([html.P()
                           , html.H6('Timeframe (not working)')
                           , dcc.Dropdown(id='time-drop'
                                          , options=[
                        {'label': i, 'value': y} for (i,y) in [('alltime', 'max'),
                                                             ('5years','1825'),
                                                             ('Year','365'),
                                                             ('Month','31'),
                                                             ('week','7')]
                    ],
                                          value='alltime',
                                          multi=False
                                          )
                        ])
           # , html.Div([html.P()
           #                , html.H6('rank Slider')
            #               , dcc.RangeSlider(id='rank-slider'
             #                                , min=1
              #                               , max=50
               #                              , marks={20: 'top20',
                #                                      50: 'top50',
                 #                                     }
                  #                           , value=[0, 50]
                   #                          )

                    #    ])
            , html.Div([html.P()
                           , html.H6('Coins (not working)')
                           , dcc.Dropdown(id='coin-drop'
                                          , options=[
                        {'label': i, 'value': i} for i in df
                    ],
                                          value=['US'],
                                          multi=True
                                          )
                        ])
            #, dcc.Checklist(id='filtro'
            #                , options=[
            #        {'label': 'filter by rank', 'value': 'Y'}
            #    ])

        ], style={'marginBottom': 10, 'marginTop': 10, 'marginLeft': 10, 'marginRight': 10,
                  'textAlign': 'left',
                    'color': '#319199' }
        )  # end div
        , width=2)  # End col
        , dbc.Col(html.Div([
            dcc.Tabs(id="tabs", value='tab-1', children=[
                dcc.Tab(label='Market caps', value='tab-1'),
                dcc.Tab(label='Ratios', value='tab-5'),
                dcc.Tab(label='Cryptocurrencies Volume', value='tab-2'),
                dcc.Tab(label='Stablecoins Volume', value='tab-3'),
                dcc.Tab(label='Bitcoin on Ethereum', value='tab-6'),
                dcc.Tab(label='rank table', value='tab-4'),
            ])
            , html.Div(id='tabs-content')
        ]), width=10)
    ])  # end row

])  # end div
