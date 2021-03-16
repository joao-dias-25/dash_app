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
             #html.H6('Options'),

             html.Div([html.P()
                           , html.P('Timeframe')
                           , dcc.Dropdown(id='time-drop'
                                          , options=[
                        {'label': i, 'value': j} for i,j in [('All time','max'),
                                                             ('5 years',1825),
                                                            ('4 years',1460),
                                                            ('3 years',1095),
                                                             ('2 years',730),
                                                             ('Year', 365),
                                                             ('6 Months', 180),
                                                            ('3 Months', 90),
                                                             ('Month', 31)]
                    ],
                                          value=1460,
                                          #multi=False,
                                            clearable=False
                                          )
                        ]),
            html.Div([html.P()
                         , html.P('Top coins (not available)')
                         , dcc.Dropdown(id='order-drop'
                                        , options=[
                        {'label': i, 'value': j} for i, j in [('by Market Cap', 'market_cap_desc'),
                                                              ('by Gecko rank', 'gecko_desc'),
                                                              ('by Volume','volume_desc')]
                                                            ],
                                        value='gecko_desc',
                                        clearable=False
                                        )
                      ])


            , html.Div([html.P()
                           , html.P('Rank slider (not available)')
                           , dcc.RangeSlider(id='rank-slider'
                                             , min=min_p
                                             , max=max_p
                                             #, marks={20: 'top20',
                                            #          50: 'top50',
                                              #        }
                                             , value=[2, 10]
                                             )

                        ])
            , html.Div([html.P()
                           , html.P(f'Select coins (top {len(coins)})')
                           , dcc.Dropdown(id='coin-drop'
                                          , options=[
                        {'label': i, 'value': i} for i in coins
                    ],
                                          value=['bitcoin','ethereum','cardano'],
                                          multi=True,
                                          clearable=False
                                          )
                        ])
            #, dcc.Checklist(id='filtro'
            #                , options=[
            #        {'label': 'filter by rank', 'value': 'Y'}
            #    ])

        ], style={'marginBottom': 10, 'marginTop': 70, 'marginLeft': 20, 'marginRight': 20,
                  'textAlign': 'left',
                    #'color': 'white',
                    'dark' : True}
        )  # end div
        , width=2)  # End col
        , dbc.Col(html.Div([
            dcc.Tabs(id="tabs", value='tab-1', children=[
                dcc.Tab(label='Market caps', value='tab-1'),
                dcc.Tab(label='Marketcap Ratios', value='tab-5'),
                dcc.Tab(label='Price analysis', value='tab-7'),
                dcc.Tab(label='Cryptocurrencies Dominance', value='tab-2'),
                dcc.Tab(label='BTC & ETH nodes Count', value='tab-3'),
                dcc.Tab(label='On-chain stats', value='tab-6'),
                dcc.Tab(label='Bitcoin 24h stats', value='tab-4'),
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
