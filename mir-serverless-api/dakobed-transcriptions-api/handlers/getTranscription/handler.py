import json
import boto3
import uuid

from botocore.exceptions import ClientError


def handler(event, context):
    transcriptionID = event['pathParams']['transcriptionId']
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('DakobedTranscriptions')
    try:
        response = table.get_item(Key={'id': transcriptionID})
    except ClientError as e:
        print(e.response['Error']['Message'])

    return response['Item']