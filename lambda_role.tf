data "aws_iam_policy_document" "assume_role_for_lambda_crawler" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_policy" "policy_for_lambda_crawler" {
  name = "${var.tag_entity}-${var.tag_project}-lambda-policy"
  description = "${var.tag_entity} ${var.tag_project} crawler lambda policy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = [
          "logs:*",
          "s3:*",
          "dynamodb:*",
          "sqs:*",
          "cloudwatch:*"
        ]
        Resource = ["*"]
      }
    ]
  })
}

resource "aws_iam_role" "iam_for_lambda_crawler" {
  name               = "${var.tag_entity}-${var.tag_project}-iam_for_lambda_crawler"
  assume_role_policy = data.aws_iam_policy_document.assume_role_for_lambda_crawler.json
}

resource "aws_iam_role_policy_attachment" "iam_role_policy_attachment_for_lambda_crawler" {
  role       = "${aws_iam_role.iam_for_lambda_crawler.name}"
  policy_arn = "${aws_iam_policy.policy_for_lambda_crawler.arn}"
}