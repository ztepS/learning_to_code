#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import matplotlib.ticker
import matplotlib.pyplot as plt
import numpy as np
import pyodbc
 
db = pyodbc.connect('DSN=test')
cursor=db.cursor()
cursor.execute(u"SELECT Zerki.нПодложки, Zerki.Тзер, Zerki.L0 FROM Zerki WHERE (((Zerki.Тзер)='Пьезо') AND ((Zerki.Вкомп)='Свободно') AND ((Zerki.ГОтказ)='Годен'));")
data=cursor.fetchall()

y=range(len(data))
minVal=99
maxVal=0
for i in range(len(data)):
    y[i] = round(data[i][2],3)
    if(y[i]<minVal):minVal = y[i]
    if(y[i]>maxVal):maxVal = y[i]

count=(maxVal-minVal)*1000
print maxVal, minVal
#y = np.random.randn(1000)

histogram=range(int(count))
currentNumber=minVal
for i in range(int(count)):
    histogram[i]=range(2)
    histogram[i][0]=round(currentNumber,3)
    histogram[i][1]=0
    currentNumber+=0.001
    for j in range(len(y)):
        if(histogram[i][0]==y[j]):histogram[i][1]+=1 ##rewrite

print histogram

#plt.hist(y, bins=count, range=None, normed=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, hold=None)
##plt.minorticks_on()
#locator = matplotlib.ticker.LinearLocator (13)
#
#plt.xticks(np.arange(minVal,maxVal,0.001))
#
#plt.show()