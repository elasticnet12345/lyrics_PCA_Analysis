import csv
import numpy as np

# 全単語の辞書を作成する
word_dict = dict()

# 水樹奈々についての辞書登録
csv_data1 = "./data/Nana_keitaiso.csv"
with open(csv_data1, "r") as f:
    reader = csv.reader(f)
    # すべての歌詞について
    for row in reader:
        lyric = row[2:]
        # ひとつの歌詞について
        for word in lyric:
            # 単語が登録済であったら
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

# 田村ゆかりについての辞書登録
csv_data2 = "./data/Yukari_keitaiso.csv"
with open(csv_data2, "r") as f:
    reader = csv.reader(f)
    # すべての歌詞について
    for row in reader:
        lyric = row[2:]
        # ひとつの歌詞について
        for word in lyric:
            # 単語が登録済であったら
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    
# CSVに登録
csv_path = "./data/word_count.csv"
with open(csv_path, "w") as f:
    writer = csv.writer(f, lineterminator="\n")
    # header を記述
    word_list = list(word_dict.keys())
    header = ["", ""] + word_list
    writer.writerow(header)
    # それぞれの曲を登録
    with open(csv_data1, "r") as g:
        reader = csv.reader(g)
        for row in reader:
            music, url, lyric = row[0], row[1], row[2:]
            tmp = np.zeros(len(word_list))
            for word in lyric:
                tmp[word_list.index(word)] += 1
            
            data = [music, url] + list(tmp) # tmp はnp.ndarrayなのでlist化
            writer.writerow(data)
    
    with open(csv_data2, "r") as g:
        reader = csv.reader(g)
        for row in reader:
            music, url, lyric = row[0], row[1], row[2:]
            tmp = np.zeros(len(word_list))
            for word in lyric:
                tmp[word_list.index(word)] += 1
            
            data = [music, url] + list(tmp) # tmp はnp.ndarrayなのでlist化
            writer.writerow(data)
    





