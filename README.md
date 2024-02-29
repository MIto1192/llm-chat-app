# 本リポジトリについて
下記記事にて紹介されているChatGPTを用いたチャットアプリのバックエンドコードに機能追加を実施したコードになります。<br>
https://zenn.dev/ktechb/articles/chatgpt-clone-stream

# 機能追加内容
- ChatGPTに送信するプロンプトにフロントエンドから受け取った添付ファイル情報を参考情報として含む機能

# 実行方法
- 実行準備
    - Pythonインストール
       - 稼働確認済ver:Python 3.10
    - OpenAIのAPIKEY発行
- 実行手順
    - srcディレクトリに移動
    - src配下に仮想環境(venv)作成
    - venvをアクティベートにして、仮想環境にrequirements.txtを指定してpip install
    - 「uvicorn llm_server.main:app --reload」でアプリを起動する
    - 「export OPENAI_API_KEY="<発行したOpenAIのAPIKELangChainY>"」を実行

# 参考サイト
- LangChainのmemoryを使用時、プロンプトテンプレートに複数変数を指定するとエラーになる事象の解消法
  - https://stackoverflow.com/questions/76941870/valueerror-one-input-key-expected-got-text-one-text-two-in-langchain-wit
