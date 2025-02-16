This project is a real-time Python Dashboard using the dash, pandas, threading and plotly packages and libraries. 

The Dashboard opens to a new tab in default browser and features real-time updates. The CSV file serves as the data source, so that
any changes or data added to the CSV will automatically be updated in the dashboard. 
This shopping trend dashboard features useful analysis such as real-time purchase amounts and purchase updates, 
top 5 purchase items and top 5 locations. A filter function for location is also added. 

This project was created using the VS Code Python Extension. Git was used to commit and push the code to this repository.

The Timer function is used to open a web browser and run the Dash server. For fetching real-time data from the CSV file
at regular intervals, the dcc.Interval component in Dash is used. It triggers the callback function to reload the CSV data 
and update the graphs in real-time.

The Dash server is a powerful tool that allows users to interact with graphs and visualizations through a web browser.

Here's the Dashboard: (relative/path/to/dash.png)

