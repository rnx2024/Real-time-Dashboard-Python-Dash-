import os
import time
import math
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

CSV_PATH = os.getenv("CSV_PATH", "shopping-trends.csv")
CSV_CACHE_TTL = int(os.getenv("CSV_CACHE_TTL", "60"))  # seconds

# ------- simple cache (per process) -------
_cache = {"df": None, "mtime": None, "loaded_at": 0.0}

def _read_csv() -> pd.DataFrame:
    df = pd.read_csv(CSV_PATH)
    df["Purchase Amount (USD)"] = pd.to_numeric(df["Purchase Amount (USD)"], errors="coerce").fillna(0)
    return df

def get_data() -> pd.DataFrame:
    try:
        mtime = os.path.getmtime(CSV_PATH)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Item Purchased", "Location", "Purchase Amount (USD)"])
    now = time.time()
    needs_reload = (
        _cache["df"] is None
        or (now - _cache["loaded_at"]) > CSV_CACHE_TTL
        or _cache["mtime"] != mtime
    )
    if needs_reload:
        df = _read_csv()
        _cache.update(df=df, mtime=mtime, loaded_at=now)
    return _cache["df"]

# preload once for dropdown options
base_df = get_data()

palette = ['#4e79a7', '#59a14f', '#9c755f', '#f28e2b', '#edc948', '#e15759', '#76b7b2', '#ff9da7', '#af7aa1']

app = dash.Dash(__name__)
app.layout = html.Div(style={'display': 'flex', 'flex-direction': 'row'}, children=[
    html.Div(style={'flex': '50%', 'padding': '10px'}, children=[
        html.H1('Real-Time Shopping Trends Dashboard', style={'font-family': 'Arial', 'font-size': '30px', 'color': '#800000'}),
        html.Div(style={'display': 'flex', 'justify-content': 'space-between'}, children=[
            html.Div(id='total-purchase-amount', style={'font-family': 'Arial', 'font-size': '48px', 'color': '#377eb8'}),
            html.Div(id='total-purchase-count', style={'font-family': 'Arial', 'font-size': '48px', 'color': '#ff7f00'})
        ]),
        html.Div(style={'display': 'flex', 'justify-content': 'space-between'}, children=[
            html.Div('Total Purchase Amount', style={'font-family': 'Arial', 'font-size': '24px', 'color': '#777'}),
            html.Div('Total Purchase Count', style={'font-family': 'Arial', 'font-size': '24px', 'color': '#777'})
        ]),
        dcc.Graph(id='live-update-graph', animate=True, style={'height': '50vh'}),
    ]),
    html.Div(style={'flex': '50%', 'padding': '10px'}, children=[
        html.Label('Filter by Location', style={'font-family': 'Arial', 'font-size': '18px'}),
        dcc.Dropdown(
            id='location-filter',
            options=[{'label': loc, 'value': loc} for loc in sorted(base_df['Location'].dropna().unique())],
            multi=True,
            placeholder='Select locations',
            style={'font-family': 'Arial', 'font-size': '16px', 'margin-bottom': '20px'}
        ),
        dcc.Graph(id='top-items-graph', style={'height': '40vh'}),
        dcc.Graph(id='top-locations-graph', style={'height': '40vh'}),
    ]),
    # consider 30000–60000 ms for non-real-time dashboards
    dcc.Interval(id='interval-component', interval=int(os.getenv("DASH_INTERVAL_MS", "1000")), n_intervals=0)
])

@app.callback(
    [
        Output('live-update-graph', 'figure'),
        Output('top-items-graph', 'figure'),
        Output('top-locations-graph', 'figure'),
        Output('total-purchase-amount', 'children'),
        Output('total-purchase-count', 'children'),
    ],
    [
        Input('interval-component', 'n_intervals'),
        Input('location-filter', 'value'),
    ]
)
def update_graphs(_, selected_locations):
    try:
        data = get_data()

        if selected_locations:
            data = data[data['Location'].isin(selected_locations)]

        if data.empty:
            empty_fig = go.Figure()
            return empty_fig, empty_fig, empty_fig, "$0.00", "0"

        total_amt = data['Purchase Amount (USD)'].sum()
        total_cnt = int(len(data))

        by_item = (
            data.groupby('Item Purchased', as_index=False)['Purchase Amount (USD)']
            .sum()
            .sort_values('Purchase Amount (USD)', ascending=False)
        )
        colors = (palette * math.ceil(len(by_item) / len(palette)))[:len(by_item)]

        main_fig = go.Figure(
            data=[go.Bar(
                x=by_item['Item Purchased'],
                y=by_item['Purchase Amount (USD)'],
                marker=dict(color=colors)
            )],
            layout=go.Layout(title='Real-Time Data', xaxis=dict(title='Item Purchased'), yaxis=dict(title='Purchase Amount (USD)'))
        )

        top_items = by_item.head(5)
        top_items_fig = go.Figure(
            data=[go.Bar(
                x=top_items['Item Purchased'],
                y=top_items['Purchase Amount (USD)'],
                marker=dict(color=colors[:len(top_items)])
            )],
            layout=go.Layout(title='Top 5 Items', xaxis=dict(title='Item Purchased'), yaxis=dict(title='Total Purchase Amount (USD)'))
        )

        top_items_filter = data['Item Purchased'].isin(top_items['Item Purchased'])
        top_locations = (
            data[top_items_filter]
            .groupby('Location', as_index=False)['Purchase Amount (USD)']
            .sum()
            .sort_values('Purchase Amount (USD)', ascending=False)
            .head(5)
        )
        top_locations_fig = go.Figure(
            data=[go.Bar(
                x=top_locations['Location'],
                y=top_locations['Purchase Amount (USD)'],
                marker=dict(color=palette[:len(top_locations)])
            )],
            layout=go.Layout(title='Top 5 Locations', xaxis=dict(title='Location'), yaxis=dict(title='Total Purchase Amount (USD)'))
        )

        return (
            main_fig,
            top_items_fig,
            top_locations_fig,
            f"${total_amt:,.2f}",
            f"{total_cnt}",
        )
    except Exception as e:
        print(f"Error updating graphs: {e}")
        empty = go.Figure()
        return empty, empty, empty, "$0.00", "0"

if __name__ == "__main__":
    app.run_server(debug=True)
