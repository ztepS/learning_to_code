#!/usr/bin/env python 
# -*- coding: utf-8 -*-



import os.path as path
import datetime
import pyodbc
import sys
from PyQt4 import QtCore, QtGui, uic
import ctypes.wintypes

reload(sys)  
sys.setdefaultencoding('utf8')


sys.stdout = open("stdout.log", "w")
sys.stderr = open("errors.log", "w")

def DeltaToSigma(delta):
    pi=3.14159265
      
    sigma=(float(delta)-180)*(pi/180)
    
    return sigma

class ImageDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)

# Set up the user interface from Designer.
        self.ui = uic.loadUi("lef.ui")
        self.ui.show()
        self.ui.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
## Make some local modifications.
#         self.ui.colorDepthCombo.addItem("2 colors (1 bit per pixel)")
#

#        button = QtGui.QPushButton("start")
        
        QtCore.QObject.connect(self.ui.startButton, QtCore.SIGNAL('clicked()'), search)
        
#        button2 = QtGui.QPushButton("start")
        
        QtCore.QObject.connect(self.ui.exitButton, QtCore.SIGNAL('clicked()'), sys.exit)
        
        
    def ErrorMessage(self, text):
        reply = QtGui.QMessageBox.critical(self, u'Ошибка',
             text ,  QtGui.QMessageBox.Ok)

    def InfoMessage(self, text):
        reply =  QtGui.QMessageBox.information(self, '', u'''Данные успешно внесены''',
            QtGui.QMessageBox.Ok)
        
def search():
    
    
    processId = str(window.ui.processName.text())
    
    sqlQuery=u"SELECT PodlP.НпПодл FROM PodlP WHERE ((PodlP.НомПартии)='"+processId+"' ) ORDER BY PodlP.НпПодл;"
    
  
    db = pyodbc.connect('DSN=zerki_current')
    cursor = db.cursor()
    cursor.execute(sqlQuery)
    names=cursor.fetchall()
    substratesCountDb=len(names)
    
    filmDateSys = window.ui.dateEdit.date().toPyDate()
    filmDate="#"+ str(filmDateSys.day)+"/"+ str(filmDateSys.month) + "/" + str(filmDateSys.year)+ "#"
    currentDateSys=datetime.date.today()
    currentDate="#"+ str(currentDateSys.day)+"/"+ str(currentDateSys.month) + "/" + str(currentDateSys.year)+ "#"
    
    
    
    
    #print substratesCountDb
    
    if(substratesCountDb>0):
        
        sqlQuery=u"SELECT Count(Zerki.нПодложки) AS count FROM Zerki INNER JOIN PodlP ON Zerki.нПодложки = PodlP.НпПодл WHERE (((PodlP.НомПартии)='"+processId+"'));"
        cursor.execute(sqlQuery)
        
        if(cursor.fetchall()[0][0]==0):
           
            sqlQuery=(u"INSERT INTO Zerki ([нПодложки], [Тзер], [Рсферы], [Рсф_изм], [N], [ДельтаN], [Тнап], [ДатаНап], [ДатаПол], [Исп]) "
                      u"SELECT [НпПодл], [Тзер], [РсферыНом] , [РсферыИзм], [N], [ДельтаN], [ТипНап], "+ filmDate +", " + currentDate + u", 'Расев' "
                      u"FROM PodlP "
                      u"WHERE (((PodlP.НомПартии)='"+processId+"'));")
            
            #print sqlQuery
            cursor.execute(sqlQuery)
            db.commit()
        #else: print "already present"
            
    phaseListDeg=[]
    
    CSIDL_PERSONAL= 5       # My Documents
    SHGFP_TYPE_CURRENT= 0   # Want current, not default value
    buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(0, CSIDL_PERSONAL, 0, SHGFP_TYPE_CURRENT, buf)
    buf.value
#    print path.expanduser("~\\"+processId+".ppd")
    fname=buf.value +u"\\Процессы\\"+ processId+".ppd"
    if (path.isfile(fname) is True):  
        f = open(fname, 'r')
    else: 
        window.ErrorMessage(u"Не найден файл "+processId+".ppd")
        return 0
    
    a = f.readlines()
    for i in a:
        if(i<>"\n"): phaseListDeg.append(i.split(" ")[2]) 
    
    #print len(phaseListDeg)
    
    phaseListRad=[]
    for i in phaseListDeg:
        phaseListRad.append(DeltaToSigma(i))
        
        
    counter=0
    if(len(phaseListDeg)==substratesCountDb):
        for i in names:
            #print i[0]
            sqlQuery=(u"Update Zerki "
                      u"SET [Сигма]="+str(phaseListRad[counter])+" "
                      u"WHERE Zerki.НПодложки='"+i[0]+"'")
            counter+=1
            #print sqlQuery
            cursor.execute(sqlQuery)
        db.commit()
    else: 
        window.ErrorMessage(u"Не совпадает количество подложек.")
        return 0
    
    window.InfoMessage(u"Данные успешно добавлены.")
    
app = QtGui.QApplication(sys.argv)
window = ImageDialog()
sys.exit(app.exec_())
