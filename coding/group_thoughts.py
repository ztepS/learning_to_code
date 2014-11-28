#!/usr/bin/env python 
# -*- coding: utf-8 -*-




#todo:    
#        
#        

#        refactor to use numpy? use fixed randomDataSize array
#        use integers?
#        is double search on pz needed?
#        defragmentation needs testing, when to start
#        selection algorythm is still bad



#     stupid array format:
#    mirror list
#    0  1  2  3  4
#    


import random
import itertools
import time
import datetime
import cPickle
import os
import pyodbc

random.seed()

typeSearch="real data"  #random numbers or real data

randomDataSize=50


timeStart=time.time()

#searchType="EK-104"  ## "EK-104" or"K-5" or "all"
    

#minL0K=0.14
#maxL0K=0.16
minL0K=0
maxL0K=0

maxL0E=999
minL0E=0.20
#elif(searchType=="all"):
#    maxL0E=999
#    minL0E=0


quotaDelta=0.001        #   0.11 default
minDelta=-quotaDelta
maxDelta=quotaDelta



def PrintResultList(resultList):
    for i in resultList:
        groupStr=""
        delta = piezoList[i[0]][0]+piezoList[i[1]][0] + flatList[i[2]][0] + sphereList[i[3]][0]
        L0 = piezoList[i[0]][1]+piezoList[i[1]][1] + flatList[i[2]][1] + sphereList[i[3]][1]

    
        groupStr+=str(piezoListFull[i[0]][0])+ "("+ str(piezoListFull[i[0]][4])+ "-"+ str(piezoListFull[i[0]][5])+ ") "
        groupStr+=str(piezoListFull[i[1]][0])+ "("+ str(piezoListFull[i[1]][4])+ "-"+ str(piezoListFull[i[1]][5])+ ") "
        groupStr+=str(flatListFull[i[2]][0])+ "("+ str(flatListFull[i[2]][4])+ "-"+ str(flatListFull[i[2]][5])+ ") "
        groupStr+=str(sphereListFull[i[3]][0])+ "(" + str(sphereListFull[i[3]][4])+ "-" + str(sphereListFull[i[3]][5])+ ") "
        groupStr+="L0 = "+ str(L0)+ " delta = "+ str(round(delta,3))+ "\n"
        file1.write(groupStr)
            
    
    
def PrintResultDataConsole(typeList):
    global resultListE, resultListK, flatListFull, piezoListFull, sphereListFull 
    if(typeList=="E"): resultInternal=resultListE
    elif(typeList=="K"):resultInternal=resultListK
    for i in resultInternal:
    
        if(typeSearch=="real data"): print  piezoListFull[i[0]]
        else: print piezoList[i[0]]
        if(typeSearch=="real data"): print  piezoListFull[i[1]]
        else: print piezoList[i[1]] 
        if(typeSearch=="real data"): print  flatListFull[i[2]]
        else: print flatList[i[2]]  
        if(typeSearch=="real data"): print  sphereListFull[i[3]]
        else: print sphereList[i[3]] 
 
        print "delta = ", piezoList[i[0]][0]+piezoList[i[1]][0] + flatList[i[2]][0] + sphereList[i[3]][0]   
        print "L0 = ", piezoList[i[0]][1]+piezoList[i[1]][1] + flatList[i[2]][1] + sphereList[i[3]][1]    
    



def GetRealData():
    
    global flatListFull, sphereListFull, piezoListFull
    
    db = pyodbc.connect('DSN=zerki_local')
    cursor=db.cursor()
    
    #cursor.execute(u"SELECT DISTINCTROW zerki.нПодложки, zerki.Тзер, zerki.Сигма, zerki.L0, zerki.МесХран, zerki.Ячейка, zerki.Рсферы FROM zerki WHERE (((zerki.[Материал подл]) Is Null) AND ((zerki.ГОтказ)='Годен') AND ((zerki.Вкомп)='Свободно') AND ((zerki.НранВоз) Is Null));")

    cursor.execute(u"SELECT DISTINCTROW zerki.нПодложки, zerki.Тзер, zerki.Сигма, zerki.L0, zerki.МесХран, zerki.Ячейка, zerki.Рсферы, zerki.[Годен для Тамбова], zerki.MaxS FROM zerki WHERE (((zerki.[Материал подл]) Is Null) AND ((zerki.ГОтказ)='Годен') AND ((zerki.Вкомп)='Свободно') AND ((zerki.НранВоз) Is Null))  ;")
    #AND zerki.[Годен для Тамбова] <>'тт'
    data=cursor.fetchall()
    
    
    global flatListFull
    global piezoListFull
    global sphereListFull
    global flatList
    global sphereList
    global piezoList
    global totalSize
    
    
    flatListFull=[]
    piezoListFull=[]
    sphereListFull=[]
    flatList=[]
    sphereList=[]
    piezoList=[]
    
    
    
    
    flatCount=0
    piezoCount=0
    sphereCount=0
    for i in range(len(data)):
        #print type(data[i][3])
        if(data[i][3] is None): 
            data[i][3]=999
            print "Empty L0"
        if(data[i][2] is None): 
            data[i][2]=999
            print "Empty delta"
        if(data[i][1] == u"Плоское"): 
            flatCount+=1
            flatListFull.append([data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], flatCount-1])
        
        if(data[i][1] == u"Пьезо"): 
            piezoCount+=1
            piezoListFull.append([data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], piezoCount-1])
        
        if(data[i][1] == u"Сфера" and (abs(data[i][6] - 3.6))<0.1): 
            sphereCount+=1
            sphereListFull.append([data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], sphereCount-1])
    
    #print flatListFull[1]
    for i in flatListFull: flatList.append([round(i[2], 3),i[3],i[6]])
    for i in sphereListFull: sphereList.append([round(i[2], 3),i[3],i[6]])
    for i in piezoListFull: piezoList.append([round(i[2], 3),i[3],i[6]])
    totalSize=(len(piezoList)*len(piezoList)*len(sphereList)*len(flatList))
    print len(piezoList), len(sphereList), len(flatList)
    

def Store(data, number):
    file1="temp."+str(number)
    output = open(file1, 'wb')
    cPickle.dump(data, output)
    output.close()


def DefragmentStorage():
    global pickles
    combinationStoredList=[]
    newPickle=1
    counter=0
    for j in range(pickles):
        
        file1="temp."+str(j+1)
        pkl_file = open(file1, 'rb')
        combinationStoredListOld=cPickle.load(pkl_file)
        
        for i in combinationStoredListOld:
            
            if(CheckUsed(i)==0):
                combinationStoredList.append(i)
                counter+=1
                
                if(counter==1000000) :
                    Store(combinationStoredList,newPickle)
                    newPickle+=1
                    combinationStoredList=[]
                    counter=0
            del(i)
        print counter
        pkl_file.close()
    Store(combinationStoredList,newPickle)
    #newPickle+=1
    print "before ", pickles, "after ", newPickle
    pickles=newPickle
    
def CheckUsedMirror(mirrType, mirrId):

    
    if(mirrType==2 and flatList[mirrId][4]==1): return 1
    if(mirrType==3 and sphereList[mirrId][4]==1): return 1
    if(mirrType==0  and piezoList[mirrId][4]==1): return 1
    return 0    


def CheckUsed(combination):
    #if (combination==0): return 1
    if (piezoList[combination[0]][4]==1):return 1
    if (piezoList[combination[1]][4]==1):return 1
    if (flatList[combination[2]][4]==1):return 1
    if (sphereList[combination[3]][4]==1):return 1
    return 0

def MakeUsed(combination):
    piezoList[combination[0]][4]=1
    piezoList[combination[1]][4]=1
    flatList[combination[2]][4]=1
    sphereList[combination[3]][4]=1
    return 0



def CombinationsSearch(combType, combId):
#    for i in combinationList:
#        if(i[combType][2]==combId and CheckUsed(i)==0): 
#            return i
        #else: print combType, i[combType][2],  combId
#        if(combType==0):
#            if(i[1][2]==combId):
#                return i
#pickle here
    for j in range(pickles):
        file1="temp."+str(j+1)
        pkl_file = open(file1, 'rb')
        combinationStoredList = cPickle.load(pkl_file)
        for i in combinationStoredList:
            if(i[combType]==combId and CheckUsed(i)==0): 
                return i
    pkl_file.close()
    print "none found"
    return 0
    
if(typeSearch=="random numbers"):
    flatList = range(randomDataSize)
    for i in range(randomDataSize):
        flatList[i] = range(3)
        flatList[i][0] = float(random.randrange(-110, 110)) / 1000
        flatList[i][1] = float(random.randrange(9, 16)) / 100
        flatList[i][2] = i
    

    piezoList = range(randomDataSize * 2)
    for i in range(randomDataSize * 2):
        piezoList[i] = range(3)
        piezoList[i][0] = float(random.randrange(-110, 110)) / 1000
        piezoList[i][1] = float(random.randrange(1, 4)) / 1000  # rethink
        piezoList[i][2] = i
    


    sphereList = range(randomDataSize)
    for i in range(randomDataSize):
        sphereList[i] = range(3)
        sphereList[i][0] = float(random.randrange(-110, 110)) / 1000
        sphereList[i][1] = float(random.randrange(1, 4)) / 1000
        sphereList[i][2] = i
    totalSize=(randomDataSize**4)*4

else: GetRealData() 

    
#loop 1
  
  
delta=0
L0=0
combinationList=[]
goodList=[]
percent = 0.0
counter=0
pickles=0
counterGood=0
counterIterations=0
counterFile=0

timeIterStart=time.time() 
for i in itertools.product(*[piezoList,piezoList,flatList,sphereList]):
    delta=i[0][0]+i[1][0]+i[2][0]+i[3][0]
    try: L0=i[0][1]+i[1][1]+i[2][1]+i[3][1]
    except TypeError: L0=0
    if(abs(delta)<= maxDelta and ((L0>=minL0K and L0 <= maxL0K) or (L0>=minL0E and L0 <= maxL0E)) and i[0][2] <> i[1][2]):
        combinationList.append([i[0][2],i[1][2],i[2][2],i[3][2]])
        counterGood+=1
    counter+=1
    
    if(counter==1000000):
        percent = float(counter)*(counterIterations+1)*100/totalSize
        print percent, "%  of phase 1"
        counterIterations+=1
        counter=0
        if(percent<>0): 
            secondCount = ((time.time()-timeIterStart)*100/percent - (time.time()-timeIterStart))  
            print str(datetime.timedelta(seconds=secondCount)), " eta"


    if(counterGood==1000000):  
        counterFile+=1 
        file1="temp."+str(counterFile)
        output = open(file1, 'wb')
        cPickle.dump(combinationList, output)
        output.close()
        combinationList=[]
        pickles+=1
        
        counterGood=0
        print "used up to ", counterFile*33.152, "Mb"

totalSize = len(combinationList)+pickles*1000000
pickles+=1
file1="temp."+str(pickles)
output = open(file1, 'wb')
cPickle.dump(combinationList, output)
output.close()

picklesMaximum = pickles

#   rewrite? code repetition

for i in flatList:
    i.append(0) #frequency
    i.append(0) #used
    
    
for i in sphereList:
    i.append(0)
    i.append(0)
    
for i in piezoList:
    i.append(0)
    i.append(0)
    




#for i in combinationList:
#    flatList[i[2][2]][3]+=1
#    sphereList[i[3][2]][3]+=1
#    piezoList[i[0][2]][3]+=1
#    piezoList[i[1][2]][3]+=1
    
    
    
    
for j in range(pickles):
    file1="temp."+str(j+1)
    pkl_file = open(file1, 'rb')
    print j+1, " out of", pickles, " to complete phase 2"
    combinationStoredList = cPickle.load(pkl_file)
    for i in combinationStoredList:
        flatList[i[2]][3]+=1
        sphereList[i[3]][3]+=1
        piezoList[i[0]][3]+=1
        piezoList[i[1]][3]+=1
        
          
pkl_file.close()
        
#    print flatList[i[2][2]]
    

#flatList.sort(cmp=None, key=lambda flatList: flatList[3], reverse=True)
#sphereList.sort(cmp=None, key=lambda sphereList: sphereList[3], reverse=True)
#piezoList.sort(cmp=None, key=lambda piezoList: piezoList[3], reverse=True)

flatCount=0
piezoCount=0
sphereCount=0

unitedFreqList=[]
result=[]
for i in flatList:
    if i[3]>0:
        result=[2,i[2],i[3]]
        unitedFreqList.append(result)
        flatCount+=1

for i in sphereList:
    if i[3]>0:
        result=[3,i[2],i[3]]
        unitedFreqList.append(result)
        sphereCount+=1

for i in piezoList:
    if i[3]>0:
        result=[0,i[2],i[3]]
        unitedFreqList.append(result)
        piezoCount+=1

unitedFreqList.sort(cmp=None, key=lambda unitedFreqList: unitedFreqList[2], reverse=False)

maxPossibleCombinations=min(flatCount, piezoCount, sphereCount)
print maxPossibleCombinations


#   needs big rethinking


combinationCount=0
result=[]
defragCounter=0
resultListE=[]
resultListK=[]

for i in unitedFreqList:
    #print i
    found = 0
    
    if(CheckUsedMirror(i[0], i[1])==0 and combinationCount < maxPossibleCombinations): 
        
        result=CombinationsSearch(i[0],i[1])
        #print result,">", i[1] ,"<"
        
        if(result<>0):
                  
            MakeUsed(result)
            print(result)
            delta = piezoList[result[0]][0]+piezoList[result[1]][0] + flatList[result[2]][0] + sphereList[result[3]][0]
            L0=piezoList[result[0]][1]+piezoList[result[1]][1] + flatList[result[2]][1] + sphereList[result[3]][1]
            
            if(L0<maxL0E and L0>minL0E): resultListE.append(result)
            if(L0<maxL0K and L0>minL0K): resultListK.append(result)
            combinationCount+=1
            
            defragCounter+=1
            if(defragCounter>(maxPossibleCombinations/8)):
                DefragmentStorage()    
                defragCounter=0
                
                
                
                
#for i in resultList:
#    
#    if(typeSearch=="real data"): print  piezoListFull[i[0]]
#    else: print piezoList[i[0]]
#    if(typeSearch=="real data"): print  piezoListFull[i[1]]
#    else: print piezoList[i[1]] 
#    if(typeSearch=="real data"): print  flatListFull[i[2]]
#    else: print flatList[i[2]]  
#    if(typeSearch=="real data"): print  sphereListFull[i[3]]
#    else: print sphereList[i[3]] 
# 
#    print "delta = ", piezoList[i[0]][0]+piezoList[i[1]][0] + flatList[i[2]][0] + sphereList[i[3]][0]   
#    try: print "L0 = ", piezoList[i[0]][1]+piezoList[i[1]][1] + flatList[i[2]][1] + sphereList[i[3]][1]    
#    except(TypeError): print "faulty L0 data"
                
print len(resultListE), len(resultListK)
        
#PrintResultDataConsole("E")
#PrintResultDataConsole("K")        

groupStr=""

file1=open("group.txt", 'w')
file1.write("K-5:\n")
PrintResultList(resultListK)
file1.write("\nЭK-104:\n")
PrintResultList(resultListE)
file1.close()
os.system("start "+"group.txt")
        #else: DefragmentStorage()

#print "flat:"
#for i in flatList:
#    print i
#
#print "piezo:"
#for i in piezoList:
#    print i
#    
#print "sphere:"
#for i in sphereList:
#    print i





#          cleanup
for i in range(picklesMaximum):
    file1="temp."+str(i+1)
    os.remove(file1)


print (time.time()-timeStart)/60, " min."










#timeIterStart=time.time()
#for j in range(counterIterations):
#    percent = float(j)*100/counterIterations
#    for i in combinationList:
#        delta=i[0][0]+i[1][0]+i[2][0]+i[3][0]
#
#        L0=i[0][1]+i[1][1]+i[2][1]+i[3][1]
#        if(abs(delta)<= maxDelta and L0>=minL0 and L0 <= maxL0 and i[0][2] <> i[1][2]):
#            goodList.append(i)
#        del i
#    file1="temp."+str(j+1)
#    pkl_file = open(file1, 'rb')
    
#    combinationList = cPickle.load(pkl_file)
#    if(percent<>0): 
#        secondCount = ((time.time()-timeIterStart)*100/percent - (time.time()-timeIterStart))  
#        print str(datetime.timedelta(seconds=secondCount)), " eta of phase 2"
#    pkl_file.close()
#    os.remove(file1)



#print len(goodList)


