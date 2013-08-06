#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import pyodbc

class mirror:
    def __init__(self, name, delta, L0, box, place, radius):
        self.name = name
        self.delta = delta
        self.L0 = L0
        self.box = str(box)
        self.place = str(place)
        
#        if (model == u"Плоское"):self.model=0
#        if (model == u"Пьезо"):self.model=1
#        if (model == u"Сфера"):
#            self.model=3
        #print radius
        #self.radius=round(radius,1)
        self.radius = radius
    def report(self):
        print self.name, self.delta, self.L0, self.box, self.place, self.radius
        
    
        

class group():
    def __init__(self):
        self.list=[]
    
    def add(self,mirror):
        self.list.append(mirror)
        
    def report(self):
        for i in self.list:
            i.report()
        
db = pyodbc.connect('DSN=test')
cursor=db.cursor()
cursor.execute(u"SELECT Zerki.нПодложки, Zerki.Тзер, Zerki.Сигма, Zerki.L0, Zerki.МесХран, Zerki.Ячейка, Zerki.Рсферы FROM Zerki WHERE (Zerki.ГОтказ='Годен' AND zerki.[Материал подл] Is Null AND zerki.Вкомп='Свободно' AND zerki.НранВоз Is Null);")
data=cursor.fetchall()


#mirrorsList=[]
#for i in range(len(data)):
#    mirrorsList.append(mirror(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]))

flatList=[]
piezoList=[]
sphereList=[]
for i in range(len(data)):
    if(data[i][1] == u"Плоское"): flatList.append(mirror(data[i][0], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]))
    if(data[i][1] == u"Пьезо"): piezoList.append(mirror(data[i][0], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]))
    if(data[i][1] == u"Сфера"): sphereList.append(mirror(data[i][0], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]))


first=group()
first.add(flatList[3])
first.add(piezoList[3])

first.report()


