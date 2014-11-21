'''
Created on 25.12.2013

@author: user
'''

def is_operator(symbol):
    operatorList=["+","*","-","/"]
    for i in range(len(operatorList)):
        if (symbol==operatorList[i]):return 1
    return 0
    

class Operator:
    def __init__(self,symbol):
        self.type=symbol
        self.left=0
        self.right=0
        if(self.type=="+" or self.type=="-"): self.priority=2
        if(self.type=="*" or self.type=="/"): self.priority=1
        
    def __repr__(self):   
        return "("+ str(self.left) + " " + self.type + " " + str(self.right) + ")"
#    def __str__(self):
#        return self.type
    
    def count(self):
        if (self.left.__class__==Operator):self.left = self.left.count()
        if (self.right.__class__==Operator):self.right = self.right.count()
        if (self.type=="+") : return (self.left + self.right)
        if (self.type=="-") : return (self.left - self.right)
        if (self.type=="*") : return (self.left * self.right)
        if (self.type=="/") : return (self.left / self.right)
        
        
syntaxList=[]

print -890*2451*96-8/66
text="-890*2451*96-8/66"
#print len(text)
i=0

while(i<len(text)):
    current_number=0
    while(i<len(text) and is_operator(text[i])==0):
        current_number*=10
        current_number+=int(text[i])
        i+=1
    syntaxList.append (current_number)
    if(i<len(text)):syntaxList.append(Operator(text[i])) 
    i+=1

if (syntaxList[len(syntaxList)-1].__class__==Operator):syntaxList.append(0)
print syntaxList

operatorCount=(len(syntaxList)-1)/2
print operatorCount

for i in range(operatorCount):
    highestOperator=0
    highestPriority=99
    for i in range(len(syntaxList)):
        if (syntaxList[i].__class__==Operator):
            if(highestPriority>syntaxList[i].priority):
                highestPriority=syntaxList[i].priority
                highestOperator=i
                
    syntaxList[highestOperator].left=syntaxList[highestOperator-1]
    syntaxList[highestOperator].right=syntaxList[highestOperator+1]
    syntaxList[highestOperator].priority=99
    del syntaxList[highestOperator+1]
    del syntaxList[highestOperator-1]
    
    print syntaxList

print syntaxList[0].count()
