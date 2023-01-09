# 逐行读取csv文件
import csv

res = ""
filename = r'result/word.csv'
with open(filename, 'r', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        res += row["word"]
        res += " "
with open('result/word.txt','w') as f:
    f.write(res)