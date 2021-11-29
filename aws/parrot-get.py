import json

print('*Loading lambda: parrot-get')

def lambda_handler(event, context):
    response = event.get('queryStringParameters')
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'     
        },
        'body':json.dumps(response)
    }