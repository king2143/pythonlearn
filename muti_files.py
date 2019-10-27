# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 18:20:40 2019

@author: SAIC_G7066
"""
import pandas as pd
from pandas import DataFrame as df
import csv
import os

filedirectory = 'F:\data'

def machengnan(rootDir):
    filelist= list ()
    for root,dirs,files in os.walk(rootDir):
        for file in files:
            file_name = os.path.join(root,file)
            filelist += [file_name]
    return(filelist)

filenames = machengnan(filedirectory)

xlsx_file = []
for file in filenames:
    if 'xlsx' in file:
        xlsx_file.append(file)


for a in xlsx_file:
    data = pd.read_excel(a, sheet_name = 'C',header = None)
    for i in range(data.shape[1]):
        if ('drag torque' in data[i].values) == True:
            torquedata = list(data[i])[10:22] 
            with open(r'F:\data\result.csv',"a+", newline='') as csvfile: 
                writer = csv.writer(csvfile)
                writer.writerow(torquedata)
   
    
    


