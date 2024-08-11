import json
import boto3

iam_client = boto3.client('iam')

# Define the role name
role_name = 'Glue_Sales_ETL_Role'

# Define the assume role policy that allows Glue to assume this role
assume_role_policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "glue.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

# Create the role
role_response = iam_client.create_role(
    RoleName=role_name,
    AssumeRolePolicyDocument=json.dumps(assume_role_policy_document),
    Description='Role to allow Glue to access S3, Glue Data Catalog, and Redshift'
)

# Define the S3 policy to allow access to the specific S3 bucket
s3_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::ecommerce-sales-etl-bucket",
                "arn:aws:s3:::ecommerce-sales-etl-bucket/*"
            ]
        }
    ]
}

# Create and attach the S3 policy
s3_policy_response = iam_client.put_role_policy(
    RoleName=role_name,
    PolicyName='S3AccessPolicy',
    PolicyDocument=json.dumps(s3_policy)
)

# Define the Glue policy to allow access to the Glue Data Catalog
glue_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "glue:*"
            ],
            "Resource": [
                "arn:aws:glue:*:024848463817:catalog",
                "arn:aws:glue:*:024848463817:database/ecommerce_sales_database",
                "arn:aws:glue:*:024848463817:table/ecommerce_sales_database/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "glue:GetConnection"
            ],
            "Resource": [
                "arn:aws:glue:us-east-2:024848463817:connection/RedshiftEcommerceConnection"
            ]
        }
    ]
}

# Create and attach the Glue policy
glue_policy_response = iam_client.put_role_policy(
    RoleName=role_name,
    PolicyName='GlueDataCatalogPolicy',
    PolicyDocument=json.dumps(glue_policy)
)

# Define the Redshift policy to allow access to the specific Redshift cluster
redshift_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "redshift:DescribeClusters",
                "redshift-data:ExecuteStatement",
                "redshift-data:DescribeStatement",
                "redshift-data:GetStatementResult",
                "redshift:GetClusterCredentials"
            ],
            "Resource": [
                "arn:aws:redshift:us-east-2:024848463817:namespace:bf960ccc-2d98-43c8-89da-1c542a197b98",
                "arn:aws:redshift:us-east-2:024848463817:namespace:bf960ccc-2d98-43c8-89da-1c542a197b98/*"
            ]
        }
    ]
}

# Create and attach the Redshift policy
redshift_policy_response = iam_client.put_role_policy(
    RoleName=role_name,
    PolicyName='RedshiftAccessPolicy',
    PolicyDocument=json.dumps(redshift_policy)
)

print("IAM role created with restricted policies attached.")
