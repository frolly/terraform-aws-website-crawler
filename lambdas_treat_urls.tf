resource "aws_lambda_function" "lambda_treat_urls" {
  filename      = "${path.module}/lambdas/lambda_treat_urls_function_payload.zip"
  function_name = "${var.tag_entity}-${var.tag_project}-treat-urls"
  role          = aws_iam_role.iam_for_lambda_crawler.arn
  handler       = "treat_urls.init"

  source_code_hash = "${filebase64sha256("${path.module}/lambdas/lambda_treat_urls_function_payload.zip")}"

  runtime = var.lambda_python_version
  memory_size = 2048
  timeout = 900

  skip_destroy = false
  
  environment {
    variables = {
      bucket_website_sitemaps = lower("${var.tag_entity}-${var.tag_project}-sitemaps")
      bucket_website_pages    = lower("${var.tag_entity}-${var.tag_project}-pages")
      website_domain_name     = var.website_domain_name
      website_sitemap_index   = var.website_sitemap_index
      sqs_website_sitemaps    = "${var.tag_entity}-${var.tag_project}-sitemaps-queue"
      sqs_website_sitemaps_dl = "${var.tag_entity}-${var.tag_project}-sitemaps-queue-deadletter"
      sqs_website_pages       = "${var.tag_entity}-${var.tag_project}-urls-queue"
      sqs_website_pages_dl    = "${var.tag_entity}-${var.tag_project}-urls-queue-deadletter"
      cw_log_group_domain     = aws_cloudwatch_log_group.domain.name
      cw_log_group_sitemaps   = aws_cloudwatch_log_group.domain_get_sitemaps.name
      cw_log_group_get_urls   = aws_cloudwatch_log_group.domain_get_urls.name
      cw_log_group_put_urls   = aws_cloudwatch_log_group.domain_put_urls.name
      cw_log_group_err_urls   = aws_cloudwatch_log_group.domain_put_urls_error.name
    }
  }
}

resource "aws_cloudwatch_log_group" "lambda_treat_urls_log_group" {
  name = "/aws/lambda/${var.tag_entity}-${var.tag_project}-treat-urls"
  retention_in_days = 5
  lifecycle {
    create_before_destroy = true
    prevent_destroy       = false
  }
}
