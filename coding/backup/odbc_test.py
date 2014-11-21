#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import pyodbc
import sys
from PyQt4 import QtGui, QtCore
import itertools
import operator


class Gui(QtGui.QWidget):
    
    def __init__(self):
        super(Gui, self).__init__()
        
        self.initUI()
        
    def initUI(self):               
        
        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(1180, 700)       
        self.qlist=QtGui.QListWidget(self)
        self.qlist.resize(1100,620)
        #qlist.addItem("L0 = 456| B12 13pz, B06 11p, B03 12q, B23 5654m")
#        qlist.setColumnCount(5)
#        qlist.setItem(3,3,"aaa")
        self.setGeometry(30, 30, 1280, 800)
        self.setWindowTitle('Quit button')    
        self.show()
        
    def add_item(self,finalList):
        for i in finalList:
            self.qlist.addItem(i)
        
def findmax(group):
    maxVal=0
    position=0
    for i in range(len(group)):
        if (maxVal<abs(group[i].delta)):
            maxVal = abs(group[i].delta) 
            position = i
    return position


    

def main():
    

    db = pyodbc.connect('DSN=test')
    cursor=db.cursor()
    
    #cursor.execute(u"SELECT Zerki.нПодложки, Zerki.Тзер, Zerki.Сигма, Zerki.L0, Zerki.МесХран, Zerki.Ячейка, Zerki.Рсферы FROM Zerki WHERE (((Zerki.МесХран) Is Not Null) AND ((Zerki.Ячейка) Is Not Null) AND ((Zerki.Рсферы)=3.6 Or (Zerki.Рсферы) Is Null) AND ((Zerki.ГОтказ)='Годен') AND ((Zerki.[Материал подл]) Is Null) AND ((Zerki.Вкомп)='Свободно') AND ((Zerki.НранВоз) Is Null) AND ((Zerki.[Годен для Тамбова])<>'тт'));")
    cursor.execute(u"SELECT DISTINCTROW zerki.нПодложки, zerki.Тзер, zerki.Сигма, zerki.L0, zerki.МесХран, zerki.Ячейка, zerki.Рсферы FROM zerki WHERE (((zerki.[Материал подл]) Is Null) AND ((zerki.ГОтказ)='Годен') AND ((zerki.Вкомп)='Свободно') AND ((zerki.НранВоз) Is Null));")
    data=cursor.fetchall()
    
    global minL0, maxL0
    global minDelta
    global maxDelta
    
    
    
    searchType="K-5"  ## "EK-104" or"K-5"
    
    if(searchType=="K-5"):
        minL0=0.14
        maxL0=0.16
    else:
        maxL0=999
        minL0=0.20
        
    minDelta=-0.1
    maxDelta=0.1

#mirrorsList=[]
#for i in range(len(data)):
#    mirrorsList.append(Mirror(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]))

    flatList=[]
    piezoList=[]
    sphereList=[]
    for i in range(len(data)):
        if(data[i][1] == u"Плоское"): flatList.append(Mirror(data[i][0], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]))
        if(data[i][1] == u"Пьезо"): piezoList.append(Mirror(data[i][0], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]))
        if(data[i][1] == u"Сфера" and (abs(data[i][6] - 3.6))<0.1): sphereList.append(Mirror(data[i][0], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]))
        
   


    
#    for i in range(len(flatList)):
#        flatL0.append(flatList[i].L0)
#    print flatL0
    
    combinationList=[]
    deltaSumList=[]
    L0SumList=[]

   
    for i in itertools.product(*[flatList,piezoList,piezoList]):
        combinationList.append(i)
    
    print len(combinationList) 
  
    for i in combinationList:
        deltaSumList.append(i[0].delta+i[1].delta+i[2].delta)
        L0SumList.append(i[0].L0+i[1].L0+i[2].L0)

    print len(piezoList),"(/2)", len(sphereList), len(flatList)
#
#    
#    for i in itertools.product(*[flatL0,piezoL0,piezoL0]):
#        L0SumList.append(sum(i))
#        debugLList.append(i)
#    
#    for i in itertools.product(*[flatIndex,piezoIndex,piezoIndex]):
#        indexList.append(i)
#        
#    for i in itertools.product(*[flatDelta,piezoDelta,piezoDelta]):
#        deltaSumList.append(sum(i))
#        debugDList.append(i)
        
   



#    combinedList=[]
#
#    for i in range(len(deltaSumList)):
#        if(abs(deltaSumList[i])<0.01 and L0SumList[i] > minL0 and L0SumList[i]< maxL0): combinedList.append(i)
        
    groupList=[]    
    for i in range(len(combinationList)):
        for j in range(len(sphereList)):
            L0TotalSum=L0SumList[i] + sphereList[j].L0
            deltaTotalSum = deltaSumList[i] + sphereList[j].delta
            if (L0TotalSum>=minL0 and L0TotalSum<=maxL0 and abs(deltaTotalSum) <= maxDelta and combinationList[i][1]<>combinationList[i][2] ): 
               
#                print "======="
               
#                print L0TotalSum, L0SumList[i], sphereList[j].L0
#                print deltaTotalSum, deltaSumList[i], sphereList[j].delta
#                print debugDList[combinedList[i]], "<--"
#                print debugLList[combinedList[i]], "<--L"
                #print indexList[i], j
                
                groupList.append(Group())
                groupList[len(groupList)-1].add(combinationList[i][0]) 
                groupList[len(groupList)-1].add(combinationList[i][1])
                groupList[len(groupList)-1].add(combinationList[i][2]) 
                groupList[len(groupList)-1].add(sphereList[j])
                groupList[len(groupList)-1].check()
#                groupList[len(groupList)-1].report()

    
    print len(groupList)
            
#    print len(groupList)
#    for i in range(len(groupList)):
#        if ([1]==groupList[i][2]): groupList.remove(groupList[i])
    
#    print len(groupList)
#    
    
#    print findmax(piezoList)
    
   

       
#    first=Group()
#    first.add(flatList[0])
#    first.add(piezoList[17])
#    first.add(piezoList[15])
#    first.add(sphereList[20])
    
#    first.report()
    
#    for i in itertools.product(*[flatDelta,piezoDelta,piezoDelta]):
#        print sum(i), i
    
    minLen=len(flatList)
    if(len(piezoList)<minLen):minLen=len(piezoList)
    if(len(sphereList)<minLen):minLen=len(sphereList)  
    
    #for i in range(minLen):
        
    
    for i in piezoList:
        counter=0
        for j in groupList:
            if (j[1]==i or j[2]==i): counter+=1
        i.combinationsCount=counter
        
    for i in flatList:
        counter=0
        for j in groupList:
            if (j[0]==i): counter+=1
        i.combinationsCount=counter
        
    for i in sphereList:
        counter=0
        for j in groupList:
            if (j[3]==i): counter+=1
        i.combinationsCount=counter
        
    for i in groupList:
        i.combinations_count()
    
    
    
    groupList.sort(key=operator.attrgetter('deltaSumAbs'))
    #groupList.sort(key=operator.attrgetter('combinationsCount'),reverse=False)
    
    
    groupList[0].report()
    
   
    finalList=[]
    for i in range(len(groupList)):
        if(abs(groupList[i].check_used())<0.1):
           
#            count=0
#            for j in groupList:
#                if(j.check_used()==1):count+=1
#            print "group", count
#             
#            count=0
#            for j in sphereList:
#                if(j.used==0):count+=1
#            print "sphere", count 
#            
#            count=0
#            for j in flatList:
#                if(j.used==0):count+=1
#            print "flat", count 
#             
#            count=0
#            for j in piezoList:
#                if(j.used==0):count+=1
#            print "piezo", count 
             
            finalList.append(groupList[i])
            groupList[i].make_used()


    app = QtGui.QApplication(sys.argv)
    ui = Gui()
    screenList=[]
    for i in range(len(finalList)):
        screenList.append(finalList[i].UI_report())
    
    Gui.add_item(ui,screenList)
    
    
    
    
    sys.exit(app.exec_())



class Mirror:
    def __init__(self, name, delta, L0, box, place, radius):
        self.used=0
        self.name = name
        self.delta = round(delta,3)
        self.L0 = L0
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
    
        

class Group():
    def __init__(self):
        self.list=[]
        self.type = "Bad"
        self.deltaSum=0
        self.L0Sum=0
        self.deltaSumAbs=0
        self.combinationsCount=0
    
    def check_used(self):
        for i in range(len(self.list)):
            if(abs(self.list[i].used)>0.1):return 1
        return 0
        
    def make_used(self):
        for i in range(len(self.list)):
            self.list[i].used = 1
    
    def combinations_count(self):
        count=self.list[0].combinationsCount
        for i in range(1,4):
            if(self.list[i]<count):count = self.list[i]
        self.combinationsCount=count        

    def __getitem__(self,num):
        return self.list[num]
    
    def add(self,Mirror):
        self.list.append(Mirror)
        
    def report(self):
        self.check()
        for i in self.list:
            i.report()
        print self.type, self.deltaSum, self.L0Sum, self.combinationsCount
    
    def UI_report(self):
        self.check()
        returnString =""
        returnString+= ("L0 = " + str(self.L0Sum))
        returnString+= (" phase = " + str(self.deltaSum) + " ")
        for i in range(4):
            returnString+= (self.list[i].name + " (" + self.list[i].place + ") ")
        returnString += str(self.list[3].delta)
        return returnString
        
    def check(self):
        if(len(self.list)<>4): 
            self.type = "Bad"
            return 0
        self.deltaSum=0
        self.L0Sum=0
        for i in range(4):
            self.deltaSum += self.list[i].delta
            self.L0Sum += self.list[i].L0
        self.deltaSum=round(self.deltaSum,3)
        self.deltaSumAbs = abs(self.deltaSum)
        if (self.L0Sum > minL0  and self.L0Sum < maxL0 and self.deltaSum < maxDelta and self.deltaSum > minDelta):self.type = "Good"
    
    def sort_delta(self):
        return self.deltaSum

main()

