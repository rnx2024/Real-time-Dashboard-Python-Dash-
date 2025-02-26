# Real-Time Dashboards Created with Plotly and Dash

<br>
<br>
<div style="text-align: center;">
  <img src="https://revenue.ai/wp-content/uploads/2023/06/Plotly-1.png" alt="Plotly" width="100" height="100">
  <img src="https://thumbs.dreamstime.com/b/dash-icon-flat-illustration-dash-vector-icon-web-dash-icon-flat-style-114331438.jpg" alt="Dash" width="100" height="100">
  <img src="https://www.liblogo.com/img-logo/aw314s096-aws-s3-logo-setting-up-aws-s3-for-open-edx-blog.png" alt="AWS S3" width="100" height="100">
  <img src="https://www.selectdistinct.co.uk/wp-content/uploads/2023/03/Google-Big-Query-jpg.webp" alt="Google Big Query" width="100" height="100">
  <img src="https://e7.pngegg.com/pngimages/747/798/png-clipart-mysql-logo-mysql-database-web-development-computer-software-dolphin-marine-mammal-animals.png" alt="MySQL" width="100" height="100">
  <img src="https://directdevops.blog/wp-content/uploads/2019/03/boto3.jpeg" alt="Boto3" width="100" height="100">
  <img src="https://play-lh.googleusercontent.com/ARKZLqwqNpLiFYPABKjRdSmhSMqvLojpgSpXmapJFZI3PudmsHoqkjjOFycUOuHqBQ" alt="Google Drive" width="100" height="100">
  <img src="https://www.seekpng.com/png/detail/348-3481904_images-pandas-logo-pandas-python-logo.png" alt="Pandas" width="100" height="100">
</div>

<br>
<br>

This project is a collection of real-time Python Dashboards using the dash, plotly, pandas, boto3, googlecloud-bigquery, sqlalchemy packages.

It provides Dash app codes on how to integrate Python with different data sources: local CSV file, from a database, and cloud clients such as BigQuery and AWS S3. This incluedes: 

- environment setup (modules and packages to be used)
- how to connect to data source
- how to fetch data through pandas, boto3, bigquery client, mysql connector and SQLAlchemy from different data sources
- how to create graphs and charts by using dash, plotly
- how to implement range and dropdown filters 
- how to use callbacks in Dash to provide real-time interactive updates for visuals
  

1. Dataset-based Dashboard. [![Button2](https://img.shields.io/badge/Download-KaggleDataset-blue)](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/blob/main/real-time_dashboard.py)
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

To run the code, you will need the following: 

- A BigQuery account. You can make use of the BigQuery Sandbox, which is free. 
  - Read up on this for instructions on how: [![Button1](https://img.shields.io/badge/Click%20Me-BigQuerySandbox-purple)](https://cloud.google.com/bigquery/docs/sandbox)

* Google Cloud CLI [![Button2](https://img.shields.io/badge/Click%20Me-InstallGoogleCloudCLI-orange)](https://cloud.google.com/sdk/docs/install). 
Make sure that the Google Cloud CLI is set to PATH during installation. 

- Google Cloud's authorization. Run this to get authorization and login before running the code: 

```
gcloud auth application-default login
```
This real-time dashboard simply fetches data from the bigquery-public-data.google-trends dataset using SQL within the Python code. 

Here's the dashboard:
![Dashboard](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/blob/main/dashboard-with-filter.png)

3. AWS Cloud S3 Dashboard. [![Button1](https://img.shields.io/badge/Click%20Me-AWS%20Dashboard%20Files-pink)](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/tree/main/AWSCloud-PythonDash) An AWS Cloud S3 Dashboard is added. This makes use of a dataset from an AWS Cloud S3 bucket. It retrieves the data from the S3 bucket and load it to memory. It makes use of:

- callback function to update data based on selected location
- dropdown location filter
- graphs and piecharts to visualize data using plotly and dash

For a medium dataset, loading it to a dataframe memory is quite manageable. For larger datasets, pyspark will have to be the more efficient use. The boto3 package is used here which allows the easy interaction with AWS Cloud within Python. 

This is the AWS Cloud S3 bucket Dashboard with a filter for location and summary statistics: 
![Dashboard](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/blob/main/AWSCloud-PythonDash/dashboard_awss3bucket_dataset.png)

Another code file was added [![Button3](https://img.shields.io/badge/Click%20Me-AWSS3ImprovedDashboard-blue)](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/blob/main/AWSCloud-PythonDash/awss3bucket_improved_dash.py) which enhanced the design of the dashboard. Changes made were: 

- Styles for the summary statistics to improve visuals

Here's the improved dashboard:
![Dashboard](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/blob/main/AWSCloud-PythonDash/awsclouds3bucket_enhanced-dashboard-design.png)

4. MySQL Dashboard. [![Button4](https://img.shields.io/badge/Click%20Me-MySQL%20Dashboard%20Files-gold)](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/tree/main/MYSQL_Dashboard)
   A Delivery Performance Dashboard is added. Data is fetched from MySQL using SQLAlchemy and pandas to interact with MySQL.

The dashboard provides the following features:

- Monthly Filter: Select a month to filter the data and visualize performance for the chosen period.
- Top Customer Areas: Displays the top 5 customer areas in a pie chart, highlighting the distribution of customers.
- Top Feedback/Sentiment: Shows the most common feedback category for each month in a bar chart, offering insights into customer feedback trends.
- Total Order Value: Provides the total value of orders for the selected month, giving a quick overview of sales performance.
- Average Delivery Time Difference: Calculates and displays the average difference between promised and actual delivery times, helping to assess delivery efficiency.

Data processing and visualization are handled using the pandas library and Plotly for creating interactive graphs and charts. 
The dashboard is built with Dash and Bootstrap for a responsive and user-friendly interface.

Here's the new dashboard:
![Dashboard](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/blob/main/MYSQL_Dashboard/MySQL%20Plotly_Dash.png)

The MYSQL_Dashboard folder contains all the code for data_fetching, callbacks, layouts and the actual app deployment. The MySQL credentials which were used to access the database were replaced with generic credentials but you can change these according to your MySQL credentials. The dataset used can be downloaded at [![Button4](https://img.shields.io/badge/Click%20Me-BlinkitDataset-green)](https://www.kaggle.com/datasets/arunkumaroraon/blinkit-grocery-dataset). These full datasets were migrated to MySQL database using the MySQL Workbench. If you do not have the MySQL or Workbench, you can download it here [![Button5](https://img.shields.io/badge/Click%20Me-DownloadMySQL-red)](https://dev.mysql.com/downloads/) based on your system requirements. 

Changes made to the dataset during migration: As MySQL have certain rules for date formats (yyyy-mm-dd), these were changed during the migration. Certain column names with reserved words in MySQL such as date, channel were also changed to facilitate full and accurate data migration. The date for the blinkit_inventorynew dataset were all changed to yyyy-mm-dd from the format mm-dd and appended with year 2024. 

![Button6](https://img.shields.io/badge/NOTE:-UPDATE-green) Changes to the code to derive more significant insights and focused on Customer Feedback. The dashboard now features:

- A monthly filter
- A feedback category filter
- A donut pie showing top locations based on the month selected
- A bar graph that show total sentiment counts based on selected month and feedback category
- Total order value based on selected month
- Average delivery time difference (between promised time and actual delivery time) based on selected month

This dashboard now provides more comprehensive insights into customer feedback and its relation to total order value and delivery time performance, and top customer locations. 

Here's new dashboard: 
![Dashboard](https://github.com/rnx2024/Real-time-Dashboard-Python-Dash-/blob/main/MYSQL_Dashboard/Customer%20Feedback%20Dashboard.png)

