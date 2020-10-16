import json
import boto3
import numpy as np
from keras.models import load_model

def generate_windowed_samples(spec):
    '''
    This method creates the context window for a sample at time t, Wi-2, Wi-1, Wi, Wi+1,Wi+2
    '''
    windowed_samples = np.zeros((spec.shape[0], 5, spec.shape[1]))
    for i in range(spec.shape[0]):
        if i <= 1:
            windowed_samples[i] = np.zeros((5, spec.shape[1]))
        elif i >= spec.shape[0] - 2:
            windowed_samples[i] = np.zeros((5, spec.shape[1]))
        else:
            windowed_samples[i, 0] = spec[i - 2]
            windowed_samples[i, 1] = spec[i - i]
            windowed_samples[i, 2] = spec[i]
            windowed_samples[i, 3] = spec[i + 1]
            windowed_samples[i, 4] = spec[i + 2]
    return windowed_samples


def preprocess(spectogram):
    mean = np.load('/opt/python/guitarset-mean.npy')
    var = np.load('/opt/python/guitarset-var.npy')
    spec = generate_windowed_samples(spectogram - mean) / var
    return np.expand_dims(spec, axis=-1)


def lambda_handler(event, context):
    records = event['Records'][0]
    body = records['body']
    sqs = boto3.client('sqs')
    dakobed_transform_queue = sqs.get_queue_by_name(QueueName="DakobedTransformQueue")



    try:
        parsed_json = json.loads(body)
        transform_path = parsed_json['path']
        wavpath = parsed_json['wavpath']
        user = parsed_json['user']
        print("The path is " + transform_path)
        bucket = parsed_json['bucket']
        s3 = boto3.client('s3')
        s3.download_file(bucket, transform_path, '/tmp/cqt.npy')
        cqt = np.load('/tmp/cqt.npy')
        processed_spectogram = preprocess(cqt)
        model = load_model('/opt/python/model1.h5')
        predictions = model.predict(processed_spectogram)




        print("predictions shape")

        dakobed_transform_queue.send_message(MessageBody=json.dumps({'type':'transcription', 'user':user, 'wavpath':wavpath, 'bucket':bucket}))

        print(predictions.shape)
    except Exception as e:
        print(e)

    guitarset = 'hello'

    return {
        "statusCode": 200,
        "body": guitarset,
    }
