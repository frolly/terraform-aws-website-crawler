variable "tag_entity" {
  description = "Tag Entity"
  type        = string
  default     = "TOTO"
}
variable "tag_project" {
  description = "Tag Project"
  type        = string
  default     = "Crawler"
}

variable "tag_environment" {
  description = "Tag Environment"
  type        = string
  default     = "dev"
}

variable "website_domain_name" {
  description = "Website Domain Name"
  type        = string
  default     = "www.example.com"
}

variable "website_sitemap_index" {
  description = "Website Sitemap Index"
  type        = string
  default     = "sitemap.xml"
}

variable "lambda_python_version" {
  description = "Lambda python version"
  type        = string
  default     = "python3.12"
}
