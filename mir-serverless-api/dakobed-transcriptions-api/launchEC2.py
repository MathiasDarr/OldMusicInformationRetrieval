import boto3
import time

user_data = '''#!/bin/bash -ex
        exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1
        echo BEGIN
        date '+%Y-%m-%d %H:%M:%S'
        
        cd /home/ubuntu
        aws s3 cp s3://dakobed-transcriptions/librosa_transforms_script.py .
        sudo python3 librosa_transforms_script.py
        sudo rm /var/lib/cloud/instance/sem/config_scripts_user

'''

install_script = '''
        sudo apt update
        sudo apt --assume-yes install awscli
        sudo apt --assume-yes install python3-pip
        sudo apt-get --assume-yes install libsndfile1-dev
        pip3 install librosa
        pip3 install boto3
        
    
'''

remove_this_file_rerun_user_data_startup = '/var/lib/cloud/instance/sem/config_scripts_user'




ec2 = boto3.resource('ec2', region_name='us-west-2')
#ami = 'ami-003634241a8fcdec0'

ami = 'ami-03ecf2760168d28b4'


instance = ec2.create_instances(
    ImageId=ami,
    MinCount=1,
    MaxCount=1,
    KeyName='corwin',
    InstanceInitiatedShutdownBehavior='terminate',
    IamInstanceProfile={'Name': 'S3fullaccess'},
    InstanceType='t2.micro',
    SecurityGroupIds=['sg-09c4618f69b2e5910'],
    UserData=user_data
)


