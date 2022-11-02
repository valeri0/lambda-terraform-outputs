variable "lambda_name" {
  description = "Name of the lambda"
  type        = string
  default     = ""

}

variable "input_s3_bucket_name" {
  description = "Existing S3 bucket which contains the input terraform state file for the lambda function"
  type        = string
  default     = ""
}

variable "lambda_outputs_parameter" {
  description = "List of output names to be provided for the Lambda function to return from the terraform state file"
  type        = list(string)
  default     = []
}
