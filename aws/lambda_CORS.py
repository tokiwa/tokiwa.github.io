def lambda_handler(event, context):
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'     
        },
        'body': '{"message": "Hello from AWS Lambda"}'
    }