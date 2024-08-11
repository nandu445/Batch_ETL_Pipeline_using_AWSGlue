import boto3

# Initialize S3 client
s3_client = boto3.client('s3', region_name='us-east-2')

# Upload the script to S3
s3_client.upload_file(
    'sales_etl_script.py', 
    'ecommerce-sales-etl-bucket', 
    'scripts/sales_etl_script.py'
)

