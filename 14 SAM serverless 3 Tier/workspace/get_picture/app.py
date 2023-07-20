import boto3
import os

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.getenv('TABLE_NAME'))
    picture_id = event['pathParameters']['id']
    response = table.get_item(Key={'id': picture_id})
    return {
        'statusCode': 200,
        'body': response['Item']
    }
