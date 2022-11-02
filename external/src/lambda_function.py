import boto3
import os

s3_client = boto3.client("s3")

def lambda_handler(event, context):
    desired_outputs = event['outputs']
    bucket_name = os.environ['input_bucket']
    
    file_content = read_tfstate_file(bucket_name)
    print(file_content)


def read_tfstate_file(bucket_name):
    return s3_client.get_object(Bucket=bucket_name, Key='terraform.tfstate')["Body"].read()
  
      