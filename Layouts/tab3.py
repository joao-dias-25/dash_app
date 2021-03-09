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

nodes=Api.dfnodes


fig2 = make_subplots(rows=1, cols=2,
                     specs=[[{'type':'xy'},{'type':'domain'}]],
                     subplot_titles=['Bitcoin nodes (last 2hours)', 'graph'])

fig2.add_trace(go.Scatter(x=nodes.index, y=nodes.total_nodes,
                             mode='lines',
                             name= 'bitcoin nodes'), row=1, col=1)
#fig2.update(layout_showlegend=False)


#fig2.update_traces( marker=dict( line=dict(color='#000000', width=2)))

layout = html.Div([dbc.Row([dbc.Col(
                    dcc.Graph(
                  id='segundo-graph',
                  figure=fig2)
                         ) #end of the column
                        ]) #end of the row
                        ]) #end of the div