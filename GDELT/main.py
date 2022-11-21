import requests
import pandas as pd
from datetime import datetime
import zipfile
import os

path = os.path.split(os.path.abspath(__file__))[0] + os.sep  # 获取当前文件所在目录
data_folder = path + 'data2014' + os.sep

def get_url_data(url):
    global data_folder
    if not os.path.exists(data_folder):
        os.mkdir(data_folder)  # 若文件夹不存在，则主动创建
    filename = url.split('/')[-1]  # 从url链接中获取文件名称
    filepath = data_folder + filename
    if os.path.exists(filepath) or os.path.exists(filepath[:-4]):  # 若文件已下载，则跳过
        print('文件%s已存在' % filename)
        return
    print(filename)
    try:
        data = requests.get(url)
        with open(filepath, "wb") as f:
            f.write(data.content)
        fz = zipfile.ZipFile(filepath, 'r')
        fz.extract(fz.namelist()[0], data_folder) #解压下载下来的zip文件夹
        fz.close()
        if os.path.exists(filepath):
            os.remove(filepath)  # 删除zip文件夹，只保存解压后的数据
    except Exception as e:
        print(e)
        log = open(path + 'log.txt', 'a')
        log.write(url + '\n')

def download():
    url_list = pd.read_csv(r'urls2014.csv', header=None)
    print(url_list)
    for url in url_list[0]:
        print(url)
        get_url_data(url)
        print('下载文件数据', datetime.now())


if __name__ == '__main__':
    download()

