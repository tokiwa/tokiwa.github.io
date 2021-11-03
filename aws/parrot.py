import json

print('*Loading lambda: parrot')

def lambda_handler(event, context):
    body = event["body"]
    print(body)
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'     
        },
        'body':body
    }