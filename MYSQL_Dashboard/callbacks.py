from dash import Input, Output, html
import plotly.express as px
from data_fetching import delivery_data, customer_data, order_data, feedback_data
from layout import app  # Import the app object

@app.callback(
    Output('top-customer-areas', 'figure'),
    [Input('month-filter', 'value')]
)
def update_top_customer_areas(month):
    # Filter customer data based on selected month
    filtered_customer_data = customer_data[customer_data['month'] == month]
    top_areas = filtered_customer_data['area'].value_counts().head(5)
    
    fig = px.pie(
        names=top_areas.index,
        values=top_areas.values,
        hole=.6,
        title="Top 5 Customer Areas"
    )
    return fig

@app.callback(
    Output('sentiment', 'figure'),
    [Input('month-filter', 'value')]
)
def update_feedback_category(month, category):
    # Filter feedback data based on selected month and feedback category
    filtered_feedback_data = feedback_data[(feedback_data['month'] == month) & 
                                           (feedback_data['feedback_category'] == category)]
    
   )
    return fig

@app.callback(
    Output('total-order-value', 'children'),
    [Input('month-filter', 'value')]
)
def update_total_order_value(month):
    # Filter order data based on selected month
    filtered_order_data = order_data[order_data['month'] == month]
    total_value = filtered_order_data['order_total'].sum()
    
    return html.Div([
        html.H4(f'Total Order Value: {total_value:.2f}', style={'color': 'white', 'fontSize': '1.2em'}),
    ], style={'padding': '10px', 'borderRadius': '5px', 'backgroundColor': '#6DA8DD', 'height': '3em'})

@app.callback(
    Output('avg-delivery-difference', 'children'),
    [Input('month-filter', 'value')]
)
def update_avg_delivery_difference(month):
    filtered_data = delivery_data[delivery_data['month'] == month]
    avg_diff = (filtered_data['actual_time'] - filtered_data['promised_time']).mean()
    
    # Convert Timedelta to total seconds for display
    avg_diff_seconds = avg_diff.total_seconds()
    
    return html.Div([
        html.H4(f'{avg_diff_seconds:.2f} seconds', style={'color': 'white', 'fontSize': '1.2em'}),
        html.P('Avg. Delivery Diff', style={'color': 'white', 'fontSize': '1em'})
    ], style={'padding': '10px', 'borderRadius': '5px', 'backgroundColor': 'green', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)', 'height': '3em'})
