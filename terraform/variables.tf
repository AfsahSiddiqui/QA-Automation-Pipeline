variable "aws_region" {
  description = "AWS region where resources will be created"
  type        = string
  default     = "us-east-1"
}

variable "bucket_name" {
  description = "S3 bucket for storing test reports"
  type        = string
  default     = "qa-automation-logs-afsah"
}