import boto3
import botocore
import json
import time

config = botocore.config.Config(
    read_timeout=900,
    connect_timeout=900,
    retries={"max_attempts": 0}
)

# boto3.set_stream_logger('')
session = boto3.Session()
client = session.client("lambda", config=config, endpoint_url="http://127.0.0.1:3001",)

response = client.invoke(
    FunctionName='HelloWorldFunction',
    InvocationType="RequestResponse",
)

response_payload = response['Payload'].read()
