"""
Lambda function which retrieves outputs from a remote terraform state file from S3
"""

import os
import json
import boto3

s3_client = boto3.client("s3")

def lambda_handler(event, context):
    # get bucket from environment variables
    bucket_name = os.environ['input_bucket']

    # get the input parameter from the lambda invocation
    specific_output = event.get('specific_output', None)

    # load the outputs section of the tfstate in memory
    outputs_section_from_tf_state = json.loads(read_tfstate_file(bucket_name))['outputs']

    code, body = get_outputs(specific_output, outputs_section_from_tf_state)
    return {
        'statusCode' : code,
        'body': body
        }

def read_tfstate_file(bucket_name):
    # we will assume that in the bucket there will be only one terraform.tfstate file
    return s3_client.get_object(Bucket=bucket_name, Key='terraform.tfstate')["Body"].read()

def get_outputs(specific_output, all_outputs_from_state_file):
    
    if specific_output is None:
        # by default, if no specific output is provided, we will return all output values
        return 200, all_outputs_from_state_file
    else:
       # check if required output does exist
       if all_outputs_from_state_file.get(specific_output, None) is None:
           return 404, 'No such output has been found for: ' + specific_output
       
       # return specific output
       return 200, {specific_output: all_outputs_from_state_file[specific_output]}

