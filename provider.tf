provider "aws" {
  default_tags {
    tags = {
        Name        = "${var.tag_entity}-${var.tag_project}-crawler-urls"
        Entity      = var.tag_entity
        Project     = var.tag_project
        Environment = var.tag_environment
    }
  }
}