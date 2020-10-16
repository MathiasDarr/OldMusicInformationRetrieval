import boto3
import json


sqs = boto3.resource('sqs')
s3 = boto3.client('s3')

transform_queue = sqs.get_queue_by_name(QueueName='TransformQueue')
for message in transform_queue.receive_messages():
    message.delete()


dakobed_transform_queue = sqs.get_queue_by_name(QueueName='DakobedTransformQueue')
for message in dakobed_transform_queue.receive_messages():
    message.delete()