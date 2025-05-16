Simple Flask Webserver on AWS ECS with Terraform and CI/CD
This repository contains a simple Flask web application deployed on AWS ECS Fargate behind an Application Load Balancer (ALB). Infrastructure is managed with Terraform, and CI/CD is automated using GitHub Actions.
________________________________________
Prerequisites
•	AWS CLI configured with credentials & permissions
•	Terraform installed (v1.x+ recommended)
•	Docker installed
•	GitHub account with repo access
________________________________________
Steps to Deploy
1. Clone the repository
bash
CopyEdit
git clone https://github.com/mukeshsaini143/ecs-cicd-application.git
cd ecs-cicd-application
________________________________________
2. Configure Terraform variables
Edit terraform.tfvars or create one with your AWS environment details, e.g.:
hcl
CopyEdit
aws_region = "us-west-1"
cluster_name = "webserver-cluster"
vpc_id = "your-vpc-id"
public_subnet_ids = ["subnet-xxxxxxxx", "subnet-yyyyyyyy"]
container_name = "webserver"
ecr_repo = "simple-webserver"
image_tag = "latest"
app_port = 5000
ecs_service_name = "simple-webserver-service"
________________________________________
3. Initialize and apply Terraform
Initialize Terraform providers and modules:
bash
CopyEdit
terraform init
Validate and apply the infrastructure:
bash
CopyEdit
terraform apply
Confirm the changes when prompted.
This will create:
•	ECS cluster
•	ALB with target group and listener
•	Security groups
•	IAM roles
•	ECS Task Definition & Service
________________________________________
4. Build and push Docker image (local or via GitHub Actions)
You can build and push the Docker image to AWS ECR manually:
bash
CopyEdit
$(aws ecr get-login --no-include-email --region us-west-1)
docker build -t simple-webserver .
docker tag simple-webserver:latest <aws_account_id>.dkr.ecr.us-west-1.amazonaws.com/simple-webserver:latest
docker push <aws_account_id>.dkr.ecr.us-west-1.amazonaws.com/simple-webserver:latest
Or, just push your code to GitHub and let the GitHub Actions workflow build and push automatically.
________________________________________
5. Access the Application
After deployment, get the ALB DNS name from Terraform output:
bash
CopyEdit
terraform output alb_dns_name
Open the URL in your browser:
cpp
CopyEdit
http://<alb-dns-name>/
You should see your Flask web server running.
________________________________________
6. Update and redeploy
Make code changes, commit, and push to GitHub. GitHub Actions will build and push new images, and ECS will update your service automatically.
________________________________________
Cleanup
To remove all deployed resources:
bash
CopyEdit
terraform destroy
________________________________________
Notes
•	Ensure your AWS credentials have permissions for ECS, ECR, IAM, VPC, and ALB.
•	Adjust security groups and subnet IDs based on your AWS environment.
•	Customize container configurations in the Terraform task definition as needed.


