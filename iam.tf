data "aws_iam_policy_document" "lambda_assume_role_policy" {
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

data "aws_iam_policy_document" "lambda_s3_get_object" {
  statement {
    sid       = "AllowGetObjectForLambda"
    effect    = "Allow"
    actions   = ["s3:GetObject"]
    resources = ["arn:aws:s3:::${var.input_s3_bucket_name}/*"]
  }
}

resource "aws_iam_policy" "lambda_s3_get_object" {
  name   = "lambda_s3_get_object_policy"
  path   = "/"
  policy = data.aws_iam_policy_document.lambda_s3_get_object.json
}

resource "aws_iam_role" "lambda_role" {
  name               = "lambdaRole"
  assume_role_policy = data.aws_iam_policy_document.lambda_assume_role_policy.json

}

resource "aws_iam_policy_attachment" "policy_attachment" {
  name       = "lambda_role_policy_attachment"
  roles      = [aws_iam_role.lambda_role.name]
  policy_arn = aws_iam_policy.lambda_s3_get_object.arn

}
