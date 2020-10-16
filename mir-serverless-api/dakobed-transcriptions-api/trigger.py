import boto3
import json


## This will trigger the Lambda function..



def trigger_ec2_launch_lambda():
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='DakobedEC2Transforms')
    queue.send_message( MessageBody=json.dumps({'bucket': 'dakobed-transcriptions', 'user': 'mddarr', 'path': 'mddarr/blues.wav'}))


def trigger_dakobed_transform_queue(path):
    sqs = boto3.resource('sqs')
    transform_queue = sqs.get_queue_by_name(QueueName="DakobedTransformQueue")
    transform_queue.send_message( MessageBody=json.dumps({'bucket': 'dakobed-transcriptions', 'user': 'mddarr', 'path': path}))


def trigger_dakobed_transcription_queue_lambda():
    sqs = boto3.resource('sqs')
    transform_queue = sqs.get_queue_by_name(QueueName="DakobedTranscriptionQueue")
    transform_queue.send_message( MessageBody=json.dumps({'bucket': 'dakobed-transcriptions', 'user': 'mddarr', 'path': 'mddarr/funk.npy'}))

trigger_dakobed_transcription_queue_lambda()