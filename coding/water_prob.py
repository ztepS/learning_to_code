'''
Created on 31.10.2013

@author: user
'''
import random


size=30


zone=range(size)
for i in range(size):
    zone[i]=range(size)
    zone[i][0] = random.randrange(1, size-1)
    for j in range(1,size):
        if(j<=zone[i][0]): zone[i][j]="#"
        else : zone[i][j]="W"

height=0
heightR=0
for i in range(size):
    if(height<zone[i][0]):height=zone[i][0]
    for j in range(height+1,size):
        if(zone[i][j]=="W"):zone[i][j]=" "
        
    if(heightR<zone[size-1-i][0]):heightR=zone[size-1-i][0]
    for j in range(heightR+1,size):
        if(zone[size-1-i][j]=="W"):zone[size-1-i][j]=" "

for i in range(size):
    print zone[i]
    