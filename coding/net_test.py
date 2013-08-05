'''
Created on 05.08.2013

@author: user
'''
import urllib2
import cStringIO
from PIL import Image
import time
import json

originX=37.663670
originY=55.592554
originCoords = str(originY)+','+str(originX)

def ParseTime(time):
    time=time.split(" ")
    
    if(len(time)==4):
        timeNum=float(time[0])+float(time[2])/60
    if(len(time)==2):
        timeNum=float(time[0])/60
    return timeNum
    
def GetTime(startX,startY,endX,endY):
    originCoords = str(startY)+','+str(startX)
    destinationCoords = str(endY)+','+str(endX)
    finalUrl='http://maps.googleapis.com/maps/api/directions/json?origin='+originCoords+'&destination='+destinationCoords+'&sensor=false&departure_time='+str(int(time.time()))+'&mode=transit'
    response = urllib2.urlopen(finalUrl)
    parsed=json.load(response)
    
    if(parsed['status']<>"ZERO_RESULTS"):
        #print parsed["routes"][0]["legs"][0]["duration"]['text']," | ",
        duration = ParseTime(parsed["routes"][0]["legs"][0]["duration"]['text'])
        print parsed['status']
        return duration
    else: return -1
#destinationX=37.652340
#destinationY=55.653036
#destinationCoords = str(destinationY)+','+str(destinationX)

result = range(10)
for i in range(10):result[i]=range(10)

markerString=""#"&markers=color:blue%7Clabel:C%7C55.592554,37.663670"

for i in range(-3,3):
    for j in range(-3,3):
        destinationX=originX+0.02*i
        destinationY=originY+0.02*j
        
        #print destinationY, destinationX
        result[i][j]=GetTime(originX,originY,destinationX,destinationY)
        time.sleep(3)
        #color:"+color+"%7C"
        if(abs(result[i][j]-0.8)<0.05):
            markerString+="&markers="+str(destinationY)+","+str(destinationX)
            #print result[i][j]
        
    print i
print markerString
print result
#print GetTime(37.663670,55.592554,37.663670,55.592554)

#ParseTime("1 hour 25 mins")


imageString="http://maps.googleapis.com/maps/api/staticmap?center=55.592554,37.663670&zoom=12&size=640x640&maptype=roadmap"+markerString+"&sensor=false"

pic = cStringIO.StringIO(urllib2.urlopen(imageString).read())
img = Image.open(pic)
img.show()