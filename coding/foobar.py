'''
Created on 18.03.2013

@author: user
'''



class num:
    def __init__(self,A):
        self.A = A
        i = 0        
        j = 0
        while j < 1:
            if(self.A/(10 ** i) < 10):
                j = j + 1 
            i = i+1
        countA = i-1

        Alist = range(countA+1)
        Alist[0] = self.A/(10**(countA))
        for i in range(1,countA+1):
            A0 = 0
            for j in range(i):
                A0=A0+(Alist[j]*10**(countA-j))

                Alist[i] = (self.A-A0)/(10**(countA-i))
       
        self.list = Alist
        self.count = countA
       

A = num(12345)
B = num(178967862798564693789789748978965)
j=0
for i in range (B.count+1):
    try:
        if A.list[j] == B.list[i]:
            j=j+1
    except IndexError:
        errcount=1
#print "j=", j
if j > A.count:
    print "yes"
else:
    print "no"

#print A.list, B.list, A.count, B.count

#for k in range (1,count+1):
#    for i in range (count+2-k):
#        Bnp=0
#        Bnm=0
#        for j in range (i):
#            Bnp = Bnp + Blist[j]*10**(count-j-k)
#        for j in range (i+k,count+1):
#            Bnm = Bnm + Blist[j]*10**(count-j)
#        Bn = Bnp + Bnm
#        #print Bn
#        
#mask=range(count+1)
#for i in range(count+1):
#    mask[i]=0
#
#for i in range(2**(count)):
#    j=0
#    while j < count:
#        if(mask[j]==0):
#            mask[j]=1
#        else:
#            mask[j]=0
#            mask[j+1]=1
#            j=count
#        j=j+1
#        #print mask
#mask = [0,1,1,0,1]
#Bm=0
#count=0
#for i in range(len(mask)-1):
#    #print len(mask)-i
#    if (mask[len(mask)-i-1]==1): 
#        count=count+1 
#        Bm=Bm+Blist[len(mask)-i-1]*10**(count-1)
#print "Bm=", Bm

