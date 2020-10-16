import json
import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('DakobedGuitarSet')
    data = table.scan()
    guitarset = data['Items']

    return {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Methods': 'OPTIONS,GET,POST,PUT,PATCH,DELETE'
        },
        "body": guitarset,
    }
