import os
import warnings

from sklearn.cluster import KMeans

from TF_IDF import main

warnings.filterwarnings("ignore")

if __name__ == "__main__":
    w = main()
    clf = KMeans(n_clusters=11)
    s = clf.fit(w)

    current_path = os.path.abspath(__file__)
    father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
    source_data_path = os.path.join(father_path, "news_data")
    files = os.listdir(source_data_path)
    i = 0
    while i < len(clf.labels_):
        print("新闻:" + files[i] + "  → 第"+ str(clf.labels_[i]) + "类别")
        i = i + 1
