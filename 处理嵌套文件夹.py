import os
import shutil

# 指定压缩包路径
zip_file = r"C:/Users/huangcheng/PycharmProjects/pythonProject/yuan/夏20210930"

# 指定输出路径
output_dir = "C:/Users/huangcheng/PycharmProjects/pythonProject/target"

# 遍历压缩包中所有文件和文件夹
for root, dirs, files in os.walk(zip_file):
    for file in files:
        # 判断文件是否是PDF格式
        if file.endswith(".pdf"):
            # 获取文件绝对路径
            file_path = os.path.join(root, file)
            print(file_path)
            shutil.copy(file_path, output_dir)
