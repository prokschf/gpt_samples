curl -o terraform.zip https://releases.hashicorp.com/terraform/0.14.7/terraform_0.14.7_linux_amd64.zip
unzip terraform.zip
rm terraform.zip
chmod +x terraform
mv terraform ~/.local/bin/

terraform init

terraform apply

curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
rm get-docker.sh

docker build -t your-dockerhub-username/backend:latest -f Dockerfile.backend .
docker build -t your-dockerhub-username/frontend:latest -f Dockerfile.frontend .
docker build -t your-dockerhub-username/fluentd:latest -f Dockerfile.fluentd .

docker login --username=your-dockerhub-username --password=your-dockerhub-password
docker push your-dockerhub-username/backend:latest
docker push your-dockerhub-username/frontend:latest
docker push your-dockerhub-username/fluentd:latest

curl -X POST -H "Accept: application/vnd.github.v3+json" -H "Authorization: token your-github-token" https://api.github.com/repos/your-github-username/your-repo-name/actions/workflows/backend.yml/dispatches --data '{"ref":"main"}'
curl -X POST -H "Accept: application/vnd.github.v3+json" -H "Authorization: token your-github-token" https://api.github.com/repos/your-github-username/your-repo-name/actions/workflows/frontend.yml/dispatches --data '{"ref":"main"}'
