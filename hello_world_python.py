# requestsは、pip install requests　にてPythonを実行するディレクトリにインストールしておく。
import requests
import json

# AWSに送信するJSONを指定する。
payload = {'key1': 'value1', 'key2': 'value2'}
# URLはAWSのAPI GatewayのURLに変更する
url = 'https://unedgij7n6.execute-api.ap-northeast-1.amazonaws.com/default/hello_world_python'
# AWSのEndPointにpostで要求した結果を r に代入する
r = requests.post(url,data=json.dumps(payload))

# AWSより返されるデータ形式
print(type(r))
# Status Codeを表示する。200：リクエスト成功
print(r.status_code)
# 返されたヘッダーを表示する
print(r.headers)
# 返されたデータをすべて表示する
print(r.json())
# keyを指定してvalueを取り出す
print(r.json()["key1"])
# AWSから返されたjsonのすべてのキーとバリューを表示する
for key, val in (r.json()).items():
    print(key, val)

# AWS Lambda Code
# AWSのLambdaはPythonコードに記載されているpayloadのデータがそのまま返される。
#
# import json
# print('*Loading lambda: hello_World_python')
# def lambda_handler(event, context):
#     body = event["body"]
#     print(body)
#     return {
#         'isBase64Encoded': False,
#         'statusCode': 200,
#         'headers': {
#             'Content-Type': 'application/json',
#             'Access-Control-Allow-Origin': '*'
#         },
#         'body':body    #bodyの内容が7行目にある r にオブジェクトとして返される。r.json()などでデータを取り出す。
#     }
