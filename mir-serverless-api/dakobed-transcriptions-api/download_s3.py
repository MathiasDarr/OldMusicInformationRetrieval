import boto3
s3 = boto3.client('s3')

s3.download_file('dakobed-transcriptions', 'mddarr/funk.npy', '/data/mddarr/DakobedBard/funk.npy')