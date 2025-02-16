This project is a real-time Python Dashboard using the dash, pandas, threading and plotly packages and libraries. 

The Dashboard opens to a new tab in default browser and features real-time updates. The CSV file serves as the data source, so that
any changes or data added to the CSV will automatically be updated in the dashboard. 
This shopping trend dashboard features useful analysis such as real-time purchase amounts and purchase updates, 
top 5 purchase items and top 5 locations. A filter function for location is also added. 

This project was created using the VS Code Python Extension. Git was used to commit and push the code to this repository.

The Timer function is used to open a web browser and run the Dash server. For fetching real-time data from the CSV file
at regular intervals, the dcc.Interval component in Dash is used. It triggers the callback function to reload the CSV data 
and update the graphs in real-time.

The Dash server is a powerful tool that allows users to interact with graphs and visualizations through a web browser. The Dash also 
allows the use of CSS to arrange a neat and compact dashboard. By using the FLexbox functionality (CSS), 

```python
app.layout = html.Div(style={'display': 'flex', 'flex-direction': 'row'}, children=[
```

the dashboard is created using 2 columns and several rows to arrange a compact Dashboard that fits the screen well. 

Here's the Dashboard:
![Dashboard](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/blob/main/dash.png)


By using the interval function, the real-time updates are set every second. The callback function updates the dashboard 
components at specific intervals and when certain filters are applied. 

    <i> dcc.Interval(
        id='interval-component',
        interval=1*1000,  
        n_intervals=0
    ) </i>

```python
@app.callback(
[Output('live-update-graph', 'figure'),
 Output('top-items-graph', 'figure'),
 Output('top-locations-graph', 'figure'),
 Output('total-purchase-amount', 'children'),
 Output('total-purchase-count', 'children')],
```

I have added another folder which contains a new real-time dashboard which makes use of Google Cloud and BigQuery data. 
Pandas, dash, dash_bootstrap_components, plotly, threading are used for this additional dashboard. The dashboard also opens
to a new tab in the default browsser tab. 

To use this new Dashboard, you must have your own BigQuery account. You can make use of the BigQuery Sandbox, a free account. 
Read up on this for instructions on how: <https://cloud.google.com/bigquery/docs/sandbox> 

You will also need to install the Google Cloud CLI <https://cloud.google.com/sdk/docs/install>. Make sure that the Google Cloud
CLI is set to PATH during installation. 

I made use of VS Code (using the Python extension) and installed the Google Cloud BigQuery extension. I also needed Google
Cloud's authorization and ran this: 

```
gcloud auth application-default login
```
This real-time dashboard simply fetches data from the bigquery-public-data.google-trends dataset using SQL within the Python code.
After fetching data, it then displays in a webbrowser the top google terms in a table and a graph.

BiqQuery Real-time Dashboard: 
![Dashboard](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/blob/main/BigQuery-GoogleSearch-TopTrends-Dashboard/bigquerydashboard_top-google-terms-last30-days.png)


