'''
Created on 12.09.2013

@author: user
'''
f=[0]



control="+.>+.>>>+++++ +++++\
[<<<[->>+<<]>>[-<+<+>>]<<<[->+<]>>[-<<+>>]<.>>>-]"

def brf_parser(str_code,f):
    
    position = 0
    i = 0   
    #for i in range(len(str_code)):
    while i < len(str_code):
        symbol=control[i]
        #print f[0], position
        if(symbol=="+"):f[position]+=1
        if(symbol=="-"):f[position]-=1
        if(symbol==">"):
            if(position==len(f)-1):f.append(0)
            position+=1
        if(symbol=="<"):
            if(position>0):position-=1
        if(symbol=="."):print chr(f[position]),
        if(symbol==","): f[position] = int(input('Input: ')  )
        if(symbol=="[" and f[position]==0): 
            while control[i]<>"]":
                i+=1
            
            
        if(symbol=="]" and f[position]<>0): 
            while control[i]<>"[":
                i-=1
            i-=1
        #print i ,position, f
        i+=1       
            #if(f[temp_pos<>0]):brf_parser(control[position:temp_pos])
    
    
brf_parser(control, f)
print f