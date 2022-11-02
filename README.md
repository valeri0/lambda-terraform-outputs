# lambda-terraform-outputs

Small terraform project which deploys a lambda that is used for retrieving terraform outputs from a given terraform state file from an S3 bucket.

## Setup

1. Create an aws profile in `~/.aws/credentials` file.
2. Export the profile name using `export TF_VAR_AWS_PROFILE=<profile_name>`
