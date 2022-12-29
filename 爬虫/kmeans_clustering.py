import warnings
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from TF_IDF import main
warnings.filterwarnings("ignore") # 忽略警告

if __name__ == "__main__":
    w = main()
    x = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    y = []
    for k in x:
        print(k)
        clf = KMeans(n_clusters=k)
        s = clf.fit(w)
        # 用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
        # y.append(clf.inertia_)
        y.append(silhouette_score(w, clf.labels_))
    print(x)
    print(y)
    # plt.plot(x, y, 's-', color='r', label="inertia_")  # s-:方形
    plt.plot(x, y, 's-', color='r', label="silhouette_score")  # s-:方形
    plt.xlabel("k-value")  # 横坐标名字
    # plt.ylabel("inertia_")  # 纵坐标名字
    plt.ylabel("silhouette_score")  # 纵坐标名字
    plt.legend(loc="best")  # 图例
    plt.show()
