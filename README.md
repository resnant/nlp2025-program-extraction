# NLP2025予稿の分析

[NLP2025](https://www.anlp.jp/nlp2025/)の発表プログラム（タイトル、著者、要旨、セッション情報）を列挙したcsvファイルと、それを作るためのツール群です。
csvファイルをLLMに投げ込んで、自分が聞きたい発表を絞り込んだり、トレンドを分析したりする使い方を想定しています。

# ディレクトリ構成

- **presentations.csv**  
  発表一覧のcsvファイルです。これをダウンロードして使ってください

- **src/以下**
  予稿PDFやhtmlをパースしてcsv化するためのスクリプト群（興味ある人向け）

## ライセンス

NLP2025の予稿集は CC BY 4.0 ライセンスにより公開されています。
本リポジトリの内容も同様にCC BY 4.0とします。