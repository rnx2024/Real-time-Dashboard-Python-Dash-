from sqlalchemy import create_engine
import pandas as pd

# Database configuration
user = 'username'
password = 'password'
host = '127.0.0.1'
database = 'name_of_your_database'

# Create an SQLAlchemy engine
engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

# Fetch data from MySQL tables
delivery_data_query = """
SELECT 
    blinkit_delivery_performance.promised_time, 
    blinkit_delivery_performance.actual_time, 
    blinkit_orders.actual_delivery_time,
    MONTH(blinkit_orders.actual_delivery_time) as month 
FROM 
    blinkit_delivery_performance 
INNER JOIN 
    blinkit_orders 
ON 
    blinkit_delivery_performance.order_id = blinkit_orders.order_id
"""
delivery_data = pd.read_sql(delivery_data_query, engine)

customer_data_query = """
SELECT area, MONTH(blinkit_customers.registration_date) as month 
FROM blinkit_customers
"""
customer_data = pd.read_sql(customer_data_query, engine)

order_data_query = """
SELECT order_total, MONTH(blinkit_orders.order_date) as month 
FROM blinkit_orders
"""
order_data = pd.read_sql(order_data_query, engine)

feedback_data_query = """
SELECT 
    sentiment,
    MONTH(feedback_date) as month 
FROM 
    blinkit_customer_feedback
"""
feedback_data = pd.read_sql(feedback_data_query, engine)

# Export the data frames
__all__ = ['delivery_data', 'customer_data', 'order_data', 'feedback_data']
