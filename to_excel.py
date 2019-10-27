# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:39:52 2019

@author: SAIC_G7066
"""
import time
import xlwt   
import datetime
WorkBook = xlwt.Workbook() 
#name_1 = r'MLPresFollow'
sheet1 = WorkBook.add_sheet('MLPresFollow')
presfollow_check = ['x','y=x^2','y = x^3']

for j in range(len(presfollow_check)):
    sheet1.write(0, j, presfollow_check[j])

for i in range(1,10):
    data = [i,i**2,i**3]
    for j in range(len(data)):
        time.sleep(0.1)
        sheet1.write(i,j,data[j])

WorkBook.save("F:\TM11whlVeh.xls")
