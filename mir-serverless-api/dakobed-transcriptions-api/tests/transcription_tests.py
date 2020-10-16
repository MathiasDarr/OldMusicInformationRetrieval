import boto3
import pytest
import json

@pytest.fixture()
def sqs_client():
    '''SNS client'''
    return boto3.client('sqs')


def test_sqs_send_message():
    sqs = boto3.resource('sqs')
    #queue = sqs.create_queue(QueueName='DakobedTestQueue', Attributes={'DelaySeconds': '5'})
    queue = sqs.get_queue_by_name(QueueName="DakobedTestQueue")
    response = queue.send_message(MessageBody=json.dumps({'bucket': 'dakobed-test-bucket', 'user': 'mddarr', 'path':'mddarr/blues.wav'}))
    assert response['ResponseMetadata']['HTTPStatusCode'] == 200

test_sqs_send_message()