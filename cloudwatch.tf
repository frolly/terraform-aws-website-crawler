resource "aws_cloudwatch_log_group" "domain" {
  name = "${var.website_domain_name}"
  retention_in_days = 5
}

resource "aws_cloudwatch_log_group" "domain_get_sitemaps" {
  name = "${var.website_domain_name}_get_sitemaps"
  retention_in_days = 5
}

resource "aws_cloudwatch_log_group" "domain_get_urls" {
  name = "${var.website_domain_name}_get_urls"
  retention_in_days = 5
}

resource "aws_cloudwatch_log_group" "domain_put_urls" {
  name = "${var.website_domain_name}_put_urls"
  retention_in_days = 5
}

resource "aws_cloudwatch_log_group" "domain_put_urls_error" {
  name = "${var.website_domain_name}_put_urls_error"
  retention_in_days = 5
}
