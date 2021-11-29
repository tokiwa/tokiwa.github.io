# tokiwa.github.io
これらのプログラムはGitHubが提供する次のGitHub Pagesによってプロラムを実行することができます。

https://docs.github.com/ja/pages/getting-started-with-github-pages/about-github-pages

## Front end sample
JQueryデモ
https://tokiwa.github.io/HTML5_JS.html

fetchでAWS lambdaにアクセス
https://tokiwa.github.io/fetch.html

Vue.js & axios でAWS lambdaにアクセス
https://tokiwa.github.io/lambda_vue.html

Vue.jsにより実装した郵便番号から住所を取得するデモ
https://tokiwa.github.io/vue_zip.html

ブロック崩しゲーム
https://tokiwa.github.io/breakout/index.html

## Back end sample
AWS ディレクトりに Front endに対応するlambdaやCORS対応のlamdaといったPythonプログラムがあります。

lambda_CORS.py: CORS対応サンプル

lambda_s3put.py: s3への書き込み

API_Gateway.py: fetch.htmlと連携

postLambda_putS3.py: fetch_post.htmlと連携

parrot.py: postされたJSONをそのままreturn

s3FileListRead.py: s3にあるファイルを一覧し、その内容を表示

parrot-get.py: getされたクエリパラメータをJSONでreturn