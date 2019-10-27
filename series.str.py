# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 08:34:48 2019
@author: SAIC_G7066
"""
import pandas as pd
from pandas import Series
from pandas import DataFrame as df
import numpy as np
from tqdm import tqdm

data = pd.read_csv(r'F:\上汽工作内容\python_learn\pythonlearn6\pi_ps.csv',header = None,engine='python')
#data.to_excel(r'F:\上汽工作内容\python_learn\pythonlearn6\pi.xls',index = 0, header = 0,sheet_name = 'pi')
data = data.dropna(axis=0,how='any') #drop all rows that have any NaN values




data = data[(data[0] != 0)]
data = data.reset_index(drop=True)


import re
for i in range(len(data)):
    data[0][i] = re.sub('-','',data[0][i])    

import re
for i in range(len(data)):
    data[0][i] = re.search('(.+?)_',data[0][i]).group(1)    




data[0] = data[0].str.replace("-", "")
data[0] = data[0].str.split('_',expand = True)





data.isnull().any()#axis = 0/1(any中)

#data.fillna(0, inplace=True)

#data[1].fillna(0, inplace=True)
#data[1].fillna(data[1].median(),inplace=True)
##Series.mean().median().mode
#data.describe()[1]['25%']

#data1 = data.groupby(0).mean()
#data1 = data.groupby(0).count()
#data1 = data[0].mode()

#data = data.drop([0],axis = 1)
#data = data.drop([1],axis = 0)

data = data.dropna(axis=0,how='all')
data = data.dropna(axis=0,how='any') #drop all rows that have any NaN values
data = data.dropna(axis=1,how='all')
data = data.dropna(axis=1,how='any') #drop all rows that have any NaN values


data[0] = data[0].str.replace("-", "")
data[0] = data[0].str.split('_',expand = True)
#data[[0,5]] = data[0].str.split('_',expand = True)
data[0] = data[0].replace(['20190814','20190815','20190817','20190819','20190826',\
                           '20190827','20190829','20190830'],[1,2,3,4,5,6,7,8])

data = data[(data[0] == 1) | (data[0] == 2)]
#m = df()
#for i in range(len(data)):
#    if data[0][i] == 1:
#        print(i)
#        m = m.append(data.iloc[i])

data[0] = pd.to_numeric(data[0])
data[[0,1]] = data[[0,1]].apply(pd.to_numeric)
data.astype(float)


#拼接 Series.str.cat
a = Series(['a', 'b', 'c'])
a.str.cat(['A', 'B', 'C'], sep='_')
a.str.cat([['x', 'y','z'], ['1', '2', '3']], sep='_')
a.str.cat(sep=',')

# 分割 Series.str.split  expand = True(会出一列)
s = pd.Series(['a_b_c', 'c_d_e', 'f_g_h'])
b = s.str.split('_',expand = True)

# 获取指定位置字符串  Series.str.get
s.str.get(0)
list(s.str.get(1))

# 使用给定的字符拼接 Series.str.join
s.str.join('!')
s.str.join('?')

# 是否包含某字符  Series.str.contains
s.str.contains('d')

# 替换 Series.str.replace
s.str.replace('_', '.')

# 重复 Series.str.repeat
s.str.repeat(3)

# 切割字符 Series.str.slice
s.str.slice(1, 3)

# 切割替换 Series.str.slice_replace
s.str.slice_replace(1, 3, '?')

# 计数 Series.str.count
s.str.count('a')

#判断是否以给定的字符串开头 Series.str.startswith(endwith)
s.str.startswith('a')

# 首字符大写 Series.str.capitalize()
s.str.capitalize()

# 查找正则表达式  Series.str.findall 
s.str.findall('[bdg]_(.+?)')
s.str.findall('[bdg](.?)[ceh]')


