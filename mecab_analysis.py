import csv
import MeCab

tagger = MeCab.Tagger("-Owakati")


person = "Nana"

path = "data/{}.csv".format(person)
with open(path, "r") as f:
    reader = csv.reader(f)

    # 一つづつ読み込む
    for row in reader:
        lyric = row[2] # 歌詞
        list_result = tagger.parse(lyric).replace("\n", "").replace("\u3000", "").split(" ")
        while "" in list_result:
            list_result.remove("")
        print(list_result)
        
        # 形態素解析結果を書き込む
        path_csv = "data/{}_keitaiso.csv".format(person)
        with open(path_csv, "a") as g:
            writer = csv.writer(g, lineterminator="\n")
            writer.writerow([row[0], row[1]] + list_result)


            

