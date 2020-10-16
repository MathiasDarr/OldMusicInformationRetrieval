import boto3



def handler(event, context):
    guitarset = 'tab'
    return {
        "statusCode": 200,
        "body": guitarset,
    }
