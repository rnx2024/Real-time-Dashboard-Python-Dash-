from google.cloud import bigquery

# Construct a BigQuery client object
client = bigquery.Client()

# Define a simple query
query = """
SELECT 
    term, 
    DATE(week) AS date, 
    score, 
    rank
FROM `bigquery-public-data.google_trends.international_top_terms`
LIMIT 10
"""

# Execute the query
query_job = client.query(query)
df = query_job.to_dataframe()

# Print the query results
print(df)
