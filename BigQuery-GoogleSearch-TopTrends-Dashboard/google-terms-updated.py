from google.cloud import bigquery
import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import webbrowser
from threading import Timer
from datetime import datetime, timedelta

# Construct a BigQuery client object
client = bigquery.Client(project="chatbot-446403")

# Calculate the date range for the past 30 days
end_date = datetime.now().date()
start_date = end_date - timedelta(days=30)

# Define your query to select the top terms daily for the past 30 days
query_30_days = f"""
WITH daily_terms AS (
    SELECT 
        term, 
        DATE(week) AS date, 
        score, 
        rank,
        ROW_NUMBER() OVER (PARTITION BY DATE(week) ORDER BY score DESC) AS daily_rank
    FROM `bigquery-public-data.google_trends.international_top_terms`
    WHERE DATE(week) BETWEEN '{start_date}' AND '{end_date}'
)
SELECT term, date, score, rank
FROM daily_terms
WHERE daily_rank <= 5
ORDER BY date, rank
"""

# Execute the query with caching disabled and convert to DataFrame
print("Executing query...")
job_config = bigquery.QueryJobConfig(use_query_cache=False)
query_job_30_days = client.query(query_30_days, job_config=job_config)
df_30_days = query_job_30_days.to_dataframe()
print("Query executed and DataFrame created.")

# Print the query results
print(df_30_days.to_string(index=False))

# Extract data for the graph (top 5 terms for each day)
df_top5_30_days = df_30_days.groupby('date').head(5)

# Create the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Custom CSS for compact tables
table_style = {
    'font-size': '10px',
    'white-space': 'nowrap',
    'text-align': 'left',
    'line-height': '1.1'
}

# Layout of the app
app.layout = dbc.Container(fluid=True, children=[
    dbc.Row([
        dbc.Col([
            html.H1(f"Google Top Search Terms ({start_date} - {end_date})", className="text-center mb-4", style={'color': 'orange', 'font-family': 'Arial'}),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        dbc.Table.from_dataframe(df_30_days, striped=True, bordered=True, hover=True, responsive=True, style=table_style),
                    ], style={'color': 'orange', 'font-family': 'Arial'})
                ], width=6),
                dbc.Col([
                    html.H2("Top 5 Search Terms by Day", className="text-center", style={'color': 'skyblue', 'font-family': 'Arial'}),
                    dcc.Graph(
                        id='bar-graph-30-days',
                        figure=px.bar(df_top5_30_days, x='date', y='score', color='term', title='Top Search Terms by Day'),
                        config={'responsive': True}
                    )
                ], width=6)
            ])
        ], width=12)
    ])
])

# Function to open the browser
def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")

# Run the app and open the browser
if __name__ == '__main__':
    Timer(1, open_browser).start()  # Delay opening the browser by 1 second
    app.run_server(debug=True)
