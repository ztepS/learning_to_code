#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import pyodbc
import sys
from PyQt4 import QtGui, QtCore



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
        
def main():
    

    db = pyodbc.connect('DSN=test')
    cursor=db.cursor()
    cursor.execute(u"SELECT Zerki.нПодложки, Zerki.Тзер, Zerki.Сигма, Zerki.L0, Zerki.МесХран, Zerki.Ячейка, Zerki.Рсферы FROM Zerki WHERE (Zerki.ГОтказ='Годен' AND zerki.[Материал подл] Is Null AND zerki.Вкомп='Свободно' AND zerki.НранВоз Is Null);")
    data=cursor.fetchall()
    

#mirrorsList=[]
#for i in range(len(data)):
#    mirrorsList.append(Mirror(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]))

    flatList=[]
    piezoList=[]
    sphereList=[]
    for i in range(len(data)):
        if(data[i][1] == u"Плоское"): flatList.append(Mirror(data[i][0], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]))
        if(data[i][1] == u"Пьезо"): piezoList.append(Mirror(data[i][0], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]))
        if(data[i][1] == u"Сфера"): sphereList.append(Mirror(data[i][0], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]))


    first=Group()
    first.add(flatList[3])
    first.add(piezoList[3])

    first.report()

    app = QtGui.QApplication(sys.argv)
    ui = Gui()
    
    testList=["dfgg"]
    Gui.add_item(ui,testList)
    
    
    
    
    sys.exit(app.exec_())



class Mirror:
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
        #main.ex.qlist.addItem("aa")
    
        

class Group():
    def __init__(self):
        self.list=[]
    
    def add(self,Mirror):
        self.list.append(Mirror)
        
    def report(self):
        for i in self.list:
            i.report()
        

main()

