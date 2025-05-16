
# Simple Flask Webserver on AWS ECS with Terraform and CI/CD
## 1. Clone the repository

To deploy this project run

```bash
git clone https://github.com/mukeshsaini143/ecs-cicd-application.git
cd ecs-cicd-application

```
## 2. Configure Terraform variables

terraform.tfvars or create one with your AWS environment details, e.g.:

```bash
aws_region = "us-west-1"
cluster_name = "webserver-cluster"
vpc_id = "your-vpc-id"
public_subnet_ids = ["subnet-xxxxxxxx", "subnet-yyyyyyyy"]
container_name = "webserver"
ecr_repo = "simple-webserver"
image_tag = "latest"
app_port = 5000
ecs_service_name = "simple-webserver-service"


```
## 3. Initialize and apply Terraform

Initialize Terraform providers and modules:

```bash
terraform init

```
Validate, plan and apply the infrastructure:

```bash
terraform plan
terraform apply

```
Confirm the changes when prompted.
This will create:

•	ECS cluster

•	ALB with target group and listener

•	Security groups

•	IAM roles

•	ECS Task Definition & Service

## 4. Build and push Docker image (local or via GitHub Actions)
You can build and push the Docker image to AWS ECR manually:

```bash
$(aws ecr get-login --no-include-email --region us-west-1)
docker build -t simple-webserver .
docker tag simple-webserver:latest <aws_account_id>.dkr.ecr.us-west-1.amazonaws.com/simple-webserver:latest
docker push <aws_account_id>.dkr.ecr.us-west-1.amazonaws.com/simple-webserver:latest

```
Or, just push your code to GitHub and let the GitHub Actions workflow build and push automatically.
## 5. Access the Application
After deployment, get the ALB DNS name from Terraform output:
```bash
terraform output alb_dns_name
```
Open the URL in your browser:
```bash
http://<alb-dns-name>/
```
You should see your Flask web server running.
## 6. Update and redeploy
Make code changes, commit, and push to GitHub. GitHub Actions will build and push new images, and ECS will update your service automatically.
## Cleanup
To remove all deployed resources:
```bash
terraform destroy
```
## Notes
•	Ensure your AWS credentials have permissions for ECS, ECR, IAM, VPC, and ALB.

•	Adjust security groups and subnet IDs based on your AWS environment.

•	Customize container configurations in the Terraform task definition as needed.


