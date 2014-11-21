#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
#f = codecs.open('word_rus.txt', encoding='cyrillic')
#for line in f:
#    print line.decode('iso8859_5')

f = open("word_rus.txt", 'r')
a = f.readlines()
dictionary = []
for i in a:
    dictionary.append(i.decode("cp1251"))
dictionary = sorted(dictionary)
print len(dictionary)
#print dictionary[5]
inputChar = raw_input("Enter something: ")
print inputChar
for i in range(len(inputChar)-1):
    dictNumber=0
    for j in range(len(dictionary)-1):
        try: 
            if( len(dictionary[j]) < (i-1) or inputChar[i]<>dictionary[j][i]): dictionary.remove(dictionary[j])
        except IndexError : print i, j    
            
print dictionary[1]
            
  