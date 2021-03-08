import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output
from app import app
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# import dataframe
from Database import Api

df2=Api.df_mk
PAGE_SIZE = 40


layout = html.Div(
            id='table-pag-with-graph-price',
            #className="five columns"
        )

@app.callback(Output('table-pag-with-graph-price', "children"),
        [Input('time-drop', 'value')
        ,Input('coin-drop', 'value')
        ])
def update_graph(time,lista):
    if str == type(time):
        df = df2
    else:
        df = df2.tail(time)

    coins = lista
    df_series= df[coins].dropna().pct_change()
    df_series['Portfolio'] = df_series.mean(axis=1)  # 20% bitcoin, ... , 20% ethereum
    df = (df_series + 1).cumprod()

    fig = make_subplots(rows=1, cols=2, subplot_titles=[f'Price return ({len(coins)} coins selected + equal share portolio)',
                                                    f'Statistics'])
    # Add traces

    for coin in coins:
        fig.add_trace(go.Scatter(x=df.index, y=df[f'{coin}'],
                             mode='lines',
                             name= coin), row=1, col=1)

    fig.add_trace(go.Scatter(x=df.index, y=df['Portfolio'],
                             mode='lines',
                             name='Portfolio return'), row=1, col=1)

    def sharpe_ratio(return_series, N, rf):
        mean = return_series.mean() * N - rf
        sigma = return_series.std() * np.sqrt(N)
        return mean / sigma

    N = 365  # 255 trading days in a year
    rf = 0.01  # 1% risk free rate
    sharpes = df_series.apply(sharpe_ratio, args=(N, rf,), axis=0)


    fig.add_trace(go.Bar(x=sharpes.index, y=sharpes,
                         name='Sharpe ratio'), row=1, col=2)


    def sortino_ratio(series, N, rf):
        mean = series.mean() * N - rf
        std_neg = series[series < 0].std() * np.sqrt(N)
        return mean / std_neg

    sortinos = df_series.apply(sortino_ratio, args=(N, rf,), axis=0)

    fig.add_trace(go.Bar(x=sortinos.index, y=sortinos,
                         name='Sortino ratio'), row=1, col=2)

    def max_drawdown(return_series):
        comp_ret = (return_series + 1).cumprod()
        peak = comp_ret.expanding(min_periods=1).max()
        dd = (comp_ret / peak) - 1
        return dd.min()

    max_drawdowns = df_series.apply(max_drawdown, axis=0)

    fig.add_trace(go.Bar(x=max_drawdowns.index, y=max_drawdowns,
                         name='max drawdows'), row=1, col=2)

    calmars = df_series.mean() * N / abs(max_drawdowns)

    fig.add_trace(go.Bar(x=calmars.index, y=calmars,
                         name='Calmar ratio'), row=1, col=2)

    fig.update_layout(height=500)#, showlegend=False)

    return html.Div(dcc.Graph(
                  id='meu-graph',
                  figure=fig,
                    ))
