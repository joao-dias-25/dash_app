import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# import dataframe
from Database import Api

nodes=Api.dfnodes_count
coor = Api.dfnodes[['I','J','K']]
eth_nodes=Api.nodes_eth()


fig1 = make_subplots(rows=1, cols=1,
                     #specs=[[{'type':'xy'}, {}]],
                     subplot_titles=['Bitcoin nodes count', 'map'])

fig1.add_trace(go.Scatter(x=nodes.index, y=nodes.total_nodes,
                             mode='lines',
                             name= 'bitcoin nodes'), row=1, col=1)

fig2 =go.Figure(go.Scattergeo(
        lon = coor['J'],
        lat = coor['I'],
        text = coor['K'],

       # mode = 'markers',
       # marker_color = df['cnt'],
        ))

fig2.update_layout(
        title = (f'Total Bitcoin nodes: {nodes.total_nodes[0]} ; snapshot:{nodes.index[0]}'
                 f'<br>Total Ethereum nodes: {eth_nodes[0]}; snapshot:{eth_nodes[1]}'),
        geo_scope='world',
    )

layout = html.Div([dbc.Row([dbc.Col([
                 dcc.Graph(
                 id='mapa',
                  figure=fig2
                        )
                        ])#end of the column
                        ]) #end of the row
                        ]) #end of the div