import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
from dash.dependencies import Input, Output
from app import app
from Database import Api
df_info = Api.coin_info
PAGE_SIZE = 30
layout =html.Div(dash_table.DataTable(
                            id='table-sorting-filtering',
                            columns=[
                            {"name": i, "id": i} for i in ['name','market_cap_rank','current_price','market_cap','price_change_percentage_24h','market_cap_change_percentage_24h']
                            ],
                            data=df_info.to_dict('records'),
                            style_table={'height':'750px'
                                ,'overflowX': 'scroll'},
style_data_conditional=[
                                {
                                    'if': {'row_index': 'odd'},
                                    'backgroundColor': 'rgb(248, 248, 248)'
                                }
                            ],
                            style_cell={
                                'height': '90',
                                # all three widths are needed
                                'minWidth': '140px', 'width': '140px', 'maxWidth': '140px', 'textAlign': 'left'
                                ,'whiteSpace': 'normal'
                            }
                            ,style_cell_conditional=[
                                {'if': {'column_id': 'description'},
                                'width': '48%'},
                                {'if': {'column_id': 'title'},
                                'width': '18%'},
                            ]
                            , page_current= 0,
                            page_size= PAGE_SIZE,
                            page_action='custom',
                            filter_action='custom',
                            filter_query='',
                            sort_action='custom',
                            sort_mode='multi',
                            sort_by=[]
                        )
                        )