import pandas as pd
from nltk import word_tokenize,pos_tag   #分词、词性标注
from nltk.corpus import wordnet
from nltk.corpus import stopwords    #停用词
from nltk.stem import WordNetLemmatizer    #词性还原
from tqdm import tqdm

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

news = pd.read_excel('2016newstext.xlsx').values
newscut = []
for text in tqdm(news):
    text = ''.join(text)
    text = text.replace("\n", "")
    text = text.replace("."," ")
    text = text.lower()
    cutwords1 = word_tokenize(text)  #分词
    interpunctuations = [',', ' ','.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$','--', '%', '’', '“', '.-', '/', '—', '”','`','','-']
    cutwords2 = [word for word in cutwords1 if word not in interpunctuations]  #去除标点符号
    stops = set(stopwords.words("english"))
    cutwords3 = [word for word in cutwords2 if word not in stops]  #删除停用词
    cutwords3 = [word for word in cutwords3 if len(word) < 20]  # 删除停用词
    tagged_sent = pos_tag(cutwords3)  # 获取单词词性
    cutwords4 = []
    for tag in tagged_sent:
        wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
        cutwords4.append(WordNetLemmatizer().lemmatize(word = tag[0], pos=wordnet_pos))  # 词形还原
    newscut.append(cutwords4)
    # cutwords4=[]
    # for cutword in cutwords3:
    #     if len(cutword) > 20 :
    #         cutword = ''
    #     else:
    #         cutwords4.append(WordNetLemmatizer().lemmatize(cutword))  #将词根转化为名词形式
    newscut.append(cutwords4)
with open('data2016.txt', 'w',encoding='utf-8') as f:
    for ele in newscut:
        ele = ' '.join(ele) + '\n'
        f.write(ele)