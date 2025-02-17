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

print(df.columns)
print(df.head())

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

returning_customers = df[df[frequency_column] != 'First-time']['Customer ID'].nunique()
total_purchase_amounts = df[purchase_amount_column].sum()

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout of the dashboard
app.layout = dbc.Container(fluid=True, children=[
    dbc.Row([
        dbc.Col([
            html.H1("Customer Purchase Analysis Dashboard", className="text-center mb-3")
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H4("Summary Statistics"),
            html.P(f"Total Purchase Amounts: ${total_purchase_amounts:.2f}"),
            html.P(f"Total Customers: {df[customer_id_column].nunique()}"),
            html.P(f"Average Age: {df[age_column].mean():.2f}"),
            html.P(f"Average Review Rating: {df[review_rating_column].mean():.2f}"),
            html.P(f"Returning Customers: {returning_customers}"),
            dcc.Graph(figure=px.pie(df, names=gender_column, title='Gender Distribution'))
        ], width=4),
        dbc.Col([
            dcc.Dropdown(
                id='location-dropdown',
                options=[{'label': loc, 'value': loc} for loc in df[location_column].unique()],
                placeholder='Select a Location'
            ),
            dcc.Graph(id='category-bar-chart', style={'height': '300px'}),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='payment-method-pie-chart', style={'height': '300px'})
                ], width=6),
                dbc.Col([
                    dcc.Graph(id='shipping-type-pie-chart', style={'height': '300px'})
                ], width=6)
            ], style={'padding': '0'})
        ], width=8)
    ])
])

# Callbacks to update charts and tables
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

# Function to open the browser automatically
def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")

# Run the Dash app
if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run_server(debug=True)
