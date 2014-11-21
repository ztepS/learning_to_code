'''
Created on 26.05.2014

@author: user
'''
import itertools
a = [[[1,2],2,3],[4,[5,5],6],[7,8,9,10]]
print a
for i in itertools.product(*a):
    print i