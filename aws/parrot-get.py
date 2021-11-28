import json

print('*Loading lambda: parrot-get')

def lambda_handler(event, context):
    # TODO implement
    name = event['queryStringParameters']['name']
    role = event['queryStringParameters']['role']
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'     
        },
        'body':json.dumps('name:'+ name + ' role:' + role)
    }