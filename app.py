import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

# .envファイルの内容を読み込む
load_dotenv()

# 環境変数からURLとクラス名を取得
url = os.getenv("URL")
class_name = os.getenv("CLASS_NAME")

# User-Agentを設定
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

print("開始")

# HTTPリクエストを送信
response = requests.get(url, headers=headers)

# ステータスコードを確認
print(f"ステータスコード: {response.status_code}")

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    
    # 見出しとリンクを抽出
    headlines = soup.find_all("a", class_=class_name)
    
    for headline in headlines:
        print("見出し:", headline.text.strip())
        print("リンク:", headline.get("href"))
else:
    print(f"HTTPリクエストが失敗しました。ステータスコード: {response.status_code}")

print("終了")