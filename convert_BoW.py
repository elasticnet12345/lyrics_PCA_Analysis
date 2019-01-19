import csv

csv_path = "./data/word_count.csv"
with open(csv_path, "r") as f:
    csv_write_path = "./data/word_count_BoW.csv"        
    with open(csv_write_path, "w") as g:
        writer = csv.writer(g, lineterminator="\n")
        reader = csv.reader(f)
        # header 
        header = next(reader)
        writer.writerow(header)
        # data
        for row in reader:
            music, url, vec = row[0], row[1], row[2:]
            tmp = [float(_) for _ in vec]
            sum_vec = sum(tmp)
            vec = [float(_)/ sum_vec for _ in tmp]
            writer.writerow([music, url] + vec)
        


        