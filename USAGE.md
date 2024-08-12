# 詳細な使用方法

## 環境設定
1. OpenAIのAPIキーを環境変数として設定します：
   - Windows:
     ```
     set OPENAI_API_KEY=あなたのAPIキー
     ```
   - Linux/macOS:
     ```
     export OPENAI_API_KEY=あなたのAPIキー
     ```

2. `config/config.yaml` ファイルを編集して、必要に応じてファイルパスやOpenAIモデルを設定します。

## 入力データの準備
1. `data/result_question.csv` に分類したいテキストデータを配置します。
2. `data/classification.csv` に分類カテゴリーを配置します。
3. `config/prompt.txt` にGPT-3.5モデルへのプロンプトテンプレートを配置します。

## スクリプトの実行
1. コマンドラインで以下を実行します：
   ```
   python ChatGPT-QuestionAnalysis.py
   ```
2. スクリプトは進捗状況をログに出力します。
3. 処理が完了すると、結果が `output/output.csv` に保存されます。

## 結果の解釈
出力されたCSVファイルには、元のテキストデータと共に、各テキストに対する分類結果が含まれています。

## パフォーマンスに関する注意
- 大量のデータを処理する場合、十分なメモリと処理能力を持つマシンを使用することをお勧めします。
- 非同期処理を利用しているため、ネットワーク接続が安定していることを確認してください。

## エラー処理
スクリプトはエラーが発生した場合、ログにエラーメッセージを出力します。エラーログを確認し、必要に応じて対応してください。