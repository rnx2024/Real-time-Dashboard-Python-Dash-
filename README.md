# Real-Time Dashboards Created with Plotly and Dash


This project is a collection of real-time Python Dashboards using the dash, pandas, plotly, boto3, googlecloud-bigquery, sqlalchemy packages.

1. Dataset-based Dashboard. The Dashboard opens to a new tab in default browser and features real-time updates. The CSV file serves as the data source, so that
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

2. BigQuery Dashboard. [![Button1](https://img.shields.io/badge/Click%20Me-BigQueryDashboard%20Code%20File-red)](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/blob/main/google-top-terms-addl-filters.py) This dashboard for Top Google Search terms has a location filter.The top search terms (weekly) within the last 30 days are visualized in a table and graph. 

To use this new Dashboard, you must have your own BigQuery account. You can make use of the BigQuery Sandbox, which is free. 
Read up on this for instructions on how: [![Button1](https://img.shields.io/badge/Click%20Me-BigQuerySandbox-purple)](https://cloud.google.com/bigquery/docs/sandbox)

You will also need to install the Google Cloud CLI [![Button2](https://img.shields.io/badge/Click%20Me-InstallGoogleCloudCLI-orange)](https://cloud.google.com/sdk/docs/install). 
Make sure that the Google Cloud CLI is set to PATH during installation. 

I made use of VS Code (using the Python extension) and also installed the Google Cloud BigQuery extension. I also needed Google
Cloud's authorization and ran this: 

```
gcloud auth application-default login
```
This real-time dashboard simply fetches data from the bigquery-public-data.google-trends dataset using SQL within the Python code.
After fetching data, it then displays in a webbrowser the top google terms in a table and a graph.

Here's the dashboard:
![Dashboard](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/blob/main/dashboard-with-filter.png)

3. AWS Cloud S3 Dashboard. [![Button1](https://img.shields.io/badge/Click%20Me-AWS%20Dashboard%20Files-pink)](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/tree/main/AWSCloud-PythonDash) An AWS Cloud S3 Dashboard is added. This makes use of a dataset from an AWS Cloud S3 bucket. It retrieves the data from the S3 bucket and load it to memory. It makes use of the callback function to make real-time updates. For a medium dataset, loading it to a dataframe memory is quite manageable. For larger datasets, pyspark will have to be the more efficient use. The boto3 package is used here which allows the easy interaction with AWS Cloud within Python.

This is the AWS Cloud S3 bucket Dashboard with a filter for location and summary statistics: 
![Dashboard](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/blob/main/AWSCloud-PythonDash/dashboard_awss3bucket_dataset.png)

Another code file was added [![Button3](https://img.shields.io/badge/Click%20Me-AWSS3ImprovedDashboard-blue)](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/blob/main/AWSCloud-PythonDash/awss3bucket_improved_dash.py) which enhanced the design of the dashboard. Additional sytling were added to the summary statistics and the dropdown menu.

Here's the improved dashboard:
![Dashboard](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/blob/main/AWSCloud-PythonDash/awsclouds3bucket_enhanced-dashboard-design.png)

4. MySQL Dashboard. [![Button4](https://img.shields.io/badge/Click%20Me-MySQL%20Dashboard%20Files-gold)](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/tree/main/MYSQL_Dashboard)
   A Delivery Performance Dashboard is added. Data is fetched from MySQL using SQLAlchemy and pandas to interact with MySQL.

The dashboard provides the following features:

Monthly Filter: Select a month to filter the data and visualize performance for the chosen period.

Top Customer Areas: Displays the top 5 customer areas in a pie chart, highlighting the distribution of customers.

Top Feedback/Sentiment: Shows the most common feedback category for each month in a bar chart, offering insights into customer feedback trends.

Total Order Value: Provides the total value of orders for the selected month, giving a quick overview of sales performance.

Average Delivery Time Difference: Calculates and displays the average difference between promised and actual delivery times, helping to assess delivery efficiency.

Data processing and visualization are handled using the pandas library and Plotly for creating interactive graphs and charts. 
The dashboard is built with Dash and Bootstrap for a responsive and user-friendly interface.

Here's the new dashboard:
![Dashboard](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/blob/main/MYSQL_Dashboard/MySQL%20Plotly_Dash.png)

The MYSQL_Dashboard folder contains all the code for data_fetching, callbacks, layouts and the actual app deployment. The MySQL credentials which were used to access the database were replaced with generic credentials but you can change these according to your MySQL credentials. The dataset used can be downloaded at [![Button4](https://img.shields.io/badge/Click%20Me-BlinkitDataset-green)](https://www.kaggle.com/datasets/arunkumaroraon/blinkit-grocery-dataset). These full datasets were migrated to MySQL database using the MySQL Workbench. If you do not have the MySQL or Workbench, you can download it here [![Button5](https://img.shields.io/badge/Click%20Me-DownloadMySQL-red)](https://dev.mysql.com/downloads/) based on your system requirements. 

Changes mades to the dataset during migration: As MySQL have certain rules for date formats (yyyy-mm-dd), these were changed during the migration. Certain column names with reserved words in MySQL such as date, channel were also changed to facilitate full and accurate data migration. The date for the blinkit_inventorynew dataset were all changed to yyyy-mm-dd from the format mm-dd and appended with year 2024. 

