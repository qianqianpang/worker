import os


def rename():
    i = 0
    path = r"C:\Users\huangcheng\PycharmProjects\pythonProject\result0"
    filelist = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹）
    i = 276
    for files in filelist:  # 遍历所有文件
        i = i + 1
        Olddir = os.path.join(path, files)  # 原来的文件路径
        filetype = '.pdf'  # 文件扩展名
        Newdir = os.path.join(path, str(i) + filetype)  # 新的文件路径
        os.rename(Olddir, Newdir)  # 重命名
    return True


if __name__ == '__main__':
    rename()
