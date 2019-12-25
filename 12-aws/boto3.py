##################################################
#  Boto3 
##################################################

# Boto3 is the name of the Python SDK for AWS. It allows you to directly create, update, and delete AWS resources from your Python scripts.


'''
credentials
'''

# Step 1: create an IAM user with programmatic access to AWS

# Step 2: save credentials in ~/.aws/credentials
# [default]
# aws_access_key_id = YOUR_ACCESS_KEY_ID
# aws_secret_access_key = YOUR_SECRET_ACCESS_KEY

# Step 3: create default config in ~/.aws/config
# [default]
# region = YOUR_PREFERRED_REGION


'''
client vs. resource vs. session 
'''
# Client:
# low-level AWS service access
# generated from AWS service description
# exposes botocore client to the developer
# typically maps 1:1 with the AWS service API
# all AWS service operations are supported by clients
# snake-cased method names (e.g. ListBuckets API => list_buckets method)

# Resource:
# higher-level, object-oriented API
# generated from resource description
# uses identifiers and attributes
# has actions (operations on resources)
# exposes subresources and collections of AWS resources
# does not provide 100% API coverage of AWS services

# Session:
# stores configuration information (primarily credentials and selected region)
# allows you to create service clients and resources
# boto3 creates a default session for you when needed

# The boto3 module acts as a proxy to the default session, which is created automatically when needed. Example default session use:
# Using the default session
sqs = boto3.client('sqs')
s3 = boto3.resource('s3')


# client
# pass in the name of the service to connect to 
import boto3 
s3_client = boto3.client('s3')

# resource: high-level object-oriented service access
import boto3 
s3_resource = boto3.resource('s3')

# you can access the client directly via the resource like s3_resource.meta.client

# With clients, there is more programmatic work to be done. The majority of the client operations give you a dictionary response. 
# To get the exact information that you need, you’ll have to parse that dictionary yourself.
# With resource methods, the SDK does that work for you.

# session object 
# Boto3 will create the session from your credentials. 

'''
s3 examples
'''
# https://realpython.com/python-boto3-aws-s3/
# create a bucket 
# generate a bucket with uuid to make it unique 
import uuid 
def create_bucket_name(bucket_prefix):
    return ''.join([bucket_prefix, str(uuid.uuid4())])

s3_resource.create_bucket(Bucket=YOUR_BUCKET_NAME,
                          CreateBucketConfiguration = {
                              'LocationConstraint': 'eu-west-1'
                          })

# better approach, take the region from the session state 
def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_resource = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': current_region})
    print(bucket_name, current_region)
    return bucket_name, current_region

first_bucket_name, first_response = create_bucket(
    bucket_prefix='firstpythonbucket', 
    s3_connection=s3_resource.meta.client)

# the below gives back a Bucket instance as the bucket_response
second_bucket_name, second_response = create_bucket(
    bucket_prefix='secondpythonbucket', s3_connection=s3_resource)

# by using the resource, you have access to high-level classes like Bucket and Object 
first_bucket = s3_resource.Bucket(name=first_bucket_name)
first_object = s3_resource.Object(
    bucket_name=first_bucket_name, key=first_file_name)

# upload file using object or bucket or client
# object
first_object.upload_file(first_file_name)
# bucket
first_bucket.upload_file(
    Filename=first_file_name, Key=first_file_name)
# client 
s3_resource.meta.client.upload_file(
    Filename=first_file_name, Bucket=first_bucket_name,
    Key=first_file_name
)

# download file 
s3_resource.Object(first_bucket_name, first_file_name).download_file(
    f'/tmp/{first_file_name}') 

# copy an object between buckets 
def copy_to_bucket(bucket_from_name, bucket_to_name, file_name):
    copy_source = {
        'Bucket': bucket_from_name,
        'Key': file_name
    }
    s3_resource.Object(bucket_to_name, file_name).copy(copy_source)

copy_to_bucket(first_bucket_name, second_bucket_name, first_file_name)

'''
s3 examples - official docs 
'''
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-creating-buckets.html

# create an s3 bucket 
import logging 
import boto3
from botocore.exceptions import ClientError 

def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else: 
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint':region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False 
    return True 

# list existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')


# upload files
# upload_file method accepts a file name, bucket name, and object name
# handles large file by splitting into chuncks and handl each in parallel
def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    if object_name is None:
        object_name = file_name 
    
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False 
    return True 

s3 = boto3.client('s3')
with open("FILE_NAME", "rb") as f:
    s3.upload_fileobj(f, "BUCKET_NAME", "OBJECT_NAME")

# download files 
# The download_file method accepts the names of the bucket and object to download and the filename to save the file to.
s3 = boto3.client('s3')
s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')

# The download_fileobj method accepts a writeable file-like object. 
# The file object must be opened in binary mode, not text mode.
s3 = boto3.client('s3')
with open('FILE_NAME', 'wb') as f:
    s3.download_fileobj('BUCKET_NAME', 'OBJECT_NAME', f)


'''
EC2 examples
'''
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-managing-instances.html

# describe instances
import boto3 

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)

import sys 
import boto3
from botocore.exceptions import ClientError 

instance_id = sys.argv[2]
action = sys.argv[1].upper()

ec2 = boto3.client('ec2')

if action == 'ON':
    try: 
        ec2.start_instance(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e: 
        if 'DryRunOperation' not in str(e):
            raise 
    
    # dry run succeeded, run start_instance without dry run 
    try: 
        response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
    


'''
Secrets Manager examples
'''
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/secrets-manager.html

# get secrets 

def get_secret():
    secret_name = "MySecretName"
    region_name = "us-west-2"

    session = boto3.session.Session()
    client = session.client(
        service_name = 'secretsmanager',
        region_name = region_name,
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name 
        )
    except ClientError as e: 
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print("The requested secret " + secret_name + " was not found")
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            print("The request was invalid due to:", e)
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print("The request had invalid params:", e)
    else:
        # Secrets Manager decrypts the secret value using the associated KMS CMK
        # Depending on whether the secret was a string or binary, only one of these fields will be populated
        if 'SecretString' in get_secret_value_response:
            text_secret_data = get_secret_value_response['SecretString']
        else:
            binary_secret_data = get_secret_value_response['SecretBinary']
