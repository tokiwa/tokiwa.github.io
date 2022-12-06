import requests
import json
from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def helloWorld():
    return "<h1>Hello, World!</h1>"

@app.route("/aws")
def awsLambda():
    payload = {'date': '2022-12-25', 'yen': '130.5'}
    url = 'https://unedgij7n6.execute-api.ap-northeast-1.amazonaws.com/default/hello_world_python'
    r = requests.post(url,data=json.dumps(payload))
    return '<h1>' + str(r.json()["date"]) + " : " + str(r.json()["yen"]) + ' yen/$</h1>'

if __name__ == "__main__":
    app.run(debug=True)

# 実行方法
# 1. urlで示されるAPI GatewayのURLを変更後、このプログラムをPCのターミナルから pythonで実行する
# 2. 実行したターミナルに、*Running on http://127.0.0.1:5000とBaseURLが表示される
# 3. 同じPCにあるブラウザから http://127.0.0.1:5000/aws　にアクセスする
# 4. ブラウザに"2022-12-25 : 130.5 yen/$"と表示される