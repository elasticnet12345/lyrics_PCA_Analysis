import requests
from bs4 import BeautifulSoup
from argparse import ArgumentParser
import os
import csv
from crawl_lyric import get_lyrics

#
#   実行例
#   $ python crawler.py http://　j-lyric.net/artist/a0018f8/ .
#
#
#
#
#


if __name__ == "__main__":
    
    # 引数設定
    usage = "$ python url"# usage = "$ python url path"
    argparser = ArgumentParser(usage = usage)
    argparser.add_argument("url", type=str, default=None, help="copy adn pase url")
    argparser.add_argument("file_name", type=str, help="distination directory path, default current directory")
    args = argparser.parse_args()

    # URLの指定
    URL = args.url
    
    # 出力先の指定
    name_csv_file =  args.file_name

    # JLyricsのサイトかチェック
    flag_JLyrics, flag_KashiMap, flag_KashiTime = False, False, False
    if "j-lyric.net" in URL:
        flag_JLyrics = True
    else:
        pass

    # リクエスト
    resp = requests.get(URL)

    # オブジェクトに分解
    html = resp.content
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        soup = BeautifulSoup(html, "html5lib")

    # pタグの取得
    list_lyrics = []
    contents_p_tag = soup.find_all("p")
    for i, content in enumerate(contents_p_tag):
        if content.get("class") == ["ttl"]:
            print(content.a.get("href"), end=",")
            print(content.text)
            _url_ = "http://j-lyric.net"+content.a.get("href")
            list_lyrics.append([content.text, _url_, get_lyrics(_url_).replace(",","")])

    # 歌詞の取得

    # 出力
    path_csv_file = os.path.join("./data", name_csv_file)
    if os.path.exists(path_csv_file):
        print("This file already exists.")
        # exit()

    with open(path_csv_file, "w") as f:
        writer = csv.writer(f, lineterminator="\n")

        for lyric in list_lyrics:
            writer.writerow(lyric)



