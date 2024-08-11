import json
import boto3

iam_client = boto3.client('iam')

# Define the role name
role_name = 'Redshift_Ecomerce_Role'

# Define the assume role policy that allows Glue to assume this role
assume_role_policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "redshift.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

# Create the role
role_response = iam_client.create_role(
    RoleName=role_name,
    AssumeRolePolicyDocument=json.dumps(assume_role_policy_document),
    Description='Redshift Role'
)

iam_client.attach_role_policy(
        RoleName=role_name,
        PolicyArn="arn:aws:iam::aws:policy/AmazonRedshiftFullAccess"
)
