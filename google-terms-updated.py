import os
from datetime import datetime, timedelta

import pandas as pd
from google.cloud import bigquery

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table, Input, Output
import plotly.express as px

# ---------------- Config ----------------
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "chatbot-446403")
client = bigquery.Client(project=PROJECT_ID)

# Last 30 days window (table is weekly; this yields ~4–5 weeks)
END_DATE = datetime.now().date()
START_DATE = END_DATE - timedelta(days=30)

# ---------------- Queries ----------------
COUNTRIES_SQL = """
SELECT DISTINCT country_name
FROM `bigquery-public-data.google_trends.international_top_terms`
WHERE country_name IS NOT NULL
ORDER BY country_name
"""

TOP_TERMS_SQL = """
WITH weekly_terms AS (
  SELECT
    country_name,
    term,
    DATE(week) AS week_date,
    score,
    rank,
    ROW_NUMBER() OVER (
      PARTITION BY country_name, DATE(week)
      ORDER BY score DESC
    ) AS rnk
  FROM `bigquery-public-data.google_trends.international_top_terms`
  WHERE DATE(week) BETWEEN @start_date AND @end_date
    AND country_name = @country
)
SELECT
  country_name,
  term,
  week_date AS date,
  score,
  rank
FROM weekly_terms
WHERE rnk <= 5
ORDER BY date, rank
"""

def fetch_countries() -> list[str]:
    df = client.query(COUNTRIES_SQL, job_config=bigquery.QueryJobConfig(use_query_cache=True)).to_dataframe()
    return df["country_name"].dropna().tolist()

def fetch_top_terms(country: str, start_date: datetime.date, end_date: datetime.date) -> pd.DataFrame:
    job_config = bigquery.QueryJobConfig(
        use_query_cache=True,
        maximum_bytes_billed=1_000_000_000,
        query_parameters=[
            bigquery.ScalarQueryParameter("start_date", "DATE", start_date.isoformat()),
            bigquery.ScalarQueryParameter("end_date", "DATE", end_date.isoformat()),
            bigquery.ScalarQueryParameter("country", "STRING", country),
        ],
    )
    return client.query(TOP_TERMS_SQL, job_config=job_config).to_dataframe()

# ---------------- Data bootstrap ----------------
COUNTRIES = fetch_countries()
DEFAULT_COUNTRY = "Philippines" if "Philippines" in COUNTRIES else (COUNTRIES[0] if COUNTRIES else "")

# ---------------- App ----------------
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

table_style = dict(fontSize="12px", whiteSpace="nowrap", lineHeight="1.1")

app.layout = dbc.Container(fluid=True, children=[
    dbc.Row([
        dbc.Col([
            html.H1(
                id="title",
                className="text-center mb-3",
                style={"color": "orange", "fontFamily": "Arial"},
            ),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Country"),
                    dcc.Dropdown(
                        id="country-dropdown",
                        options=[{"label": c, "value": c} for c in COUNTRIES],
                        value=DEFAULT_COUNTRY,
                        placeholder="Select a country",
                        clearable=False,
                    ),
                ], width=4),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col([
                    html.H5("Weekly Top 5 Terms (Table)", className="mb-2"),
                    dash_table.DataTable(
                        id="terms-table",
                        columns=[
                            {"name": "date", "id": "date"},
                            {"name": "term", "id": "term"},
                            {"name": "score", "id": "score"},
                            {"name": "rank", "id": "rank"},
                        ],
                        data=[],
                        page_size=15,
                        style_table={"overflowX": "auto"},
                        style_cell=table_style,
                        sort_action="native",
                    ),
                ], width=6),
                dbc.Col([
                    html.H5("Weekly Top 5 Terms (Bar)", className="mb-2"),
                    dcc.Graph(id="bar-graph", config={"responsive": True}),
                ], width=6),
            ]),
        ], width=12),
    ]),
])

# ---------------- Callbacks ----------------
@app.callback(
    Output("title", "children"),
    Output("terms-table", "data"),
    Output("bar-graph", "figure"),
    Input("country-dropdown", "value"),
)
def update_country(country):
    title = f"Google Top Search Terms (Weekly) — {START_DATE} to {END_DATE}"
    if not country:
        return title, [], px.bar(title="No country selected")

    df = fetch_top_terms(country, START_DATE, END_DATE)

    if df.empty:
        fig = px.bar(title=f"No data for {country} in window")
        return f"{title} — {country}", [], fig

    # Table data
    table_data = df.to_dict("records")

    # Bar chart
    fig = px.bar(
        df,
        x="date",
        y="score",
        color="term",
        title=f"Top 5 Weekly Terms — {country}",
        barmode="group",
    )
    fig.update_layout(legend_title_text="term", xaxis_title="week", yaxis_title="score")

    return f"{title} — {country}", table_data, fig
