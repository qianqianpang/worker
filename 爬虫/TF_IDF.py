import os
import re

import jieba
import jieba.analyse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
stop_words_path = os.path.join(father_path, "stop_words.txt")
stopwords = []
for word in open(stop_words_path, 'r', encoding='utf-8'):
    stopwords.append(word.strip("\n"))


# 中文分词
def word_segment(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        docs = f.readlines()
    words_list = []
    for i, text in enumerate(docs):
        words = []
        final_word = []
        p = re.compile(r"\n|：|；|,|、|（|）|\.|。|，|/|(\|)", re.S)
        text = p.sub('', text)
        word = jieba.cut(text)
        words += word
        for i, word in enumerate(words):
            if word not in stopwords:
                final_word.append(word)
        words_list.append(final_word)
    return words_list


def tf_idf():
    source_data_path = os.path.join(father_path, "news_data")
    files = os.listdir(source_data_path)
    corpus = []
    for file in files:
        file_path = os.path.join(source_data_path, file)
        corpus.append(word_segment(file_path))

    # 将文本中的词语转换为词`频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
    vectorizer = CountVectorizer()

    # 该类会统计每个词语的tf-idf权值
    transformer = TfidfTransformer()

    # 第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))

    # 获取词袋模型中的所有词语
    word = vectorizer.get_feature_names_out()

    # 将tf-idf矩阵抽取出来，元素w[i][j]表示j词在i类文本中的tf-idf权重
    weight = tfidf.toarray()

    print(weight)
    return weight


def main():
    tf_idf()
