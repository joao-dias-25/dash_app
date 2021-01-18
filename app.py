# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.express as px
import pandas as pd
import urllib3
from urllib3 import request

# to handle certificate verification
import certifi

# to manage json data
import json


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server


# handle certificate verification and SSL warnings:
# reference https://urllib3.readthedocs.io/en/latest/user-guide.html#ssl
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())

# get data from the API; replace url with target source
url = 'https://maps2.dcgis.dc.gov/dcgis/rest/services/FEEDS/MPD/MapServer/2/query?where=1%3D1&outFields=*&outSR=4326&f=json'
r = http.request('GET', url)

# decode json data into a dict object
data = json.loads(r.data.decode('utf-8'))

df = pd.json_normalize(data, 'features')
# print the first rows and header of the dataframe
#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')



#fig = px.bar(df, x=df.index, y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='A Dashboard'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    #dcc.Graph(
       # id='example-graph',
       # figure=fig
    #)
    dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)
])

if __name__ == '__main__':
    app.run_server(debug=True)