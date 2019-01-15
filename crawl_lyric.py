import requests
from bs4 import BeautifulSoup
from argparse import ArgumentParser
import os

#
#   実行例
#   $ python crawler.py http://j-lyric.net/artist/a0018f8/l00c342.html .
#
#
#
def get_lyrics(url):

    # リクエスト
    resp = requests.get(url)

    # オブジェクトに分解
    html = resp.content
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        soup = BeautifulSoup(html, "html5lib")

    # pタグの取得
    contents_p_tag = soup.find_all("p")
    for i, content in enumerate(contents_p_tag):
        if content.get("id") == "Lyric":
            lyric = content.text
            break

    return lyric