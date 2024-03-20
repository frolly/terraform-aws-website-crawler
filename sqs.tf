resource "aws_sqs_queue" "sqs_queue_sitemaps" {
    name                        = "${var.tag_entity}-${var.tag_project}-sitemaps-queue"
    delay_seconds               = 90
    max_message_size            = 2048
    message_retention_seconds   = 86400
    receive_wait_time_seconds   = 10
    visibility_timeout_seconds  = aws_lambda_function.lambda_get_urls.timeout
    redrive_policy = jsonencode({
        deadLetterTargetArn = aws_sqs_queue.sqs_queue_deadletter_sitemaps.arn
        maxReceiveCount     = 4
    })
}

resource "aws_sqs_queue" "sqs_queue_deadletter_sitemaps" {
    name = "${var.tag_entity}-${var.tag_project}-sitemaps-queue-deadletter"
}

resource "aws_lambda_event_source_mapping" "event_source_mapping_sitemaps" {
  event_source_arn = aws_sqs_queue.sqs_queue_sitemaps.arn
  enabled          = true
  function_name    = aws_lambda_function.lambda_get_urls.arn
  batch_size       = 1
}

resource "aws_sqs_queue" "sqs_queue_pages" {
    name                        = "${var.tag_entity}-${var.tag_project}-urls-queue"
    delay_seconds               = 90
    max_message_size            = 2048
    message_retention_seconds   = 86400
    receive_wait_time_seconds   = 10
    visibility_timeout_seconds  = aws_lambda_function.lambda_treat_urls.timeout
    redrive_policy = jsonencode({
        deadLetterTargetArn = aws_sqs_queue.sqs_queue_deadletter_pages.arn
        maxReceiveCount     = 4
    })
}

resource "aws_sqs_queue" "sqs_queue_deadletter_pages" {
    name = "${var.tag_entity}-${var.tag_project}-urls-queue-deadletter"
}

resource "aws_lambda_event_source_mapping" "event_source_mapping_pages" {
  event_source_arn = aws_sqs_queue.sqs_queue_pages.arn
  enabled          = true
  function_name    = aws_lambda_function.lambda_treat_urls.arn
  batch_size       = 1
}