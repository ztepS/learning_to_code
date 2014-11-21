#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import pyodbc
import sys
from PyQt4 import QtGui, QtCore
import itertools
import operator
import shelve

def main():
    
    db = pyodbc.connect('DSN=zerki_local')
    cursor=db.cursor()
    
    #cursor.execute(u"SELECT Zerki.нПодложки, Zerki.Тзер, Zerki.Сигма, Zerki.L0, Zerki.МесХран, Zerki.Ячейка, Zerki.Рсферы FROM Zerki WHERE (((Zerki.МесХран) Is Not Null) AND ((Zerki.Ячейка) Is Not Null) AND ((Zerki.Рсферы)=3.6 Or (Zerki.Рсферы) Is Null) AND ((Zerki.ГОтказ)='Годен') AND ((Zerki.[Материал подл]) Is Null) AND ((Zerki.Вкомп)='Свободно') AND ((Zerki.НранВоз) Is Null) AND ((Zerki.[Годен для Тамбова])<>'тт'));")
    cursor.execute(u"SELECT DISTINCTROW zerki.нПодложки, zerki.Тзер, zerki.Сигма, zerki.L0, zerki.МесХран, zerki.Ячейка, zerki.Рсферы FROM zerki WHERE (((zerki.[Материал подл]) Is Null) AND ((zerki.ГОтказ)='Годен') AND ((zerki.Вкомп)='Свободно') AND ((zerki.НранВоз) Is Null));")
    data=cursor.fetchall()
    
    flatList=[]
    piezoList=[]
    sphereList=[]
    for i in range(len(data)):

        if(data[i][1] == u"Плоское"): flatList.append(Mirror(data[i][0], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]))
        if(data[i][1] == u"Пьезо"): piezoList.append(Mirror(data[i][0], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]))
        if(data[i][1] == u"Сфера" and (abs(data[i][6] - 3.6))<0.1): sphereList.append(Mirror(data[i][0], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]))
        
        
    print min(len(flatList),len(piezoList),len(sphereList))
   
    
    pzDeltaBrList=create_bracket_list(piezoList, "delta")
    pzDFreqList=create_frequency_list(pzDeltaBrList, piezoList)
    pzFreq=unite_list(pzDeltaBrList,pzDFreqList)
    
    
    sDeltaBrList=create_bracket_list(sphereList, "delta")
    sDFreqList=create_frequency_list(sDeltaBrList, sphereList)
    sFreq=unite_list(sDeltaBrList,sDFreqList)
    
    pDeltaBrList=create_bracket_list(flatList, "delta")
    pDFreqList=create_frequency_list(pDeltaBrList, flatList)
    pFreq=unite_list(pDeltaBrList,pDFreqList)
    
    
   
    combinationList=[]
    
   
    for i in itertools.product(*[pDeltaBrList,pzDeltaBrList,pzDeltaBrList]):
        combinationList.append(i)
   
    print len(combinationList)
    
    goodCombinationList=[]
    for i in combinationList:
        if(abs(i[0]+i[1]+i[2])<0.001):
            goodCombinationList.append(i)
            
    possibleVar=range(len(goodCombinationList))
    for i in range(len(goodCombinationList)):
       possibleVar[i] = min(find_frequency(goodCombinationList[i][0],pFreq), find_frequency(goodCombinationList[i][1],pzFreq) , find_frequency(goodCombinationList[i][2],pzFreq)) 
        
    possibleVariationsList = unite_list(possibleVar,goodCombinationList)
    possibleVariationsList.sort
    print possibleVariationsList
    
    print len(goodCombinationList)
    
def unite_list(list1,list2):
    result = range(len(list1))
    for i in range(len(list1)):
        result[i] = [list1[i],list2[i]]
    return result
    
def find_frequency(value,list):
    for i in list:
        if(value==i[0]): return i[1]
    
   
def return_bracket(value): 
    return round(value,2)
    
def create_bracket_list(mirrorList,listType):
    
    BracketList=[]
    for i in mirrorList:
        if(listType=="delta"): BracketList.append(i.deltaBracket)
        else:BracketList.append(i.L0Bracket)
    BracketList=set(BracketList)
    BracketList=list(BracketList)
    BracketList.sort()
    print BracketList
    return BracketList

def create_frequency_list(brList, mirrorsList):
    frequencyList=range(len(brList))
    for i in range(len(brList)):
        freq=0
        for j in mirrorsList:
            if(j.deltaBracket==brList[i]): freq+=1
        frequencyList[i]=freq
    print frequencyList
    return frequencyList

class Mirror:
    def __init__(self, name, delta, L0, box, place, radius):
        self.used=0
        self.name = name
        self.delta = round(delta,3)
        self.deltaBracket=return_bracket(self.delta)
        self.L0 = L0
        if(type(self.L0)<>float):
            self.L0=999
            print "Empty L0 on", self.name
        self.L0Bracket= return_bracket(self.L0)
        self.combinationsCount=0
        
        self.place = str(box) +"-"+ str(place)
        
        
#        if (model == u"Плоское"):self.model=0
#        if (model == u"Пьезо"):self.model=1
#        if (model == u"Сфера"):
#            self.model=3
        #print radius
        #self.radius=round(radius,1)
        self.radius = radius
    def report(self):
        print self.name, self.delta, self.L0, self.place, self.radius
        #main.ex.qlist.addItem("aa")
    
        
main()