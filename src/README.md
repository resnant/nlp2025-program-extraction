# ファイルの説明
- **purse_all_pdf.py**  
  予稿のPDFファイルをパースしてテキストに変換するやつ

- **extract_abstract_batch.py**  
  purse_all_pdf.pyで抽出・整形されたデータを元に、要旨を抽出するやつ

- **extract_presentations.py**  
  プログラム一覧のhtmlをパースして発表タイトルや著者情報を拾いつつ、↑で抽出した要旨も合体したcsvを書き出すスクリプト

# 使い方
- [予稿集のzipファイル](https://www.anlp.jp/resource/annual_meeting/NLP-2025.zip)をダウンロードして `src/`以下に解凍
- 上記スクリプトを順番に実行
    - 実行にはpymupdfとbeautifulsoupのインストールが必要です