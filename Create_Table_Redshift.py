import boto3

redshift_client = boto3.client('redshift')

cluster_identifier = 'ecommerce-cluster'

response = redshift_client.describe_clusters(ClusterIdentifier=cluster_identifier)
cluster_endpoint = response['Clusters'][0]['Endpoint']['Address']
print(f"Cluster endpoint: {cluster_endpoint}")


import psycopg2

# Redshift cluster connection details
host = "ecommerce-cluster.csdvfepxn6le.us-east-2.redshift.amazonaws.com"
port = "5439"  # default port for Redshift
dbname = "dev_ecommerce"
user = "awsuser"
password = "Password123"

# SQL statement to create a table
create_table_sql = """
CREATE TABLE IF NOT EXISTS ecommerce_orders (
    order_id BIGINT PRIMARY KEY,
    customer_id BIGINT,
    product_id BIGINT,
    quantity BIGINT,
    price DECIMAL(10,2),
    order_date TIMESTAMP,
    total_amount DECIMAL(10,2),
    product_name VARCHAR(100),
    stock_quantity BIGINT,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    gender VARCHAR(20)
);
"""

# Connect to Redshift cluster
try:
    conn = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )
    print("Connected to Redshift")

    # Create a cursor object
    cur = conn.cursor()

    # Execute the create table SQL statement
    cur.execute(create_table_sql)
    conn.commit()
    print("Table created successfully")

except Exception as e:
    print(f"Error: {e}")
finally:
    # Close the cursor and connection
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals():
        conn.close()
    print("Connection closed")

