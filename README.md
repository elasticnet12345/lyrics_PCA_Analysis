# Nana vs Yukari
水樹奈々と田村ゆかりの曲を判別するプロジェクト


### 歌詞をスクレイピングする
```shell
$ python crawler.py http://j-lyric.net/artist/a0018f8/l00c342.html ./data/Nana.csv
```
./data/Nana.csvができる. 
曲名, URL, 歌詞のCSVファイル

### 歌詞を形態素解析する
mecab_analysis内の歌手名を指定して, 
```shell
$ python mecab_analysis.py 
```
./data/Nana_keitaiso.csvが出力される.
曲名,  URL, 形態素解析の結果のリスト のCSVができる.


### 単語をカウントする
横軸に単語のリストで縦軸に曲名について横軸の単語の出現頻度を表すようなデータを作成する.
```shell
$ python word_count.py
```

### 単語をBoW表現にする
単語をカウントしたCSVの./data/word_count.csvからBoW表現にした./data/word_count_BoW.csvをつくる.
```shell
$ python convert convert_BoW.py
```

### 解析をする
PCAで二次元空間で表示する.
```shell
$ python PCA.py
```

