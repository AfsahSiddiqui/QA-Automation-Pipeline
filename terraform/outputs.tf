output "bucket_name" {
  value = aws_s3_bucket.test_reports.bucket
}

output "bucket_id" {
  value = aws_s3_bucket.test_reports.id
}

output "bucket_arn" {
  value = aws_s3_bucket.test_reports.arn
}