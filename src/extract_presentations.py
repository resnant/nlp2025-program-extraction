#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
このスクリプトは、NLP-2025/index.htmlから「一般発表」
の情報（セッション情報、発表ID、タイトル、PDF URL、著者情報、サマリー）を抽出して、
CSVファイル（presentations.csv）に書き出します。
"""

import csv
import os
from bs4 import BeautifulSoup

def extract_general_presentations(html_file):
    # HTMLファイルを読み込み、BeautifulSoupでパースする
    with open(html_file, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    
    # 「一般発表」セクション（h3要素 id="general"）を取得
    general_section = soup.find("h3", id="general")
    if not general_section:
        print("一般発表セクションが見つかりません。")
        return []
    
    # 「一般発表」セクションより後にある発表セッションのdiv（クラス名が"session1"や"session2"など）を全て取得
    session_divs = general_section.find_all_next("div", class_=lambda x: x and x.startswith("session"))
    
    presentations = []
    current_session = ""  # セッション情報（セッションヘッダーから取得）
    
    for session_div in session_divs:
        # セッションヘッダーがあればセッション情報を更新
        header = session_div.find("div", class_="session_header")
        if header:
            # ヘッダー内のテキストからセッション番号とタイトルの部分を抽出する
            # 例: "A1:〜" のような形式が含まれている前提
            current_session = header.get_text(strip=True).split("　")[0]
        
        # 各発表情報は内部の<table>に格納されていると想定
        table = session_div.find("table")
        if table:
            rows = table.find_all("tr")
            # 発表情報は2行ずつになっている前提（1行目:発表IDとタイトル、2行目:PDFリンクと著者情報）
            for i in range(0, len(rows), 2):
                if i + 1 >= len(rows):
                    break
                row1 = rows[i]
                row2 = rows[i+1]
                
                # 1行目から発表IDとタイトルを取得
                pid_td = row1.find("td", class_="pid")
                presentation_id = pid_td.get_text(strip=True) if pid_td else ""
                title_span = row1.find("span", class_="title")
                title = title_span.get_text(strip=True) if title_span else ""
                
                # 2行目からPDFリンク(URL)と著者情報を取得
                link_tag = row2.find("a")
                pdf_url = link_tag["href"] if link_tag and link_tag.has_attr("href") else ""
                tds = row2.find_all("td")
                authors = tds[1].get_text(strip=True) if len(tds) >= 2 else ""
                
                # 発表サマリーの取得
                summary_file = os.path.join("NLP-2025", "pursed_text_summary", presentation_id + ".txt")
                try:
                    with open(summary_file, encoding="utf-8") as sf:
                        summary = sf.read().strip()
                except FileNotFoundError:
                    summary = ""
                
                presentations.append({
                    "session": current_session,
                    "id": presentation_id,
                    "title": title,
                    "url": pdf_url,
                    "authors": authors,
                    "summary": summary
                })
    return presentations

def write_csv(presentations, csv_file):
    fieldnames = ["session", "id", "title", "url", "authors", "summary"]
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(presentations)

if __name__ == "__main__":
    html_file = "NLP-2025/index.html"  # 対象のHTMLファイル名
    csv_file = "presentations.csv"        # 出力先CSVファイル名
    
    presentations = extract_general_presentations(html_file)
    write_csv(presentations, csv_file)
    print(f"{len(presentations)} 件の一般発表情報を'{csv_file}'に書き出しました。")
