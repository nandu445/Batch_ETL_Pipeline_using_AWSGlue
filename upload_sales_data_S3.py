import boto3

# Initialize S3 client
s3_client = boto3.client('s3', region_name='us-east-2')

# Create S3 bucket
bucket_name = 'ecommerce-sales-etl-bucket'
s3_client.create_bucket(ACL='private', Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint':'us-east-2'})
print("bucket created")

#Upload data from local file system
customer_data = 'Customer.csv'
product_data = 'Product.csv'
order_details = 'Order.csv'

s3_client.upload_file(customer_data, bucket_name, customer_data)

s3_client.upload_file(product_data, bucket_name, product_data)

s3_client.upload_file(order_details, bucket_name, order_details)

print("Dataset uploaded to S3 bucket:", bucket_name)
