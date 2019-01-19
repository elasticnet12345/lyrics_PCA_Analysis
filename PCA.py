import csv
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def splitting(url):
    a  = url.split("/")
    return a[4]


csv_path = "./data/word_count_BoW.csv"
with open(csv_path, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    musician = ""
    label = -1
    X = []
    y = []
    for row in reader:
        music, url, vec = row[0], row[1], row[2:]
        if splitting(url) != musician:
            musician = splitting(url)
            label += 1
        x = np.array([float(_) for _ in vec])
        X.append(x)
        y.append(label)
    
    X = np.array(X)
    y = np.array(y)

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    class0_indexes = np.where(y == 0)
    class1_indexes = np.where(y == 1)

fig = plt.figure(figsize=(20,10),dpi=100)

with open(csv_path, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    for i, row in enumerate(reader):
        if y[i] == 0:
            color = "blue"
        else:
            color = "red"
        plt.plot(X_pca[i,0], X_pca[i,1], "o", color=color)
        
        # if row[0].isalpha():
        #     plt.annotate(row[0], xy=(X_pca[i,0], X_pca[i,1]))

    # plt.scatter(X_pca[class0_indexes,0], X_pca[class0_indexes,1], color="blue", label="Nana Mizuki")
    # plt.scatter(X_pca[class1_indexes,0], X_pca[class1_indexes,1], color="red", label="Yukari Tamura")
    
    plt.title("Nana Mizuki vs Yukari Tamura")
    plt.legend(loc="best", numpoints=1)
    plt.show()




        



