import os
import logging
from typing import List, Dict
import asyncio
import yaml
from openai import AsyncOpenAI
import pandas as pd

# ロギングの設定
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 設定ファイルの読み込み
with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# OpenAIクラスのインスタンスを生成
client = AsyncOpenAI(api_key=os.getenv('OPENAI_API_KEY'))

async def classify_text(text: str, categories: List[str], prompt_template: str) -> str:
    """テキストを分類する非同期関数"""
    prompt_text = prompt_template.format(categories=categories, text=text)
    try:
        response = await client.chat.completions.create(
            model=config['openai_model'],
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt_text}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"Error classifying text: {e}")
        return "Classification failed"

async def process_texts(texts: List[str], categories: List[str], prompt_template: str) -> List[str]:
    """テキストのリストを処理する非同期関数"""
    tasks = [classify_text(text, categories, prompt_template) for text in texts]
    return await asyncio.gather(*tasks)

async def main():
    # CSVファイルの読み込み
    try:
        result_question_df = pd.read_csv(config['result_question_file_path'])
        classification_df = pd.read_csv(config['classification_file_path'])
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return
    except pd.errors.EmptyDataError:
        logging.error("One of the CSV files is empty")
        return

    categories = classification_df['classification'].tolist()

    # プロンプトファイルの読み込み
    try:
        with open(config['prompt_file_path'], 'r', encoding='utf-8') as file:
            prompt_template = file.read().strip()
    except FileNotFoundError:
        logging.error(f"Prompt file not found: {config['prompt_file_path']}")
        return

    texts = result_question_df['Text'].tolist()
    total_count = len(texts)
    logging.info(f"Total text count: {total_count}")

    # テキストの分類
    classification_results = await process_texts(texts, categories, prompt_template)

    # 分類結果をDataFrameに追加
    result_question_df['Classification'] = classification_results

    # 結果をCSVに保存
    try:
        result_question_df.to_csv(config['output_csv_file_path'], index=False)
        logging.info(f"Results saved to {config['output_csv_file_path']}")
    except Exception as e:
        logging.error(f"Error saving results: {e}")

if __name__ == "__main__":
    asyncio.run(main())