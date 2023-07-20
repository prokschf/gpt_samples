# Install AWS SAM CLI
pip install --user aws-sam-cli

# Validate the SAM template
sam validate -t template.yaml

# Build the SAM application
sam build

# Deploy the SAM application
sam deploy --guided
