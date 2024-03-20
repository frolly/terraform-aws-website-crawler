resource "aws_s3_bucket" "bucket_website_sitemaps" {
  bucket = lower("${var.tag_entity}-${var.tag_project}-sitemaps")
  force_destroy = true
}

resource "aws_s3_bucket" "bucket_website_pages" {
  bucket = lower("${var.tag_entity}-${var.tag_project}-pages")
  force_destroy = true
}

resource "aws_s3_bucket_ownership_controls" "bucket_website_pages_ownership_controls" {
  bucket = aws_s3_bucket.bucket_website_pages.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket_public_access_block" "bucket_website_pages_public_access_block" {
  bucket = aws_s3_bucket.bucket_website_pages.id
  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_s3_bucket_acl" "bucket_website_pages_bucket_acl" {
  depends_on = [
    aws_s3_bucket_ownership_controls.bucket_website_pages_ownership_controls,
    aws_s3_bucket_public_access_block.bucket_website_pages_public_access_block,
  ]
  bucket = aws_s3_bucket.bucket_website_pages.id
  acl    = "public-read"
}