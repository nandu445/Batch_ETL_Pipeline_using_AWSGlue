# Batch_ETL_Pipeline_using_AWSGlue
Batch ETL pipeline that transforms and load data from S3 bucket to redshift cluster

Objective: 
To design and build a batch ETL pipeline in AWS Glue. This pipeline will enable glue to extract raw data from S3 bucket. A Glue Crawler will catalog the raw data. A Glue job will run a Glue script to perform transformations on data and store it into Redshift Cluster. This transformend data should be consistent, clean and in a format supported for querying.

Tech Stack:
1.	ETL Tool: AWS Glue
2.	Data Source: Amazon S3 (Source)
3.	Data Cataloging: AWS Glue Crawler
4.	Transformation Engine: AWS Glue Job
5.	Data Warehouse: Amazon Redshift (Target)
6.	Security: IAM

Work Flow:
1.	Data Storage: Store raw sales data in S3.
2.	Data Cataloging: Use Glue Catalog by running a Glue Crawler to catalog the raw data.
3.	ETL Job: Create a Glue ETL job to transform the raw data into a suitable format for analysis.
4.	Data Loading: Load the transformed data into a table in Redshift cluster

Steps:
1.	Load raw data in S3 bucket
2.	If there is an existing table in Redshift, proceed to next step.
Create IAM role for redshift, then create a cluster. Create a table in the required schema in the redshift cluster.
3.	Create IAM role for Glue to access S3, Redshift, and Glue data catalog
4.	Create and run a glue crawler to catalog the raw data
5.	Write a script to transform the raw data in S3 into required format and specify the    target location. Upload this script to S3
6.	Create and run Glue ETL Job that executes the script from S3

Repository Structure:
1. Customer.csv, Product.csv, Order.csv	: Raw data files
2. upload_sales_data_s3.py : Creates an s3 bucket and uploads raw data into it
3. Create_IAMRole_Redshift.py :	Creates IAM role for Redshift
4. Create_Redshift_Cluster.py	: Creates redshift cluster
5. Create_Table_Redshift.py	: Creates a table in redshift
6. Create_iam_role.py	: Creates IAM role for Glue to access S3, Glue and Redshift
7. Create_Glue_Crawler.py	: Create and run Glue Crawler
8. Sales_etl_script.py	: Script for applying transformations on data
9. Upload_GlueETL_Script.py :	Upload the script to S3 bucket
10. Create_Glue_Job.py :	Create and run Glue ETL Job

Conclusion - 
Built a batch etl pipeline that successfully transforms data from s3 bucket and load into a table in redshift cluster.


