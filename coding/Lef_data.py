#!/usr/bin/env python 
# -*- coding: utf-8 -*-


import pyodbc
import sys


reload(sys)  
sys.setdefaultencoding('utf8')



def DeltaToSigma(delta):
    pi=3.14159265
      
    sigma=(float(delta)-180)*(pi/180)
    
    return sigma


processId="ionfab3014"

sqlQuery=u"SELECT PodlP.НпПодл FROM PodlP WHERE ((PodlP.НомПартии)='"+processId+"' ) ORDER BY PodlP.НпПодл;"

db = pyodbc.connect('DSN=zerki_local')
cursor = db.cursor()
cursor.execute(sqlQuery)
names=cursor.fetchall()
substratesCountDb=len(names)

print substratesCountDb

if(substratesCountDb>0):
    
    sqlQuery=(u"INSERT INTO Zerki ([нПодложки], [Тзер], [Рсферы], [Рсф_изм], [N], [ДельтаN], [Тнап]) "
              u"SELECT [НпПодл], [Тзер], [РсферыНом] , [РсферыИзм], [N], [ДельтаN], [ТипНап] "
              u"FROM PodlP "
              u"WHERE (((PodlP.НомПартии)='"+processId+"'));")

    print sqlQuery
    try: cursor.execute(sqlQuery)
    except pyodbc.IntegrityError: print "already present"
    db.commit()
phaseListDeg=[]


f = open(processId+".txt", 'r')
a = f.readlines()
for i in a:
    phaseListDeg.append(i.split(" ")[2]) 

print len(phaseListDeg)

phaseListRad=[]
for i in phaseListDeg:
    phaseListRad.append(DeltaToSigma(i))
    
    
counter=0
if(len(phaseListDeg)==substratesCountDb):
    for i in names:
        print i[0]
        sqlQuery=(u"Update Zerki "
                  u"SET [Сигма]="+str(phaseListRad[counter])+" "
                  u"WHERE Zerki.НПодложки='"+i[0]+"'")
        counter+=1
        print sqlQuery
        cursor.execute(sqlQuery)
    db.commit()
else: print "Number of records mismatch "   
