#!/usr/bin/env python3
# このスクリプトはハードコードされたディレクトリ "NLP-2025/pursed_text" 内の全テキストファイルを再帰的に処理し、
# 各ファイルから「概要」部分を抽出して、同名のテキストファイルとして "NLP-2025/pursed_text_summary" に保存します。
import os
import re

def extract_abstract(text):
    """
    与えられたテキストから「概要」行以降、次のセクション（改行に続く数字の出現行）までのテキストを抽出する。
    抽出できない場合は例外を発生させる。
    """
    pattern = r'(?:概要|要旨|Abstract)\s*\n(.*?)\n\d'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        raise ValueError("概要部分が見つかりませんでした。")

def process_file(file_path):
    """
    ファイルを読み込み、概要を抽出する。
    エラーが発生した場合は例外をスローする。
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return extract_abstract(text)

def main():
    input_dir = "NLP-2025/pursed_text"
    output_dir = "NLP-2025/pursed_text_summary"
    os.makedirs(output_dir, exist_ok=True)
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".txt"):
                input_file_path = os.path.join(root, file)
                # 出力先はベースネームのみを用いて output_dir に保存
                output_file_path = os.path.join(output_dir, file)
                try:
                    abstract = process_file(input_file_path)
                    # 抽出された概要内の改行を削除
                    abstract = abstract.replace("\n", "")
                    with open(output_file_path, "w", encoding="utf-8") as f_out:
                        f_out.write(abstract)
                    print(f"保存成功: {output_file_path}")
                except Exception as e:
                    print(f"エラー発生ファイル: {input_file_path} - Error: {e}")

if __name__ == '__main__':
    main()
