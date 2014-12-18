'''
Created on 10.12.2014

@author: user
'''
line= "#1054#1095#1080#1089#1090#1080#1090#1100"
line2=line.split("#")


for i in line2:
    
    if(i<>""): 
        c = unichr(int(i))
        print c,