output "alb_dns_name" {
  description = "ALB DNS Name"
  value       = aws_lb.app_lb.dns_name
}

