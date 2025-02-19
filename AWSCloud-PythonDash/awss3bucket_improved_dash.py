import boto3
import pandas as pd
from io import StringIO
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import webbrowser
from threading import Timer

s3_client = boto3.client('s3')
bucket_name = 'myfirstawsbucketlistforthisyear'
object_name = 'shoppingtrends.csv'

response = s3_client.get_object(Bucket=bucket_name, Key=object_name)
csv_content = response['Body'].read().decode('utf-8')

df = pd.read_csv(StringIO(csv_content))

customer_id_column = 'Customer ID'
age_column = 'Age'
gender_column = 'Gender'
review_rating_column = 'Review Rating'
category_column = 'Category'
payment_method_column = 'Payment Method'
shipping_type_column = 'Shipping Type'
location_column = 'Location'
frequency_column = 'Frequency of Purchases'
purchase_amount_column = 'Purchase Amount (USD)'

total_purchase_amounts = df[purchase_amount_column].sum()
total_customers = df[customer_id_column].nunique()
average_review_rating = df[review_rating_column].mean()

# buttons and dropdown styles
LARGE_CIRCLE_STYLE = {
    'width': '110px',
    'height': '110px',
    'border-radius': '50%',
    'color': 'white',
    'font-weight': 'bold',
    'font-size': '1.2rem',
    'display': 'inline-block',
    'line-height': '110px', 
    'box-shadow': '0px 4px 6px rgba(0, 0, 0, 0.1)', 
    'text-align': 'center',
    'margin': '0.5rem'
}

TEXT_STYLE = {
    'color': '#7A7B84',  
    'font-size': '0.9rem',
    'font-family': 'Arial',  
    'text-align': 'center',
    'margin-top': '0.25rem'
}

DROPDOWN_STYLE = {
    'background-color': '#52AC6C',  
    'color': 'black',
    'font-weight': 'regular',
    'font-size': '0.8rem', 
    'font-family': 'Arial', 
    'border-radius': '0px',  
    'height': '1em',  
    'border': 'none',    
    }

GREEN_BUTTON_STYLE = LARGE_CIRCLE_STYLE.copy()
GREEN_BUTTON_STYLE['background-color'] = '#61AC52'

BLUE_BUTTON_STYLE = LARGE_CIRCLE_STYLE.copy()
BLUE_BUTTON_STYLE['background-color'] = '#3B5BC3'  

ORANGE_BUTTON_STYLE = LARGE_CIRCLE_STYLE.copy()
ORANGE_BUTTON_STYLE['background-color'] = '#C0883E'  


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Dashboard layout
app.layout = dbc.Container(fluid=True, children=[
    dbc.Row([
        dbc.Col([
            html.H1("Customer Purchase Analysis Dashboard", className="text-center mb-3")
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H4("Summary Statistics"),
            html.Div([
                html.Div([
                    html.Div(f"${total_purchase_amounts:.2f}", style=GREEN_BUTTON_STYLE),
                    html.Div("Total Purchase Amounts", style=TEXT_STYLE)
                ], style={'text-align': 'center', 'display': 'inline-block', 'margin-right': '1rem'}),
                html.Div([
                    html.Div(f"{total_customers}", style=BLUE_BUTTON_STYLE),
                    html.Div("Total Customers", style=TEXT_STYLE)
                ], style={'text-align': 'center', 'display': 'inline-block'})
            ], style={'text-align': 'center'}),
            html.Div([
                html.Div([
                    html.Div(f"{average_review_rating:.2f}", style=ORANGE_BUTTON_STYLE),
                    html.Div("Average Review Rating", style=TEXT_STYLE)
                ], style={'text-align': 'center', 'display': 'inline-block'})
            ], style={'text-align': 'center'}),
            dcc.Graph(figure=px.pie(df, names=gender_column, title='Gender Distribution', height=350))
        ], width=4),
        dbc.Col([
            html.Div([
                dcc.Dropdown(
                    id='location-dropdown',
                    options=[{'label': loc, 'value': loc} for loc in df[location_column].unique()],
                    value='Kentucky',  
                    placeholder='Select a Location',
                    style=DROPDOWN_STYLE,  
                    className='custom-dropdown'  
                )
            ], style={'text-align': 'center', 'margin-bottom': '1rem'}), 
            dcc.Graph(id='category-bar-chart', style={'height': '320px'}),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='payment-method-pie-chart', style={'height': '320px'})
                ], width=6),
                dbc.Col([
                    dcc.Graph(id='shipping-type-pie-chart', style={'height': '320px'})
                ], width=6)
            ], style={'padding': '0'})
        ], width=8)
    ])
])

@app.callback(
    Output('category-bar-chart', 'figure'),
    Output('payment-method-pie-chart', 'figure'),
    Output('shipping-type-pie-chart', 'figure'),
    Input('location-dropdown', 'value')
)
def update_dashboard(location):
    filtered_df = df if location is None else df[df[location_column] == location]
    category_bar_chart = px.bar(filtered_df, x=category_column, y=purchase_amount_column, title='Number of Purchases by Category', 
                                hover_data={category_column: True, purchase_amount_column: ':$.2f'})
    payment_method_pie_chart = px.pie(filtered_df, names=payment_method_column, title='Payment Method Distribution')
    shipping_type_pie_chart = px.pie(filtered_df, names=shipping_type_column, title='Shipping Type Distribution')

    return category_bar_chart, payment_method_pie_chart, shipping_type_pie_chart

def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run_server(debug=True)