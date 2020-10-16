import json
import boto3


def handler(event, context):
    guitarset = 'hello'
    return {
        "statusCode": 200,
        "body": guitarset,
    }
