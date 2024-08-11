import boto3

# Define the location of the Glue script
bucket_name = 'ecommerce-sales-etl-bucket'
script_location = f's3://{bucket_name}/scripts/sales_etl_script.py'


glue_client = boto3.client('glue')
job_name = 'ECommerceSalesTransformETLJob'

job_response = glue_client.create_job(
    Name=job_name,
    Role='Glue_Sales_ETL_Role',
    ExecutionProperty={
        'MaxConcurrentRuns': 1
    },
    Command={
        'Name': 'glueetl',
        'ScriptLocation': script_location,
        'PythonVersion': '3'
    },
    DefaultArguments={
        '--TempDir': 's3://ecommerce-sales-etl-bucket/temp/',
        '--job-bookmark-option': 'job-bookmark-enable',
        '--job-language': 'python',
        '--enable-metrics': '',
        '--enable-continuous-log-filter': 'true',
        '--enable-spark-ui': 'true',
        '--REDSHIFT_DB': 'dev_ecommerce',
        '--REDSHIFT_TABLE': 'ecommerce_orders',
        '--REDSHIFT_USER': 'awsuser',
        '--REDSHIFT_PASSWORD': 'Password123',
        '--REDSHIFT_ENDPOINT': 'ecommerce-cluster.csdvfepxn6le.us-east-2.redshift.amazonaws.com',
        '--S3_TEMP_DIR': 's3://ecommerce-sales-etl-bucket/temp/'
    },
    MaxRetries=0,
    GlueVersion='3.0',
    NumberOfWorkers=2,
    WorkerType='G.1X'
)

print(f"Glue ETL Job '{job_name}' created successfully.")

# Start the Glue job
response = glue_client.start_job_run(JobName=job_name)

print(f"Glue ETL Job '{job_name}' started with JobRunId: {response['JobRunId']}")

