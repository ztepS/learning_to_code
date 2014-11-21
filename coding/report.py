#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import pyodbc
import os
import sys
import time
reload(sys)  
sys.setdefaultencoding('utf8')

def return_count(mType,mat,rad,podl):

    if(mType=="pz"): 
        mirrorType="пьезо"
        radius="Is Null"
    
    if(mType=="p"): 
        mirrorType="плоское"
        radius="Is Null"
    
    if(mType=="s"): 
        mirrorType="сфера"
        radius=u"= "+rad

    if(mat=="z"): material="='z'"
    if(mat=="si"): material="Is Null"
        
    #db = pyodbc.connect('DSN=test',connect_args={'convert_unicode': True})
    

    if(podl==0):
        db = pyodbc.connect('DSN=zerki_local')
        sqlQuery=u"SELECT Count(Zerki.[нПодложки]) AS count FROM Zerki WHERE (((Zerki.[Вкомп])='свободно') AND ((Zerki.[МесХран]) Is Not Null) AND ((Zerki.[Ячейка]) Is Not Null) AND ((Zerki.[Тзер])='"+mirrorType+"') AND ((Zerki.[Материал подл]) "+material+") AND ((Zerki.[ГОтказ])='годен') AND ((Zerki.[Рсферы]) "+radius+"));"
    else:
        db = pyodbc.connect('DSN=podl_local')
        sqlQuery=u"SELECT count(PODL.[нПодл]) AS count FROM PODL WHERE ((Not (PODL.[Завод])='оптик пента') AND ((PODL.[Воз])='свободно') AND ((PODL.[Тзер])='"+mirrorType+"') AND ((PODL.[№кор]) Is Not Null) AND ((PODL.[Место]) Is Not Null) AND ((PODL.[Материал]) "+material+") AND ((PODL.[РсферыНом])"+radius+"));"
    #print(sqlQuery)
    cursor=db.cursor()
    cursor.execute(sqlQuery)
   
    data=cursor.fetchall()
    return data[0][0]




radiusList=["2  ", "2.8", "3.6", "4.5", "5  ", "6  "]

def print_mat(mat,podl):

    if(mat=="si"):fileSi.write("Ситалл:\n")
    else:fileSi.write("Clearceram:\n")
    
    fileSi.write("плоских - ")    
    fileSi.write( str(return_count("p",mat,"",podl))+"\n")
    
    fileSi.write("пьезо - ")    
    fileSi.write( str(return_count("pz",mat,"",podl))+"\n")

    fileSi.write("сфер:\n")
    for i in radiusList:
        fileSi.write(i+" - " )   
        fileSi.write(str(return_count("s",mat,i,podl))+"\n")
    

fileSi=open("spravka.txt", 'w')

fileSi.write(time.strftime("%d/%m/%Y")+"\n\n")
fileSi.write("Подложек:\n\n")
print_mat("si",1)
fileSi.write("\n") 
print_mat("z",1)

fileSi.write("\n\n")
    
fileSi.write("Зеркал:\n\n")
print_mat("si",0)
fileSi.write("\n") 
print_mat("z",0)

#print return_count_podl("pz","si","")


#line1="Еженедельная справка по имеющимся в наличии оптическим деталям на 05.08.2014;;;;;;;;;;"
#fileSi.write(str(return_count("p","si","")))

fileSi.close()

os.system("start "+"spravka.txt")
