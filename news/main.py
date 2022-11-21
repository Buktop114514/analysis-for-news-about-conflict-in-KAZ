from gne import GeneralNewsExtractor
import requests
import pandas as pd
from tqdm import tqdm
headers = {
    'Cookie': 'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhksMy7d_KC46wJoZSioG5c5NHD95QNSKqEeh2E1Kq0Ws4DqcjLi--fi-zNi-zNi--4iKnNiKyhi--Xi-z4i-2ci--NiK.XiKLswntt; SCF=Aib6P0veKhMbHrv1KlGKW8KU8AutuZ118RWEgZmpYswMokx929em5j9zjyLDZ-WwQC35-i7XXrYWe5Vgg7MXKzM.; SUB=_2A25MGmZxDeRhGeFL7VAR8SzFzT-IHXVv5Qo5rDV6PUJbktCOLRDtkW1NfcqVFlWZ7LY28q6kqXrgoiaUkstuaprc; SSOLoginState=1629361698; BAIDU_SSP_lcr=https://link.csdn.net/?target=http://m.weibo.cn; _WEIBO_UID=7562012963; WEIBOCN_FROM=1110106030; _T_WM=87785942621; MLOGIN=1; M_WEIBOCN_PARAMS=oid=4647414625212687&luicode=20000061&lfid=4647414625212687&uicode=20000061&fid=4647414625212687; XSRF-TOKEN=c232f6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}
urllist = pd.read_excel('2015.xlsx',sheet_name='Sheet1').values
rows=[]
n=0
for i in tqdm(urllist):
    url = ''.join(i)
    try:
        html = requests.get(url,headers=headers,timeout=1)  # 如果这个请求失败，那么并不会运行break，将运行except中的代码
        html.encoding = 'utf-8'
        extractor = GeneralNewsExtractor()
        result = extractor.extract(html.text, noise_node_list=['//div[@class="comment-list"]'])
        text = result['content']
        row = [url, text]
        rows.append(row)
    except:
        n=n+1
        print(n)

#将数据誊写到Excel文件中
from openpyxl import Workbook

wb = Workbook()
# 选中活动表
ws1 = wb.active

# 设置表头
titleList = ['url', 'news']
for row in range(len(titleList)):
    c = row + 1
    ws1.cell(row=1, column=c, value=titleList[row])

# 数据录入
for listIndex in range(len(rows)):
    ws1.append(rows[listIndex])

wb.save(filename='2015news.xlsx')
