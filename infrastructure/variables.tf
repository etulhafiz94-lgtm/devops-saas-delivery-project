variable "aws_region" {
  description = "AWS region used for the infrastructure"
  type        = string
  default     = "eu-central-1"
}

variable "project_name" {
  description = "Name used to identify project resources"
  type        = string
  default     = "devops-saas"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "development"
}