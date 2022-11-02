import os
import json
import boto3

s3_client = boto3.client("s3")

def lambda_handler(event, context):
    
    # get bucket from environment variables
    bucket_name = os.environ['input_bucket']

    # get the input parameter from the lambda invocation
    specific_output = event['specific_output'][0]
    
    # load the outputs section of the tfstate in memory
    outputs_section_from_tf_state = json.loads(read_tfstate_file(bucket_name))['outputs']
    
    return {
        'statusCode' : 200,
        'body': json.dumps(get_outputs(specific_output, outputs_section_from_tf_state))
        }


def read_tfstate_file(bucket_name):
    # we will assume that in the bucket there will be only one terraform.tfstate file
    return s3_client.get_object(Bucket=bucket_name, Key='terraform.tfstate')["Body"].read()
  

def get_outputs(specific_output, all_outputs_from_state_file):
    
    if specific_output is not None:
        for output_item in all_outputs_from_state_file:
            return {specific_output: all_outputs_from_state_file[specific_output]}
    else:
        # by default we will return all output values
        return all_outputs_from_state_file
