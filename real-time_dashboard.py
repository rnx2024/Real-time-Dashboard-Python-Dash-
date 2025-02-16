import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import webbrowser
from threading import Timer

def load_data():
    return pd.read_csv(r'C:\Users\acer\Documents\data_analysis_project\ExcelDashboard\shopping-trends.csv')

df = load_data()

# Define a color palette with more neutral shades
main_graph_palette = ['#4e79a7', '#59a14f', '#9c755f', '#f28e2b', '#edc948', '#e15759', '#76b7b2', '#ff9da7', '#af7aa1']

app = dash.Dash(__name__)
app.layout = html.Div(style={'display': 'flex', 'flex-direction': 'row'}, children=[
    html.Div(style={'flex': '50%', 'padding': '10px'}, children=[
        html.H1(children='Real-Time Shopping Trends Dashboard', style={'font-family': 'Arial', 'font-size': '30px', 'color': '#800000'}),
        
        html.Div(style={'display': 'flex', 'justify-content': 'space-between'}, children=[
            html.Div(id='total-purchase-amount', style={'font-family': 'Arial', 'font-size': '48px', 'color': '#377eb8'}),
            html.Div(id='total-purchase-count', style={'font-family': 'Arial', 'font-size': '48px', 'color': '#ff7f00'})
        ]),
        
        html.Div(style={'display': 'flex', 'justify-content': 'space-between'}, children=[
            html.Div('Total Purchase Amount', style={'font-family': 'Arial', 'font-size': '24px', 'color': '#777777'}),
            html.Div('Total Purchase Count', style={'font-family': 'Arial', 'font-size': '24px', 'color': '#777777'})
        ]),
        
        dcc.Graph(
            id='live-update-graph',
            animate=True,
            style={'height': '50vh'}
        ),
    ]),
    
    html.Div(style={'flex': '50%', 'padding': '10px'}, children=[
        html.Label('Filter by Location', style={'font-family': 'Arial', 'font-size': '18px'}),
        dcc.Dropdown(
            id='location-filter',
            options=[{'label': loc, 'value': loc} for loc in df['Location'].unique()],
            multi=True,
            placeholder='Select locations',
            style={'font-family': 'Arial', 'font-size': '16px', 'margin-bottom': '20px'}
        ),
        
        dcc.Graph(
            id='top-items-graph',
            style={'height': '40vh'}
        ),
        
        dcc.Graph(
            id='top-locations-graph',
            style={'height': '40vh'}
        ),
    ]),
    
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # in milliseconds
        n_intervals=0
    )
])

@app.callback(
    [Output('live-update-graph', 'figure'),
     Output('top-items-graph', 'figure'),
     Output('top-locations-graph', 'figure'),
     Output('total-purchase-amount', 'children'),
     Output('total-purchase-count', 'children')],
    [Input('interval-component', 'n_intervals'),
     Input('location-filter', 'value')]
)
def update_graphs(n, selected_locations):
    try:
        # Reload data from CSV
        df = load_data()
        
        # Apply filters
        if selected_locations:
            df = df[df['Location'].isin(selected_locations)]
        
        # Calculate total purchase amount and counts
        total_purchase_amount = df['Purchase Amount (USD)'].sum()
        total_purchase_count = df.shape[0]
        
        # Create the main graph with more neutral colors
        main_fig = go.Figure(
            data=[go.Bar(x=df['Item Purchased'], y=df['Purchase Amount (USD)'],
                         marker=dict(color=main_graph_palette[:len(df['Item Purchased'].unique())]))],
            layout=go.Layout(title='Real-Time Data', xaxis=dict(title='Item Purchased'), yaxis=dict(title='Purchase Amount (USD)'))
        )
        
        # Create the top 5 items graph
        top_items = df.groupby('Item Purchased')['Purchase Amount (USD)'].sum().nlargest(5).reset_index()
        top_items_fig = go.Figure(
            data=[go.Bar(x=top_items['Item Purchased'], y=top_items['Purchase Amount (USD)'],
                         marker=dict(color=main_graph_palette[:5]))],
            layout=go.Layout(title='Top 5 Items', xaxis=dict(title='Item Purchased'), yaxis=dict(title='Total Purchase Amount (USD)'))
        )
        
        # Create the top 5 locations graph for the top 5 items
        top_items_df = df[df['Item Purchased'].isin(top_items['Item Purchased'])]
        top_locations = top_items_df.groupby('Location')['Purchase Amount (USD)'].sum().nlargest(5).reset_index()
        top_locations_fig = go.Figure(
            data=[go.Bar(x=top_locations['Location'], y=top_locations['Purchase Amount (USD)'],
                         marker=dict(color=main_graph_palette[:5]))],
            layout=go.Layout(title='Top 5 Locations', xaxis=dict(title='Location'), yaxis=dict(title='Total Purchase Amount (USD)'))
        )
        
        total_purchase_amount_text = f"${total_purchase_amount:,.2f}"
        total_purchase_count_text = f"{total_purchase_count}"
        
        return main_fig, top_items_fig, top_locations_fig, total_purchase_amount_text, total_purchase_count_text
    except Exception as e:
        print(f"Error updating graphs: {e}")
        return go.Figure(), go.Figure(), go.Figure(), '', ''

def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run_server(debug=True)
