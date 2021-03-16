
# -*- coding: utf-8 -*-

# Run this app with `python index.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from app import app
from Layouts import tab1, tab2, tab3, tab4, tab5, tab6, tab7, navbar, SidePanel
from app import server
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output


colors = {
    'background': '#E5EEFD',
    'text': 'black'}


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[

            navbar.Navbar(),
            SidePanel.layout,
            #html.Div(id='display-value'),

            html.Br(),

             html.H3(children='Dashboard on crypto currencies', style={
            'textAlign': 'center',
            'color': colors['text']
             }),
            html.H6(children=["Support this project by donating BTC :)"]
                        , id='outro-texto',
                        title='titulo',
                        style={'textAlign': ['center'],
                               'color': colors['text']
                                                        }),
            html.H6(children=["bc1qhl0um3rgwm64unykdc8wces2c6vcy59qtf6kja"]
                        , id='nota',
                        title='titulo',
                        style={'textAlign': ['center'],
                               'color': colors['text']
                                                        }),
            html.Footer(children='© 2021 Crypto dashboard One', id='footer',
                        style={'textAlign': 'center',
                                'color': colors['text']
                                                        }

                        ),
])

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return tab1.layout
    elif tab == 'tab-2':
       return tab2.layout
    elif tab == 'tab-3':
       return tab3.layout
    elif tab == 'tab-4':
       return tab4.layout
    elif tab == 'tab-5':
       return tab5.layout
    elif tab == 'tab-6':
       return tab6.layout
    elif tab == 'tab-7':
       return tab7.layout

#@app.callback(dash.dependencies.Output('display-value', 'children'), [dash.dependencies.Input('escolhas', 'value')])
#def display_value(value):
#    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)

