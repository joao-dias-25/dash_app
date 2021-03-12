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

    fig = make_subplots(rows=1, cols=1, subplot_titles=[f'<i>({len(coins)} coins selected & equal share portolio)</i>'])
    # Add traces

    for coin in coins:
        fig.add_trace(go.Scatter(x=df.index, y=df[f'{coin}'],
                             mode='lines',
                             name= coin), row=1, col=1)

    fig.add_trace(go.Scatter(x=df.index, y=df['Portfolio'],
                             mode='lines',
                             name='Portfolio return'), row=1, col=1)

    fig2 = make_subplots(rows=2, cols=2)

    def sharpe_ratio(return_series, N, rf):
        mean = return_series.mean() * N - rf
        sigma = return_series.std() * np.sqrt(N)
        return mean / sigma

    N = 365  # 255 trading days in a year
    rf = 0.01  # 1% risk free rate
    sharpes = df_series.apply(sharpe_ratio, args=(N, rf,), axis=0)


    fig2.add_trace(go.Bar(x=sharpes.index, y=sharpes,
                         name='Sharpe ratio'), row=1, col=1)

    #fig3 = make_subplots(rows=1, cols=1, subplot_titles=[f'<i>({len(coins)} coins selected & equal share portolio)</i>'])

    def sortino_ratio(series, N, rf):
        mean = series.mean() * N - rf
        std_neg = series[series < 0].std() * np.sqrt(N)
        return mean / std_neg

    sortinos = df_series.apply(sortino_ratio, args=(N, rf,), axis=0)

    fig2.add_trace(go.Bar(x=sortinos.index, y=sortinos,
                         name='Sortino ratio'), row=1, col=2)

    def max_drawdown(return_series):
        comp_ret = (return_series + 1).cumprod()
        peak = comp_ret.expanding(min_periods=1).max()
        dd = (comp_ret / peak) - 1
        return dd.min()

    max_drawdowns = df_series.apply(max_drawdown, axis=0)

    fig2.add_trace(go.Bar(x=max_drawdowns.index, y=max_drawdowns,
                         name='max drawdows'), row=2, col=1)

    calmars = df_series.mean() * N / abs(max_drawdowns)

    fig2.add_trace(go.Bar(x=calmars.index, y=calmars,
                         name='Calmar ratio'), row=2, col=2)

    fig2.update_layout(height=800)#, showlegend=False)

    return html.Div([dbc.Row([dbc.Col([
                 dcc.Graph(
                 id='grafico',
                  figure=fig
                        )], width=7),
                            dbc.Col([html.Div([html.H3('Price return'),
                                     html.P(f'The plot shows the growth of $1 invested {time} days ago')])
                            ],width=5)]),
                dbc.Row([dbc.Col([
                    dcc.Graph(
                        id='grafico2',
                        figure=fig2
                    )], width=7),
                    dbc.Col([html.Div([html.H4('Sharpe ratio'),
                                       html.P('''The Sharpe ratio is the most common ratio for comparing reward (return on investment) to risk (standard deviation). This allows us to adjust the returns on an investment by the amount of risk that was taken in order to achieve it. The Sharpe ratio also provides a useful metric to compare investments.'''),
                                       html.H4('Sortino ratio'),
                                       html.P('''The Sortino ratio is very similar to the Sharpe ratio, the only difference being that where the Sharpe ratio uses all the observations for calculating the standard deviation the Sortino ratio only considers the harmful variance.'''),
                                       html.H4('Max Drawdown'),
                                       html.P('''Max drawdown quantifies the steepest decline from peak to trough observed for an investment. This is useful for a number of reasons, mainly the fact that it doesn't rely on the underlying returns being normally distributed. It also gives us an indication of conditionality amongst the returns increments. Whereas in the previous ratios, we only considered the overall reward relative to risk, however, it may be that consecutive returns are not independent leading to unacceptably high losses of a given period of time. '''),
                                       html.H4('Calmar ratio'),
                                       html.P('''The final risk/reward ratio we will consider is the Calmar ratio. This is similar to the other ratios, with the key difference being that the Calmar ratio uses max drawdown in the denominator as opposed to standard deviation.'''),

                                       ])
                             ], width=5)]) #end of the row
                        ]) #end of the div
