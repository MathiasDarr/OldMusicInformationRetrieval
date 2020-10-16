import boto3


def get_s3_client():
    return boto3.client('s3')

def list_s3_buckets():
    s3 = get_s3_client()
    response = s3.list_buckets
    if response:
        for bucket in response.get('Buckets', []):
            yield bucket['Name']

def list_s3_objects(bucket):
    """
    List s3 objects in a bucket
    :param bucket:
    :return:
    """
    s3 = get_s3_client()
    response = s3.list_objects(Bucket = bucket)
    if response:
        for _object in response.get('Contents', []):
            yield _object['Key']


def read_s3_object(bucket, key):
    s3 = get_s3_client()
    response = s3.get_object(Bucket=bucket, Key=key)
    if response:
        return response['Body'].read()