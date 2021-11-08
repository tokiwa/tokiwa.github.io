from __future__ import print_function

import json
import urllib
import boto3

print('*Loading lambda: s3FileListRead')

s3 = boto3.client('s3')

def lambda_handler(event, context):

    print('==== file list in bucket ====')
    AWS_S3_BUCKET_NAME = 'yujitokiwa-jp-test'
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(AWS_S3_BUCKET_NAME)
    result = bucket.meta.client.list_objects(Bucket=bucket.name, Delimiter='/')
    for o in result.get('Contents'):
        print(o.get('Key'))  # flie name will be printed
        response = s3.get_object(Bucket=bucket.name, Key=o.get('Key'))
        data = response['Body'].read()
        print(data.decode('utf-8'))  # file contents will be printed