import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Delivery Performance Analysis", className="text-center text-success mb-3 mt-3", style={'fontSize': '2em'}))
    ]),
    dbc.Row([
        dbc.Col([
            html.H5("Monthly Filter", style={'fontSize': '1.2em'}),
            dcc.Dropdown(
                id='month-filter',
                options=[
                    {'label': 'Jan', 'value': 1},
                    {'label': 'Feb', 'value': 2},
                    {'label': 'Mar', 'value': 3},
                    {'label': 'Apr', 'value': 4},
                    {'label': 'May', 'value': 5},
                    {'label': 'Jun', 'value': 6},
                    {'label': 'Jul', 'value': 7},
                    {'label': 'Aug', 'value': 8},
                    {'label': 'Sep', 'value': 9},
                    {'label': 'Oct', 'value': 10},
                    {'label': 'Nov', 'value': 11},
                    {'label': 'Dec', 'value': 12}
                ],
                placeholder='Select a month',
                value=1,
                style={'fontSize': '1em'}
            ),
        ], style={'fontSize': '1em', 'padding-bottom': '1em'}
    ]),
dbc.Row([
    dbc.Col([
        html.H5("Top Customer Areas", style={'fontSize': '1.2em'}),
        dcc.Graph(id='top-customer-areas'),
    ], width=6, style={'margin-bottom': '0', 'padding-right': '2em'}),
    dbc.Col([
        html.H5("Feedback Category", style={'fontSize': '1.2em'}),
        dcc.Dropdown(
            id='feedback-category',
            options=[
                {'label': 'Product Quality', 'value': 'Product Quality'},
                {'label': 'Delivery', 'value': 'Delivery'},
                {'label': 'Customer Service', 'value': 'Customer Service'},
                {'label': 'App Experience', 'value': 'App Experience'}
            ],
            placeholder='Select a feedback category',
            value='Product Quality',
            style={'fontSize': '1em', 'padding-bottom': '1em'}
        ),

         html.H5("Customer Feedback", style={'fontSize': '1.2em'}),
            dcc.Graph(id='sentiment', style={'padding-bottom': '0em'}),
            html.H5("Average Delivery Time Difference", style={'fontSize': '1.2em', 'margin': '0'}),
            html.Div(id='avg-delivery-difference', className="button-3d", style={'padding': '1px', 'borderRadius': '1px', 'backgroundColor': 'green', 'boxShadow': '0px 4px 6px rgba(0, 0, 0, 0.1)', 'height': '3em'})
        ], width=6, style={'margin-bottom': '0', 'padding-left': '2em'})
        ])
], fluid=True)
