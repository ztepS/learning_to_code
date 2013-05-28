'''
Created on 22.04.2013

@author: user
'''
#copy of array
import random
import time

itemsCount=40
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
    centralElement=array[int(len(array)/2)]
    l=0
    r=len(array)-1

    while(l<r):
        
       
        while(array[l]<centralElement):
            l+=1
        
        while(array[r]>centralElement):
            r-=1
        #if(l==centralElementN):centralElementN=r
        #if(r==centralElementN):centralElementN=l
        if(l<=r):
            print array,l,"<->",r,"|c =", centralElementN,"(",centralElement,")"
            ArraySwap(array,l,r)
            
        l+=1
        r-=1
    print "resulting ", array
    if(0<r): 
        array[0:r+1]=QuickSort(array[0:r+1])
    if(l<len(array)-1): 
        array[l-1:len(array)]=QuickSort(array[l-1:len(array)])
       
         
    return array           
    
    

for i in range(itemsCount):
    inputArray[i]=random.randrange(0,100)
     
print inputArray
#inputArray.sort()
print"========"



outputArray = QuickSort(inputArray)




print"========"
print outputArray

print time.time() - startTime
    