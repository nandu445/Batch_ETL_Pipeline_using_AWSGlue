import boto3

glue_client = boto3.client('glue')

crawler_name = 'ECommerceSalesCrawler'
database_name = 'ecommerce_sales_database'
table_name = 'etl_'

glue_client.create_database(DatabaseInput={'Name': database_name})

glue_client.create_crawler(
    Name=crawler_name,
    Role='Glue_Sales_ETL_Role',  # The IAM role created in the previous step
    DatabaseName=database_name,
    Targets={'S3Targets': [{'Path': f's3://ecommerce-sales-etl-bucket/'}]},
    TablePrefix=table_name
)

# Start the crawler
glue_client.start_crawler(Name=crawler_name)

print("Glue Crawler created and started.")
