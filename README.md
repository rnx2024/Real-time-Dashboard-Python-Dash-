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

<i>app.layout = html.Div(style={'display': 'flex', 'flex-direction': 'row'}, children=[</i>

the dashboard is created using 2 columns and several rows to arrange a compact Dashboard that fits the screen well. 

Here's the Dashboard:
![Dashboard](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/blob/main/dash.png)


The callback function in Dash updates the dashboard components at specific intervals (in milliseconds) and when certain filters are applied. 

    <i> dcc.Interval(
        id='interval-component',
        interval=1*1000,  
        n_intervals=0
    ) </i>

<i>@app.callback(
    [Output('live-update-graph', 'figure'),
     Output('top-items-graph', 'figure'),
     Output('top-locations-graph', 'figure'),
     Output('total-purchase-amount', 'children'),
     Output('total-purchase-count', 'children')],
    [Input('interval-component', 'n_intervals'),
     Input('location-filter', 'value')]</i>
