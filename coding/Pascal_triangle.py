'''
Created on 13.11.2013

@author: user
'''
size=20

triangle = range(size*2+1)
for i in range(size*2+1):
    triangle[i]=range(size)
    for j in range(size):
        triangle[i][j]=" "
        
        
triangle[size][0]=1        



def process_row(row_num):
    if(row_num==0):triangle[size][0]=1
    else:
        for i in range(size*2+1):
            if(triangle[i][row_num-1]<>" "):
                if(triangle[i-1][row_num]<>" "):triangle[i-1][row_num]+=triangle[i][row_num-1]
                else: triangle[i-1][row_num]=triangle[i][row_num-1]
                if(triangle[i+1][row_num]<>" "):triangle[i+1][row_num]+=triangle[i][row_num-1]
                else:triangle[i+1][row_num]=triangle[i][row_num-1]

space=1
for j in range(size):        
    process_row(j)
    for i in range(size*2+1):
        if len(str(triangle[i][j]))>space: space = len(str(triangle[i][j]))
        
        
for j in range(size):
    for i in range(size*2+1):
        if(triangle[i][j]==" "):
            for i in range(int(space)/2): print(" "),
        else:print triangle[i][j],
    print "\n"
    
