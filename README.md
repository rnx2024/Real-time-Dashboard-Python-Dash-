This project are collection of real-time Python Dashboards using the dash, pandas, threading and plotly, and boto3 packages and libraries. 

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

To use this new Dashboard, you must have your own BigQuery account. You can make use of the BigQuery Sandbox, which is free. 
Read up on this for instructions on how: <https://cloud.google.com/bigquery/docs/sandbox> 

You will also need to install the Google Cloud CLI <https://cloud.google.com/sdk/docs/install>. Make sure that the Google Cloud
CLI is set to PATH during installation. 

I made use of VS Code (using the Python extension) and also installed the Google Cloud BigQuery extension. I also needed Google
Cloud's authorization and ran this: 

```
gcloud auth application-default login
```
This real-time dashboard simply fetches data from the bigquery-public-data.google-trends dataset using SQL within the Python code.
After fetching data, it then displays in a webbrowser the top google terms in a table and a graph.

BiqQuery Real-time Dashboard: 
![Dashboard](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/blob/main/BigQuery-GoogleSearch-TopTrends-Dashboard/bigquerydashboard_top-google-terms-last30-days.png)

The code for the BigQuery dataset has been edited (gooogle-terms-with-filter.py) to feature a location filter. By choosing a location filter, the top search terms (weekly) within the last 30 days are visualized in the table and graph. 

Here's the new dashboard:
![Dashboard](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/blob/main/dashboard-with-filter.png)

An AWS Cloud S3 Dashboard is added. This makes use of a dataset within an AWS Cloud S3 bucket. It retrieves the data from the S3 bucket and load it to memory. It makes use of the callback function to make real-time updates. For a medium dataset, loading it to a dataframe memory is quite manageable. For larger datasets, pyspark will have to be the more efficient use. The boto3 package is used here which allows the easy interaction with AWS Cloud within Python.

This is the AWS Cloud S3 bucket Dashboard with a filter for location and summary statistics: 
![Dashboard](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/blob/main/AWSCloud-PythonDash/dashboard_awss3bucket_dataset.png)

Another code file was added <https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/blob/main/AWSCloud-PythonDash/awss3bucket_improved_dash.py>
which enhanced the design of the dashboard. Additional sytling were added to the summary statistics and the dropdown menu.

Here's the improved dashboard:
![Dashboard](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/blob/main/AWSCloud-PythonDash/awsclouds3bucket_enhanced-dashboard-design.png)
