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

coins = Api.coins
df = Api.merge_data(coins,'max')
min_p=1
max_p=len(coins)



layout = html.Div([
        dbc.Row([dbc.Col(
        html.Div([
           # html.H5('Options'),

             html.Div([html.P()
                           , html.H6('Timeframe')
                           , dcc.Dropdown(id='time-drop'
                                          , options=[
                        {'label': i, 'value': j} for i,j in [('All time','max'),
                                                             ('5 years',1825),
                                                            ('3 years',1095),
                                                             ('2 years',730),
                                                             ('Year', 365),
                                                             ('6 Months', 180),
                                                            ('3 Months', 90),
                                                             ('Month', 31)]
                    ],
                                          value=1825,
                                          multi=False
                                          )
                        ])
            , html.Div([html.P()
                           , html.H6('Rank slider(not working)')
                           , dcc.RangeSlider(id='rank-slider'
                                             , min=min_p
                                             , max=max_p
                                             #, marks={20: 'top20',
                                            #          50: 'top50',
                                              #        }
                                             #, value=[0, 50]
                                             )

                        ])
            , html.Div([html.P()
                           , html.H6('Select coins')
                           , dcc.Dropdown(id='coin-drop'
                                          , options=[
                        {'label': i, 'value': i} for i in coins
                    ],
                                          value=['bitcoin','ethereum','cardano'],
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
                dcc.Tab(label='Marketcap Ratios', value='tab-5'),
                dcc.Tab(label='Price analysis', value='tab-7'),
                dcc.Tab(label='Cryptocurrencies Volume', value='tab-2'),
                dcc.Tab(label='Stablecoins Volume', value='tab-3'),
                dcc.Tab(label='Bitcoin on Ethereum', value='tab-6'),
                dcc.Tab(label='Coins Info', value='tab-4'),
            ])
            , html.Div(id='tabs-content')
        ]), width=10)
    ])  # end row

])  # end div


#@app.callback(Output('province-drop', 'options'),
#              [Input('time-drop', 'value')])
#def set_province_options(time):
#    days = time
#    return days
