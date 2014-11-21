'''
Created on 19.11.2014

@author: user
'''

#1. round phase
#2. 
#todo:    
#        round phase
#        
#        store results and not operands
#        don't store results at all?
#        refactor to use numpy? use fixed size array
#        use integers?
#        is double search on pz needed?
#        defragmentation needs testing, when to start
#        store final piece in defrag



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

random.seed()

size=40
totalSize=(size**4)*4




timeStart=time.time()

searchType="K-5"  ## "EK-104" or"K-5" or "all"
    
if(searchType=="K-5"):
    minL0=0.14
    maxL0=0.16
elif(searchType=="EK-104"):
    maxL0=999
    minL0=0.20
elif(searchType=="all"):
    maxL0=999
    minL0=0
        
minDelta=-0.1
maxDelta=0.1

def store(data, number):
    file1="temp."+str(number)
    output = open(file1, 'wb')
    cPickle.dump(data, output)
    output.close()


def defragmentStorage():
    global pickles
    combinationStoredList=[]
    newPickle=1
    counter=0
    for j in range(pickles):
        
        file1="temp."+str(j+1)
        pkl_file = open(file1, 'rb')
        combinationStoredListOld=cPickle.load(pkl_file)
        
        for i in combinationStoredListOld:
            
            if(checkUsed(i)==0):
                combinationStoredList.append(i)
                counter+=1
                
                if(counter==1000000) :
                    store(combinationStoredList,newPickle)
                    newPickle+=1
                    combinationStoredList=[]
                    counter=0
            del(i)
        print counter
        pkl_file.close()
    store(combinationStoredList,newPickle)
    #newPickle+=1
    print "before ", pickles, "after ", newPickle
    pickles=newPickle
    
def CheckUsedMirror(mirrType, mirrId):

    
    if(mirrType==2 and typeFlat[mirrId][4]==1): return 1
    if(mirrType==3 and typeSphere[mirrId][4]==1): return 1
    if(mirrType==0  and typePiezo[mirrId][4]==1): return 1
    return 0    


def checkUsed(combination):
    #if (combination==0): return 1
    if (typePiezo[combination[0][2]][4]==1):return 1
    if (typePiezo[combination[1][2]][4]==1):return 1
    if (typeFlat[combination[2][2]][4]==1):return 1
    if (typeSphere[combination[3][2]][4]==1):return 1
    return 0

def makeUsed(combination):
    typePiezo[combination[0][2]][4]=1
    typePiezo[combination[1][2]][4]=1
    typeFlat[combination[2][2]][4]=1
    typeSphere[combination[3][2]][4]=1
    return 0



def combinationsSearch(combType, combId):
#    for i in combinationList:
#        if(i[combType][2]==combId and checkUsed(i)==0): 
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
            if(i[combType][2]==combId and checkUsed(i)==0): 
                return i
    pkl_file.close()
    print "none found"
    return 0
    

typeFlat=range(size)
for i in range(size):
    typeFlat[i]=range(3)
    typeFlat[i][0]=float(random.randrange(-110,110))/1000
    typeFlat[i][1]=float(random.randrange(9,16))/100
    typeFlat[i][2]=i
    

typePiezo=range(size*2)
for i in range(size*2):
    typePiezo[i]=range(3)
    typePiezo[i][0]=float(random.randrange(-110,110))/1000
    typePiezo[i][1]=float(random.randrange(1,4))/1000   #rethink
    typePiezo[i][2]=i
    


typeSphere=range(size)
for i in range(size):
    typeSphere[i]=range(3)
    typeSphere[i][0]=float(random.randrange(-110,110))/1000
    typeSphere[i][1]=float(random.randrange(1,4))/1000
    typeSphere[i][2]=i
    
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
for i in itertools.product(*[typePiezo,typePiezo,typeFlat,typeSphere]):
    delta=i[0][0]+i[1][0]+i[2][0]+i[3][0]
    L0=i[0][1]+i[1][1]+i[2][1]+i[3][1]
    if(abs(delta)<= maxDelta and L0>=minL0 and L0 <= maxL0 and i[0][2] <> i[1][2]):
        combinationList.append(i)
        counterGood+=1
    counter+=1
    
    if(counter==1000000):
        percent = float(counter)*(counterIterations+1)*100/totalSize
        print percent, "%  of phase 1"
        counterIterations+=1
        counter=0
        if(percent<>0): 
            secondCount = ((time.time()-timeIterStart)*100/percent - (time.time()-timeIterStart))  
            print str(datetime.timedelta(seconds=secondCount)), " eta of phase 1"


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

for i in typeFlat:
    i.append(0) #frequency
    i.append(0) #used
    
    
for i in typeSphere:
    i.append(0)
    i.append(0)
    
for i in typePiezo:
    i.append(0)
    i.append(0)
    




#for i in combinationList:
#    typeFlat[i[2][2]][3]+=1
#    typeSphere[i[3][2]][3]+=1
#    typePiezo[i[0][2]][3]+=1
#    typePiezo[i[1][2]][3]+=1
    
for j in range(pickles):
    file1="temp."+str(j+1)
    pkl_file = open(file1, 'rb')
    combinationStoredList = cPickle.load(pkl_file)
    for i in combinationStoredList:
        typeFlat[i[2][2]][3]+=1
        typeSphere[i[3][2]][3]+=1
        typePiezo[i[0][2]][3]+=1
        typePiezo[i[1][2]][3]+=1
pkl_file.close()
        
#    print typeFlat[i[2][2]]
    

#typeFlat.sort(cmp=None, key=lambda typeFlat: typeFlat[3], reverse=True)
#typeSphere.sort(cmp=None, key=lambda typeSphere: typeSphere[3], reverse=True)
#typePiezo.sort(cmp=None, key=lambda typePiezo: typePiezo[3], reverse=True)

flatCount=0
piezoCount=0
sphereCount=0

unitedFreqList=[]
result=[]
for i in typeFlat:
    if i[3]>0:
        result=[2,i[2],i[3]]
        unitedFreqList.append(result)
        flatCount+=1

for i in typeSphere:
    if i[3]>0:
        result=[3,i[2],i[3]]
        unitedFreqList.append(result)
        sphereCount+=1

for i in typePiezo:
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

for i in unitedFreqList:
    #print i
    found = 0
    
    if(CheckUsedMirror(i[0], i[1])==0 and combinationCount < maxPossibleCombinations): 
        
        result=combinationsSearch(i[0],i[1])
        #print result,">", i[1] ,"<"
        
        if(result<>0):
                  
            makeUsed(result)
            print(result)
            combinationCount+=1
            
            
#            if(defragCounter==10):
#                defragmentStorage()    
#                defragCounter=0
        else: defragmentStorage()

#print "flat:"
#for i in typeFlat:
#    print i
#
#print "piezo:"
#for i in typePiezo:
#    print i
#    
#print "sphere:"
#for i in typeSphere:
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


