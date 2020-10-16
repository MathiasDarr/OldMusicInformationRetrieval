import boto3
import json

def handler(event, context):
    transcription = -1

    try:
        params = event['pathParams']
        transcriptionId = params['transcriptionId']
        s3 = boto3.client('s3')
        s3.download_file('dakobed-guitarset', 'fileID{}/transcription.json'.format(transcriptionId), '/tmp/transcription.json')
        with open('/tmp/transcription.json') as f:
            transcription = json.load(f)
        transcription = transcription
    except Exception as e:
        print(e)

    return {
        "statusCode": 200,

        "body": transcription,
    }

