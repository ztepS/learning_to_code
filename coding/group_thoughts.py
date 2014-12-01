#!/usr/bin/env python 
# -*- coding: utf-8 -*-




# todo:    
#        
#        

#        refactor to use numpy? use fixed randomDataSize array
#        use integers?
#        is double search on pz needed?
#        selection algorythm is still bad

#        S0!!!




import random
import itertools
import time
import datetime
import cPickle
import os
import pyodbc
import sys
#from groupInterface import Ui_Dialog
from PyQt4 import QtGui, QtCore

from PyQt4.QtGui import QApplication, QDialog
random.seed()

typeSearch = "real data"  # random numbers or real data

randomDataSize = 50


timeStart = time.time()

# searchType="EK-104"  ## "EK-104" or"K-5" or "all"
    


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

 
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(406, 170)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(300, 130, 71, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.searchType = QtGui.QComboBox(Dialog)
        self.searchType.setGeometry(QtCore.QRect(50, 10, 141, 22))
        self.searchType.setObjectName(_fromUtf8("searchType"))
        self.searchType.addItem(_fromUtf8(""))
        self.searchType.addItem(_fromUtf8(""))
        self.searchType.addItem(_fromUtf8(""))
        self.searchType.addItem(_fromUtf8(""))
        self.progressBar1 = QtGui.QProgressBar(Dialog)
        self.progressBar1.setGeometry(QtCore.QRect(20, 100, 261, 23))
        self.progressBar1.setProperty("value", 0)
        self.progressBar1.setObjectName(_fromUtf8("progressBar1"))
        self.searchButton = QtGui.QPushButton(Dialog)
        self.searchButton.setGeometry(QtCore.QRect(300, 100, 71, 23))
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
#        self.groupBox = QtGui.QGroupBox(Dialog)
#        self.groupBox.setGeometry(QtCore.QRect(20, 90, 341, 121))
#        self.groupBox.setObjectName(_fromUtf8("groupBox"))
#        self.FlatcomboBox = QtGui.QComboBox(self.groupBox)
#        self.FlatcomboBox.setGeometry(QtCore.QRect(20, 20, 301, 22))
#        self.FlatcomboBox.setObjectName(_fromUtf8("FlatcomboBox"))
#        self.PiezocomboBox = QtGui.QComboBox(self.groupBox)
#        self.PiezocomboBox.setGeometry(QtCore.QRect(20, 50, 301, 22))
#        self.PiezocomboBox.setObjectName(_fromUtf8("PiezocomboBox"))
#        self.SpherecomboBox = QtGui.QComboBox(self.groupBox)
#        self.SpherecomboBox.setGeometry(QtCore.QRect(20, 80, 301, 22))
#        self.SpherecomboBox.setObjectName(_fromUtf8("SpherecomboBox"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 60, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 60, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.timer1 = QtGui.QLabel(Dialog)
        self.timer1.setGeometry(QtCore.QRect(130, 250, 46, 13))
        self.timer1.setText(_fromUtf8(""))
        self.timer1.setObjectName(_fromUtf8("timer1"))
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(200, 10, 121, 18))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.S0checkBox = QtGui.QCheckBox(Dialog)
        self.S0checkBox.setGeometry(QtCore.QRect(200, 30, 171, 18))
        self.S0checkBox.setObjectName(_fromUtf8("checkBox"))



        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.searchType.setItemText(0, _translate("Dialog", "ЭК-104 и К-5", None))
        self.searchType.setItemText(1, _translate("Dialog", "ЭК-104", None))
        self.searchType.setItemText(2, _translate("Dialog", "К-5", None))
        self.searchType.setItemText(3, _translate("Dialog", "Комплекты с любым L0", None))
        self.searchButton.setText(_translate("Dialog", "Поиск", None))
#        self.groupBox.setTitle(_translate("Dialog", "для К-5", None))
        self.lineEdit.setText(_translate("Dialog", "0.001", None))
        self.label.setText(_translate("Dialog", "Дельта не более", None))
        self.checkBox.setText(_translate("Dialog", "Использовать \"тт\"", None))
        self.S0checkBox.setText(_translate("Dialog", "Использовать S0>0.007 в К5", None))

def PrintResultList(resultList):
    for i in resultList:
        groupStr = ""
        delta = piezoList[i[0]][0] + piezoList[i[1]][0] + flatList[i[2]][0] + sphereList[i[3]][0]
        L0 = piezoList[i[0]][1] + piezoList[i[1]][1] + flatList[i[2]][1] + sphereList[i[3]][1]

    
        groupStr += str(piezoListFull[i[0]][0]) + "(" + str(piezoListFull[i[0]][4]) + "-" + str(piezoListFull[i[0]][5]) + ") "
        groupStr += str(piezoListFull[i[1]][0]) + "(" + str(piezoListFull[i[1]][4]) + "-" + str(piezoListFull[i[1]][5]) + ") "
        groupStr += str(flatListFull[i[2]][0]) + "(" + str(flatListFull[i[2]][4]) + "-" + str(flatListFull[i[2]][5]) + ") "
        groupStr += str(sphereListFull[i[3]][0]) + "(" + str(sphereListFull[i[3]][4]) + "-" + str(sphereListFull[i[3]][5]) + ") "
        groupStr += "L0 = " + str(L0) + " delta = " + str(round(delta, 3)) + "\n"
        file1.write(groupStr)
               
def PrintResultDataConsole(typeList):
    global resultListE, resultListK, flatListFull, piezoListFull, sphereListFull 
    if(typeList == "E"): resultInternal = resultListE
    elif(typeList == "K"):resultInternal = resultListK
    for i in resultInternal:
    
        if(typeSearch == "real data"): print  piezoListFull[i[0]]
        else: print piezoList[i[0]]
        if(typeSearch == "real data"): print  piezoListFull[i[1]]
        else: print piezoList[i[1]] 
        if(typeSearch == "real data"): print  flatListFull[i[2]]
        else: print flatList[i[2]]  
        if(typeSearch == "real data"): print  sphereListFull[i[3]]
        else: print sphereList[i[3]] 
 
        print "delta = ", piezoList[i[0]][0] + piezoList[i[1]][0] + flatList[i[2]][0] + sphereList[i[3]][0]   
        print "L0 = ", piezoList[i[0]][1] + piezoList[i[1]][1] + flatList[i[2]][1] + sphereList[i[3]][1]    
    
def GetRealData():
    
    global flatListFull, sphereListFull, piezoListFull
    
    
    db = pyodbc.connect('DSN=zerki_local')
    cursor = db.cursor()
    
    # cursor.execute(u"SELECT DISTINCTROW zerki.нПодложки, zerki.Тзер, zerki.Сигма, zerki.L0, zerki.МесХран, zerki.Ячейка, zerki.Рсферы FROM zerki WHERE (((zerki.[Материал подл]) Is Null) AND ((zerki.ГОтказ)='Годен') AND ((zerki.Вкомп)='Свободно') AND ((zerki.НранВоз) Is Null));")
    if(ui.checkBox.isChecked()==0): 
        cursor.execute(u"SELECT DISTINCTROW zerki.нПодложки, zerki.Тзер, zerki.Сигма, zerki.L0, zerki.МесХран, zerki.Ячейка, zerki.Рсферы, zerki.[Годен для Тамбова], zerki.MaxS FROM zerki WHERE (((zerki.[Материал подл]) Is Null) AND ((zerki.ГОтказ)='Годен') AND ((zerki.Вкомп)='Свободно') AND ((zerki.НранВоз) Is Null)) AND zerki.[Годен для Тамбова] <>'тт';")
    else: cursor.execute(u"SELECT DISTINCTROW zerki.нПодложки, zerki.Тзер, zerki.Сигма, zerki.L0, zerki.МесХран, zerki.Ячейка, zerki.Рсферы, zerki.[Годен для Тамбова], zerki.MaxS FROM zerki WHERE (((zerki.[Материал подл]) Is Null) AND ((zerki.ГОтказ)='Годен') AND ((zerki.Вкомп)='Свободно') AND ((zerki.НранВоз) Is Null));")

    # AND zerki.[Годен для Тамбова] <>'тт'
    data = cursor.fetchall()
    
    
    global flatListFull
    global piezoListFull
    global sphereListFull
    global flatList
    global sphereList
    global piezoList
    global totalSize
    
    
    flatListFull = []
    piezoListFull = []
    sphereListFull = []
    flatList = []
    sphereList = []
    piezoList = []
    
    
    
    
    flatCount = 0
    piezoCount = 0
    sphereCount = 0
    for i in range(len(data)):
        # print type(data[i][3])
        if(data[i][3] is None): 
            data[i][3] = 999
            print "Empty L0"
        if(data[i][2] is None): 
            data[i][2] = 999
            print "Empty delta"
        if(data[i][1] == u"Плоское"): 
            flatCount += 1
            flatListFull.append([data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], flatCount - 1, data[i][8]])
        
        if(data[i][1] == u"Пьезо"): 
            piezoCount += 1
            piezoListFull.append([data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], piezoCount - 1, data[i][8]])
        
        if(data[i][1] == u"Сфера" and (abs(data[i][6] - 3.6)) < 0.1): 
            sphereCount += 1
            sphereListFull.append([data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], sphereCount - 1, data[i][8]])
    
    # print flatListFull[1]
    for i in flatListFull: flatList.append([round(i[2], 3), i[3], i[6], i[7]])
    for i in sphereListFull: sphereList.append([round(i[2], 3), i[3], i[6], i[7]])
    for i in piezoListFull: piezoList.append([round(i[2], 3), i[3], i[6], i[7]])
    totalSize = (len(piezoList) * len(piezoList) * len(sphereList) * len(flatList))
    print len(piezoList), len(sphereList), len(flatList)
    
def Store(data, number):
    file1 = "temp." + str(number)
    output = open(file1, 'wb')
    cPickle.dump(data, output)
    output.close()

def DefragmentStorage():
    global pickles
    combinationStoredList = []
    newPickle = 1
    counter = 0
    for j in range(pickles):
        
        file1 = "temp." + str(j + 1)
        pkl_file = open(file1, 'rb')
        combinationStoredListOld = cPickle.load(pkl_file)
        
        for i in combinationStoredListOld:
            
            if(CheckUsed(i) == 0):
                combinationStoredList.append(i)
                counter += 1
                
                if(counter == 1000000) :
                    Store(combinationStoredList, newPickle)
                    newPickle += 1
                    combinationStoredList = []
                    counter = 0
            del(i)
        print counter
        pkl_file.close()
    Store(combinationStoredList, newPickle)
    # newPickle+=1
    print "before ", pickles, "after ", newPickle
    pickles = newPickle
    
def CheckUsedMirror(mirrType, mirrId):

    
    if(mirrType == 2 and flatList[mirrId][4] == 1): return 1
    if(mirrType == 3 and sphereList[mirrId][4] == 1): return 1
    if(mirrType == 0  and piezoList[mirrId][4] == 1): return 1
    return 0

def CheckUsed(combination):
    # if (combination==0): return 1
    if (piezoList[combination[0]][4] == 1):return 1
    if (piezoList[combination[1]][4] == 1):return 1
    if (flatList[combination[2]][4] == 1):return 1
    if (sphereList[combination[3]][4] == 1):return 1
    return 0

def MakeUsed(combination):
    piezoList[combination[0]][4] = 1
    piezoList[combination[1]][4] = 1
    flatList[combination[2]][4] = 1
    sphereList[combination[3]][4] = 1
    return

def CombinationsSearch(combType, combId):

    for j in range(pickles):
        
        file1 = "temp." + str(j + 1)
        pkl_file = open(file1, 'rb')
        combinationStoredList = cPickle.load(pkl_file)
        for i in combinationStoredList:
            if(i[combType] == combId and CheckUsed(i) == 0): 
                return i
        pkl_file.close()
    print "none found"
    return 0

##random numbers 
##remove GetRealData to work    
#if(typeSearch == "random numbers"):
#    flatList = range(randomDataSize)
#    for i in range(randomDataSize):
#        flatList[i] = range(3)
#        flatList[i][0] = float(random.randrange(-110, 110)) / 1000
#        flatList[i][1] = float(random.randrange(9, 16)) / 100
#        flatList[i][2] = i
#    
#
#    piezoList = range(randomDataSize * 2)
#    for i in range(randomDataSize * 2):
#        piezoList[i] = range(3)
#        piezoList[i][0] = float(random.randrange(-110, 110)) / 1000
#        piezoList[i][1] = float(random.randrange(1, 4)) / 1000  # rethink
#        piezoList[i][2] = i
#    
#
#
#    sphereList = range(randomDataSize)
#    for i in range(randomDataSize):
#        sphereList[i] = range(3)
#        sphereList[i][0] = float(random.randrange(-110, 110)) / 1000
#        sphereList[i][1] = float(random.randrange(1, 4)) / 1000
#        sphereList[i][2] = i
#    totalSize = (randomDataSize ** 4) * 4

def Search():
    
    GetRealData()
    
    PhaseOne()
    
    PhaseTwo()
    
    PhaseThree() 
    
    FileOutput()   

    Cleanup()

def PhaseOne():
    
    global totalSize
    global pickles
    global goodList
    global picklesMaximum
    
    global minL0K, maxL0K, minL0E, maxL0E, minDelta, maxDelta
    
    if(ui.searchType.currentIndex()==0):
        minL0K = 0.14
        maxL0K = 0.16   
        maxL0E = 999
        minL0E = 0.20
        
    elif(ui.searchType.currentIndex()==1):
        minL0K = 0
        maxL0K = 0   
        maxL0E = 999
        minL0E = 0.20
        
    elif(ui.searchType.currentIndex()==2):
        minL0K = 0.14
        maxL0K = 0.16   
        maxL0E = 0
        minL0E = 0
        
    elif(ui.searchType.currentIndex()==3):
        minL0K = 0
        maxL0K = 100
        maxL0E = 0
        minL0E = 0
    # elif(searchType=="all"):
    #    maxL0E=999
    #    minL0E=0
    
    
    quotaDelta = float(ui.lineEdit.text())  #   0.11 default
    
    
    minDelta = -quotaDelta
    maxDelta = quotaDelta
    
    if(ui.S0checkBox.isChecked()==0): quotaS0=0.007
    else: quotaS0=999
        
    
    
    delta = 0
    L0 = 0
    combinationList = []
    goodList = []
    percent = 0.0
    counter = 0
    pickles = 0
    counterGood = 0
    counterIterations = 0
    counterFile = 0
        
    
    timeIterStart = time.time() 
    for i in itertools.product(*[piezoList, piezoList, flatList, sphereList]):
        delta = i[0][0] + i[1][0] + i[2][0] + i[3][0]
#        try:
        k5=0 
        L0 = i[0][1] + i[1][1] + i[2][1] + i[3][1]
        if(L0 >= minL0K and L0 <= maxL0K):
            if(i[0][3]<=quotaS0 and i[1][3]<=quotaS0 and i[2][3]<=quotaS0 and i[2][3]<=quotaS0):k5=1
#            else: print  i[0][3], i[1][3], i[2][3], i[3][3]
#        except TypeError: L0 = 0
        if(abs(delta) <= maxDelta and ((k5==1) or (L0 >= minL0E and L0 <= maxL0E)) and i[0][2] <> i[1][2]):
            combinationList.append([i[0][2], i[1][2], i[2][2], i[3][2]])
            counterGood += 1
        counter += 1
        
        if(counter == 1000000):
            percent = float(counter) * (counterIterations + 1) * 100 / totalSize
            print percent, "%  of phase 1"
            ui.progressBar1.setValue(percent)
            
            counterIterations += 1
            counter = 0
            if(percent <> 0): 
                secondCount = ((time.time() - timeIterStart) * 100 / percent - (time.time() - timeIterStart))  
                print str(datetime.timedelta(seconds=secondCount)), " eta"
    
    
        if(counterGood == 1000000):  
            counterFile += 1 
            file1 = "temp." + str(counterFile)
            output = open(file1, 'wb')
            cPickle.dump(combinationList, output)
            output.close()
            combinationList = []
            pickles += 1
            
            counterGood = 0
            print "used up to ", counterFile * 33.152, "Mb"
    
    totalSize = len(combinationList) + pickles * 1000000
    pickles += 1
    file1 = "temp." + str(pickles)
    output = open(file1, 'wb')
    cPickle.dump(combinationList, output)
    output.close()
    ui.progressBar1.setValue(100)
    picklesMaximum = pickles
    
    #   rewrite? code repetition
    
    for i in flatList:
        i.append(0)  # frequency
        i.append(0)  # used
        
        
    for i in sphereList:
        i.append(0)
        i.append(0)
        
    for i in piezoList:
        i.append(0)
        i.append(0)

def PhaseTwo():
    
    global pickles, flatList, sphereList, piezoList
    
    for j in range(pickles):
        percent=j*100/pickles
        ui.progressBar1.setValue(percent)
        file1 = "temp." + str(j + 1)
        pkl_file = open(file1, 'rb')
        print j + 1, " out of", pickles, " to complete phase 2"
        combinationStoredList = cPickle.load(pkl_file)
        for i in combinationStoredList:
            flatList[i[2]][4] += 1
            sphereList[i[3]][4] += 1
            piezoList[i[0]][4] += 1
            piezoList[i[1]][4] += 1
        pkl_file.close()
    ui.progressBar1.setValue(100)

def PhaseThree():
    
    global pickles, flatList, sphereList, piezoList, resultListK, resultListE
    
    flatCount = 0
    piezoCount = 0
    sphereCount = 0
    
    unitedFreqList = []
    result = []
    for i in flatList:
       
        if i[4] > 0:
            result = [2, i[2], i[4]]
            unitedFreqList.append(result)
            flatCount += 1
    
    for i in sphereList:
        if i[4] > 0:
            result = [3, i[2], i[4]]
            unitedFreqList.append(result)
            sphereCount += 1
    
    for i in piezoList:
        if i[4] > 0:
            result = [0, i[2], i[4]]
            unitedFreqList.append(result)
            piezoCount += 1
    
    unitedFreqList.sort(cmp=None, key=lambda unitedFreqList: unitedFreqList[2], reverse=False)
    
    
    maxPossibleCombinations = min(flatCount, piezoCount, sphereCount)
    print maxPossibleCombinations
    
    
    #   needs big rethinking
    
    
    combinationCount = 0
    result = []
    defragCounter = 0
    resultListE = []
    resultListK = []
    
    for i in unitedFreqList:
        # print i
#        found = 0
        
        progress= combinationCount*100/maxPossibleCombinations
        ui.progressBar1.setValue(progress)
        if(CheckUsedMirror(i[0], i[1]) == 0 and combinationCount < maxPossibleCombinations): 
            
            result = CombinationsSearch(i[0], i[1])
            # print result,">", i[1] ,"<"
            
            if(result <> 0):
                      
                MakeUsed(result)
                print(result)
#                delta = piezoList[result[0]][0] + piezoList[result[1]][0] + flatList[result[2]][0] + sphereList[result[3]][0]
                L0 = piezoList[result[0]][1] + piezoList[result[1]][1] + flatList[result[2]][1] + sphereList[result[3]][1]
                
                if(L0 < maxL0E and L0 > minL0E): resultListE.append(result)
                if(L0 < maxL0K and L0 > minL0K): resultListK.append(result)
                combinationCount += 1
                
                defragCounter += 1
                if(defragCounter > (maxPossibleCombinations / 8)):
                    DefragmentStorage()    
                    defragCounter = 0
                    
                    
                    
                    
    
    ui.progressBar1.setValue(100)                
    print len(resultListE), len(resultListK)    
    
# loop 1

#app = QApplication(sys.argv)
#window = QDialog()
#ui = Ui_Dialog()
#ui.setupUi(window)
#
#window.show()


#app.connect(Ui_Dialog.searchButton, Qt.SIGNAL("clicked()"), phaseOne())  
  
def Cleanup():
    global picklesMaximum
    for i in range(picklesMaximum):
        file1 = "temp." + str(i + 1)
        os.remove(file1)
        
def FileOutput():
    global resultListK, resultListE, file1 
    file1 = open("group.txt", 'w')
    file1.write("K-5:\n")
    PrintResultList(resultListK)
    file1.write("\nЭK-104:\n")
    PrintResultList(resultListE)
    file1.close()
    os.system("start " + "group.txt")       




        
delta = 0
L0 = 0
combinationList = []
goodList = []
percent = 0.0
counter = 0
pickles = 0
counterGood = 0
counterIterations = 0
counterFile = 0

    
          

        
#    print flatList[i[2][2]]
    

# flatList.sort(cmp=None, key=lambda flatList: flatList[3], reverse=True)
# sphereList.sort(cmp=None, key=lambda sphereList: sphereList[3], reverse=True)
# piezoList.sort(cmp=None, key=lambda piezoList: piezoList[3], reverse=True)


        
# PrintResultDataConsole("E")
# PrintResultDataConsole("K")        


app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)

window.show()
#GetRealData() 

app.connect(ui.searchButton, QtCore.SIGNAL("clicked()"), Search)








       






print (time.time() - timeStart) / 60, " min."


sys.exit(app.exec_())










