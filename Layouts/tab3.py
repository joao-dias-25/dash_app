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

stablecoins=Api.stablecoins
stable_vol=Api.merge_vol(stablecoins, 'max')
stablecoins_info=Api.merge_inf(stablecoins)


fig2 = make_subplots(rows=1, cols=2,
                     specs=[[{'type':'xy'},{'type':'domain'}]],
                     subplot_titles=['Volume', 'Current Dominance'])

for stablecoin in stablecoins:
    fig2.add_trace(go.Scatter(x=stable_vol.index, y=stable_vol[f'volume_{stablecoin}'],
                             mode='lines',
                             name= stablecoin), row=1, col=1)
fig2.add_trace(go.Pie(labels=stablecoins_info.name, values=stablecoins_info.market_cap,
                      textinfo='label+percent', hole=.3), row=1, col=2)
#fig2.update_layout(
    # Add annotations in the center of the donut pies.
 #   annotations=[dict(text='dominance cryptocurrencies', x=0.1, y=0.5, font_size=10, showarrow=False),
  #               dict(text='dominance stablecoins', x=0.82, y=0.5, font_size=10, showarrow=False)])


fig2.update(layout_showlegend=False)
#fig2.update_layout(
    # Add annotations in the center of the donut pies.
 #   annotations=[dict(text='dominance', x=0, y=0.5, font_size=16, showarrow=False),
   #              dict(text='stablecoins', x=0.48, y=0.5, font_size=16, showarrow=False)])
#cores = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'lightblue']

fig2.update_traces( marker=dict( line=dict(color='#000000', width=2)))

layout = html.Div(dcc.Graph(
                  id='segundo-graph',
                  figure=fig2))