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

client = bigquery.Client(project="chatbot-446403")

end_date = datetime.now().date()
start_date = end_date - timedelta(days=30)

def get_query(country_name):
    return f"""
    WITH daily_terms AS (
        SELECT 
            term, 
            DATE(week) AS date, 
            score, 
            rank,
            ROW_NUMBER() OVER (PARTITION BY DATE(week), country_name ORDER BY score DESC) AS daily_rank
        FROM `bigquery-public-data.google_trends.international_top_terms`
        WHERE DATE(week) BETWEEN '{start_date}' AND '{end_date}'
        AND country_name = '{country_name}'
    )
    SELECT term, date, score, rank
    FROM daily_terms
    WHERE daily_rank <= 5
    ORDER BY date, rank
    """

def execute_query(country_name):
    query = get_query(country_name)
    print("Executing query...")
    job_config = bigquery.QueryJobConfig(use_query_cache=False)
    query_job = client.query(query, job_config=job_config)
    df = query_job.to_dataframe()
    print("Query executed and DataFrame created.")
    return df

def get_countries():
    query = """
    SELECT DISTINCT country_name
    FROM `bigquery-public-data.google_trends.international_top_terms`
    """
    query_job = client.query(query)
    df = query_job.to_dataframe()
    return df['country_name'].tolist()


initial_country_name = 'United States'
df_30_days = execute_query(initial_country_name)


df_top5_30_days = df_30_days.groupby('date').head(5)


available_countries = get_countries()


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


table_style = {
    'font-size': '10px',
    'white-space': 'nowrap',
    'text-align': 'left',
    'line-height': '1.1'
}

# Dashboard layout
app.layout = dbc.Container(fluid=True, children=[
    dbc.Row([
        dbc.Col([
            html.H1(f"Google Top Search Terms ({start_date} - {end_date})", className="text-center mb-4", style={'color': 'orange', 'font-family': 'Arial'}),
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.Div([
                dbc.Table(id='data-table', striped=True, bordered=True, hover=True, responsive=True, style=table_style),
            ], style={'color': 'orange', 'font-family': 'Arial'})
        ], width=6),
        dbc.Col([
            html.Label('Select Country:'),
            dcc.Dropdown(
                id='country-dropdown',
                options=[{'label': country, 'value': country} for country in available_countries],
                value=initial_country_name
            ),
            html.H2("Top 5 Search Terms", className="text-center mt-4", style={'color': 'skyblue', 'font-family': 'Arial'}),
            dcc.Graph(
                id='bar-graph-30-days',
                figure=px.bar(df_top5_30_days, x='date', y='score', color='term', title='Top Search Terms by Day'),
                config={'responsive': True}
            )
        ], width=6)
    ])
])


@app.callback(
    [Output('bar-graph-30-days', 'figure'),
     Output('data-table', 'children')],
    [Input('country-dropdown', 'value')]
)
def update_data(country_name):
    df_30_days = execute_query(country_name)
    df_top5_30_days = df_30_days.groupby('date').head(5)
    figure = px.bar(df_top5_30_days, x='date', y='score', color='term', title=f'Top Search Terms ({country_name})')

    table = dbc.Table.from_dataframe(df_30_days, striped=True, bordered=True, hover=True, responsive=True, style=table_style)

    return figure, table


def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")


if __name__ == '__main__':
    Timer(1, open_browser).start()  
    app.run_server(debug=True)