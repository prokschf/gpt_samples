import boto3
import os

def lambda_handler(event, context):
    lambda_client = boto3.client('lambda')
    response = lambda_client.invoke(
        FunctionName=os.getenv('GET_PICTURE_FUNCTION'),
        InvocationType='RequestResponse',
        Payload=event
    )
    return {
        'statusCode': 200,
        'body': response['Payload'].read()
    }
