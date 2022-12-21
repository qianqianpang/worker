import os
import pandas as pd

if __name__ == '__main__':
    current_path = os.path.abspath(__file__)
    father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
    source_data_path = os.path.join(father_path, "news_data")

    file_list = []
    title_list = []
    files = os.listdir(source_data_path)

    for file in files:
        file_path = os.path.join(source_data_path, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            file_list.append(file)
            title_list.append(content.split("　　")[0])

    dataframe = pd.DataFrame({'file': file_list, 'title': title_list})
    dataframe.to_csv(os.path.join(father_path, "result/file_title.csv"), index=False, sep=',')

    print('预处理 完毕')
