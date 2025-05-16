variable "aws_region" {
  default = "us-west-1"
}

variable "cluster_name" {
  default = "webserver-cluster"
}

variable "container_name" {
  default = "webserver"
}

variable "ecr_repo" {
  default = "simple-webserver"
}

variable "image_tag" {
  default = "latest"
}

variable "app_port" {
  default = 5000
}
variable "ecs_service_name" {
  default = "simple-webserver-service"
} 
variable "vpc_id" {}

variable "public_subnet_ids" {
  type = list(string)
}

