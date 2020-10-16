import json
import boto3


def lambda_handler(event, context):
    instanceID = 'ec2-34-216-1-195.us-west-2.compute.amazonaws.com'
    ec2 = boto3.client('ec2', region_name='us-west-2')
    ec2.stop_instances(InstanceIds=['i-07b5b982327a4f6f2'])

