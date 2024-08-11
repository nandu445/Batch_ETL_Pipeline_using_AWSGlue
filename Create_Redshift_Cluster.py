import boto3

redshift_client = boto3.client('redshift')

# Define the Redshift cluster parameters
cluster_identifier = 'ecommerce-cluster'
db_name = 'dev_ecommerce'
master_username = 'awsuser'
master_user_password = 'Password123'
node_type = 'dc2.large'
number_of_nodes = 2  

response = redshift_client.create_cluster(
    ClusterIdentifier=cluster_identifier,
    DBName=db_name,
    MasterUsername=master_username,
    MasterUserPassword=master_user_password,
    NodeType=node_type,
    NumberOfNodes=number_of_nodes,
    IamRoles=['arn:aws:iam::024848463817:role/Redshift_Ecomerce_Role'],  # Attach the Glue IAM role
)

print(f"Redshift cluster '{cluster_identifier}' is being created.")