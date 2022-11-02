# lambda-terraform-outputs

Small terraform project which deploys a lambda that is used for retrieving terraform outputs from a given terraform state file from an S3 bucket.

## Setup

1. Create an aws profile in `~/.aws/credentials` file with the account access key and secret key.
2. Export the profile name using `export AWS_PROFILE=<profile_name>`
3. Configure the `terraform.tfvars` with the following values:
   ```
   lambda_name = <value>
   input_s3_bucket_name = <value>
   ```

## Running the Lambda

The lambda function returns outputs from the `terraform.tfstate` file from the `input_s3_bucket_name` which is configured in the `terraform.tfvars`.

If no input is given for the lambda invocation, then it will automatically provide the entire `outputs` section from the state file.

Otherwise, if an input that respects the following format:

```
{
    "specific_output": "<output_name>"
}
```

is provided, then it will a return the following response:

```
{
  "statusCode": 200,
    "body": {
    "<specific_output_name>": {
      "value": "<string>",
      "type": "<type>"
    }
  }
}
}
```

If an output name which does not exist in the tfstate file is provided, then the Lambda function will return:

```
{
  "statusCode": 404,
  "body": "No such output has been found for: <specific_output_name>"
}
```
