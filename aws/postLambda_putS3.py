import json
import boto3
from datetime import datetime

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    body = event["body"]
    print(body)
    bucket = 'hosei-ac-jp-xxxxxx'
    key = 'post_' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.txt'
    file_contents = body
    obj = s3.Object(bucket,key)
    obj.put( Body=file_contents )
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'     
        },
        'body': '{"message": "s3 put works"}'
    }