# ChatGPT-QuestionAnalysis

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)

ChatGPT-QuestionAnalysisは、ChatGPTに対して行った質問データを自動分類し、分析するためのツールです。このプロジェクトは、処理されたテキストデータを関連するカテゴリーに分類することにより、自組織におけるChatGPTの使用状況を定量的に理解することを目的としています。

## 目次

- [ChatGPT-QuestionAnalysis](#chatgpt-questionanalysis)
  - [目次](#目次)
  - [概要](#概要)
  - [機能](#機能)
  - [前提条件](#前提条件)
  - [インストール方法](#インストール方法)
  - [使用方法](#使用方法)
  - [CSVファイルの形式](#csvファイルの形式)
  - [出力](#出力)
  - [詳細な使い方](#詳細な使い方)
  - [依存関係](#依存関係)
  - [貢献ガイドライン](#貢献ガイドライン)
  - [トラブルシューティング](#トラブルシューティング)
  - [ライセンス](#ライセンス)

## 概要
`ChatGPT-QuestionAnalysis` は、特定のテキスト（例えば、公共機関からの質問など）を分類するためのPythonスクリプトです。OpenAIのGPT-3.5モデルを使用してテキストを特定のカテゴリーに分類し、結果をCSVファイルに出力します。

## 機能
- CSV形式の入力ファイルからテキストデータを読み込む。
- GPT-3.5モデルを用いてテキストを分類。
- 分類結果をCSVファイルに保存。
- 非同期処理による高速な分類。

## 前提条件
- Python 3.7以上
- OpenAI API キー

## インストール方法
1. このリポジトリをクローンします：
   ```
   git clone https://github.com/yourusername/ChatGPT-QuestionAnalysis.git
   cd ChatGPT-QuestionAnalysis
   ```

2. 必要な依存関係をインストールします：
   ```
   pip install -r requirements.txt
   ```

## 使用方法
1. 環境変数 `OPENAI_API_KEY` にOpenAIのAPIキーを設定します。
2. 必要なCSVファイル（質問データ、分類カテゴリ）を `data/` ディレクトリに配置します。
3. プロンプトテンプレートを `config/prompt.txt` に配置します。
4. スクリプトを実行して結果を取得します：
   ```
   python ChatGPT-QuestionAnalysis.py
   ```

## CSVファイルの形式
- `result_question.csv`: 質問データが含まれるCSVファイル。
- `classification.csv`: 分類カテゴリが含まれるCSVファイル。

## 出力
- 分類結果が `output/output.csv` に保存されます。

## 詳細な使い方
[USAGE.md](USAGE.md) を参照してください。

## 依存関係
- pandas
- pyarrow
- openai
- pyyaml

詳細は `requirements.txt` を参照してください。

## 貢献ガイドライン
プロジェクトへの貢献を歓迎します。詳細は [CONTRIBUTING.md](CONTRIBUTING.md) を参照してください。

## トラブルシューティング
一般的な問題とその解決方法については、[TROUBLESHOOTING.md](TROUBLESHOOTING.md) を参照してください。

## ライセンス
このプロジェクトは [MITライセンス](LICENSE) の下で公開されています。