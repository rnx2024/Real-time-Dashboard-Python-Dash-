import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Delivery Performance Analysis", className="text-center text-primary mb-3 mt-3", style={'fontSize': '2em'}))
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
        ], width=4, style={'margin-bottom': '0'})
    ]),
    dbc.Row([
        dbc.Col([
            html.H5("Top Customer Areas", style={'fontSize': '1.2em'}),
            dcc.Graph(id='top-customer-areas'),
        ], width=6, style={'padding': '1'}),
        dbc.Col([
            html.H5("Top Feedback", style={'fontSize': '1.2em'}),
            dcc.Graph(id='sentiment'),
        ], width=6, style={'padding': '1'}),
    ], style={'margin-bottom': '0'}),
    dbc.Row([
        dbc.Col([
            html.H5("Total Order Value", style={'fontSize': '1.2em', 'margin': '0'}),
            html.Div(id='total-order-value', className="square-box", style={'padding': '1px', 'borderRadius': '1px', 'backgroundColor': '#6DA8DD', 'height': '3em'})
        ], width=6, style={'padding': '2'}),
        dbc.Col([
            html.H5("Average Delivery Time Difference", style={'fontSize': '1.2em', 'margin': '0'}),
            html.Div(id='avg-delivery-difference', className="button-3d", style={'padding': '1px', 'borderRadius': '1px', 'backgroundColor': 'green', 'boxShadow': '0px 4px 6px rgba(0, 0, 0, 0.1)', 'height': '3em'})
        ], width=6, style={'padding': '2'}),
    ], style={'margin-top': '0'})
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)
