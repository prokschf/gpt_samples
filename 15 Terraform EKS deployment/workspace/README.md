The architecture will be divided into several parts:

1. Terraform scripts for infrastructure setup.
2. GitHub Actions workflows for the backend and frontend.
3. Dockerfiles for the backend, frontend, and Fluentd sidecar.

Let's start with the Terraform scripts.

**main.tf**

This is the entry point for Terraform. It will call modules to create the EKS cluster, RDS instance, and necessary IAM roles.

