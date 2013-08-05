'''
Created on 22.04.2013

@author: user
'''
#copy of array
import random
import time

itemsCount=10000
def ArraySwap(array,a,b):
    array2=array
    c=array2[a]
    array2[a]=array2[b]
    array2[b]=c
    return array2
    
def CheckSorted(array):
    a=array[0]
    for i in range(1,len(array)):
        if(array[i]<a): return 0
        a=array[i]
    return 1

def BubbleSort(array):
    for i in range(len(array)-1):
        if (array[i] >array[i+1]): ArraySwap(array,i,i+1)
    if(CheckSorted(array)==0): BubbleSort(array)
    return array
startTime=time.time()
inputArray=range(itemsCount)
outputArray = range(itemsCount)


def QuickSort(array):
    print "starting", array
    centralElementN=int(len(array)/2)
    centralElement=array[centralElementN]
    l=0
    r=len(array)-1

    while(l<=r):
        
       
        #print "l = ",l ," r = ",r 
        while(array[l]<centralElement):
            l+=1
        
        while(array[r]>centralElement):
            r-=1

        if(l<=r):
            print array,l,"(",array[l],")<->",r,"(",array[r],")|c =", centralElementN,"(",centralElement,")"
            ArraySwap(array,l,r)
            #if(l==centralElementN):centralElementN=r
            #if(r==centralElementN):centralElementN=l
        l+=1
        r-=1
    print "resulting ", array
    
#    if(0<r): 
#        #print "Quicksort [0..",r+2,"]"
#        try:
#            array[0:r]=QuickSort(array[0:r])
#        except RuntimeError: print r
#    if(l<len(array)-1): 
#       # print "Quicksort [",l-1,"..",len(array)-1,"]"
#        array[l:len(array)]=QuickSort(array[l:len(array)])
#
#        
#         
    return array           
    
def qsort1(array):
    if array == []: 
        return []
    else:
        pivot = array[0]
        lesser = qsort1([x for x in array[1:] if x < pivot])
        greater = qsort1([x for x in array[1:] if x >= pivot])
        #print lesser, pivot, greater
        return lesser + [pivot] + greater

for i in range(itemsCount):
    inputArray[i]=random.randrange(0,100)
     
#print inputArray
#inputArray.sort()
print"Quick sort:"

outputArray = qsort1(inputArray)
if(CheckSorted(outputArray)==1): print"Sorted"
else: print"Not sorted"
print time.time() - startTime

for i in range(itemsCount):
    inputArray[i]=random.randrange(0,100)


print"Bubble:"

try: outputArray = BubbleSort(inputArray)
except RuntimeError: print "Error"
if(CheckSorted(outputArray)==1): print"Sorted"
else: print"Not sorted"
print time.time() - startTime



    