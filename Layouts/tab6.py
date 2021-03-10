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

btc_tokens=['wrapped-bitcoin','renbtc','huobi-btc','sbtc','tbtc']



fig2 = make_subplots(rows=1, cols=2,
                     specs=[[{'type':'xy'},{'type':'domain'}]],
                     subplot_titles=['information', 'information'])

#fig2.add_trace(go.Pie(labels=df_info.name, values=df_info.circulating_supply,
           #           textinfo='label+percent', hole=.3), row=1, col=2)


#fig2.update(layout_showlegend=False)

#fig2.update_traces( marker=dict( line=dict(color='#000000', width=2)))

layout = html.Div([dbc.Row([dbc.Col(
                    dcc.Graph(
                  id='segundo-graph',
                  figure=fig2)
                         ) #end of the column
                        ]) #end of the row
                        ]) #end of the div