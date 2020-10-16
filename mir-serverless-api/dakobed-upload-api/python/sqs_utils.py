import boto3
import json
sqs = boto3.resource('sqs')
# queue = sqs.create_queue(QueueName='TransformQueue', Attributes={'DelaySeconds': '5'})

queue = sqs.get_queue_by_name(QueueName='TransformQueue')
userID = 'mddarr'
fileID = 0

response = queue.send_message(MessageBody= json.dumps( {'bucket':'dakobed-transcriptions', 'path': '{}/audio{}.wav'.format(userID, fileID)}))

sqs_client = boto3.client('sqs')

# sqs_client.
def send_sqs_librosa_transform(queue, userID, user, bucket, path):
    queue = sqs.get_queue_by_name(QueueName=queue)
    response = queue.send_message(MessageBody=json.dumps({'bucket': 'dakobed-transcriptions', 'path':path}))

send_sqs_librosa_transform('DakobedEC2Transforms', 'mddarr', 'dakobed-transcriptions', 'mddarr/audio.wav')