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
import pandas as pd


# import dataframe
from Database import Api

btc_tokens=['wrapped-bitcoin','renbtc','huobi-btc','sbtc','tbtc']

#df_mk = Api.df
df_info=Api.df_btctokens

#coins=Api.coins

fig2 = make_subplots(rows=1, cols=2,
                     specs=[[{'type':'xy'},{'type':'domain'}]],
                     subplot_titles=['Total of bitcoins in Ethereum ', 'Protocol Dominance'])

fig2.add_trace(
    go.Bar(
        x=df_info.circulating_supply,
        y=df_info.name,
        marker=go.bar.Marker(
            color="rgb(253, 240, 54)",
            line=dict(color="rgb(0, 0, 0)",
                      width=2),

        ),
        orientation="h",
    ), row=1, col=1
)

#fig2.add_trace(go.Bar(x=df_info.name, y=df_info.circulating_supply, name='btc'), row=1, col=1)

fig2.add_trace(go.Pie(labels=df_info.name, values=df_info.circulating_supply,
                      textinfo='label+percent', hole=.3), row=1, col=2)


fig2.update(layout_showlegend=False)
#fig2.update_layout(
    # Add annotations in the center of the donut pies.
 #   annotations=[dict(text='dominance', x=0, y=0.5, font_size=16, showarrow=False),
   #              dict(text='stablecoins', x=0.48, y=0.5, font_size=16, showarrow=False)])
#cores = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'lightblue']

fig2.update_traces( marker=dict( line=dict(color='#000000', width=2)))

layout = html.Div([dbc.Row([dbc.Col(
                    dcc.Graph(
                  id='segundo-graph',
                  figure=fig2)
                         ) #end of the column
                        ]) #end of the row
                        ]) #end of the div