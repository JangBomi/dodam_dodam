import re
import numpy as np
import pandas as pd
import os

excel_file = './xlsx/book_emotion.xlsx'
df_book_emotion = pd.read_excel(excel_file)
#df_book_emotion
excel_file2 = './xlsx/bookinfo.xlsx'
df_book_info = pd.read_excel(excel_file2)
#df_book_info

emotion_list = []
emotion_type = df_book_emotion.columns
emotion_type #['행복함', '슬픔', '긴장감', '평온', '웅장']

happy_list = df_book_emotion['행복']
sad_list = df_book_emotion['슬픔']
nervous_list = df_book_emotion['긴장감']
relax_list = df_book_emotion['평온']
magnificent_list = df_book_emotion['웅장']

book_info_list = np.array(df_book_info)

def compare_with(text):
    
    emotion_list = ['행복함', '슬픔', '긴장감', '평온', '웅장함']
    
    count = [0,0,0,0,0]
    idx = [0,0,0,0,0]

    one_sample = str(np.array(text))[7:-2]
    one_sample = re.sub('[0-9]*','',one_sample)
    one_sample = re.sub('<.+?>','',one_sample)
    
    strsplit = one_sample.split()
    new_strsplit = []
    for word in strsplit:
        if len(word) <2:
            continue;
        else:
            new_strsplit.append(word)
    new_strsplit = " ".join(new_strsplit)
    
    for happy in happy_list:
        if re.search(str(happy),new_strsplit):
            count[0]+=1
            idx[0]=new_strsplit.index(str(happy))
    
    for sad in sad_list:
        if re.search(str(sad),new_strsplit):
            count[1]+=1
            idx[1] = new_strsplit.index(str(sad))
    
    for nervous in nervous_list:
        if re.search(str(nervous),new_strsplit):
            count[2]+=1
            idx[2] = new_strsplit.index(str(nervous))
    
    for relax in relax_list:
        if re.search(str(relax),new_strsplit):
            count[3]+=1
            idx[3] = new_strsplit.index(str(relax))
    
    for magnificant in magnificent_list:
        if re.search(str(magnificant),new_strsplit):
            count[4]+=1
            idx[4] = new_strsplit.index(str(magnificant))
    
    max_count=0
    max_idx=0
    for i in range(len(count)):
        if count[i]>max_count: 
            max_count=count[i]
            max_idx = i
        elif count[i]==max_count:
            if idx[i]>idx[max_idx]:
                max_count = count[i]
                max_idx = i
    
    
    
    return emotion_list[max_idx]