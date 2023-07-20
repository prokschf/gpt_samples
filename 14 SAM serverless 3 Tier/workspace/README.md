The AWS Serverless Application Model (SAM) is an open-source framework for building serverless applications. It extends AWS CloudFormation to provide a simplified way of defining the Amazon API Gateway APIs, AWS Lambda functions, and Amazon DynamoDB tables needed by your serverless application.

We will create a SAM template file, `template.yaml`, which will define our serverless application. This file will include the definition of our DynamoDB table, our two Lambda functions, and the API Gateway.

template.yaml
