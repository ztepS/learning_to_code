'''
Created on 05.08.2013

@author: user
'''
import urllib2
import time
import json

finalUrl='http://maps.googleapis.com/maps/api/directions/json?origin=55.592554,37.663670&destination=55.653036,37.652340&sensor=false&departure_time='+str(int(time.time()))+'&mode=transit'
#print finalUrl
response = urllib2.urlopen(finalUrl)
#html = response.read()

#print html
parsed=json.load(response)
print parsed["routes"][0]["legs"][0]["duration"]['text']
