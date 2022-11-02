data "archive_file" "python_lambda_package" {
  type        = "zip"
  source_file = "${path.module}/external/src/lambda_function.py"
  output_path = "${path.module}/external/out/lambda_code.zip"
}

resource "aws_lambda_function" "test_lambda_function" {
  function_name = var.lambda_name
  filename      = "${path.module}/external/out/lambda_code.zip"
  role          = aws_iam_role.lambda_role.arn
  runtime       = "python3.9"
  handler       = "lambda_function.lambda_handler"
  timeout       = 10
}

output "python_runtime" {
  value = aws_lambda_function.test_lambda_function.runtime
}
