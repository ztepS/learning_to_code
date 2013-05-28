'''
Created on 27.05.2013

@author: user
'''
class arrow:
    def __init__(self,X,Y):
        self.rotation = 0
        self.X = X
        self.Y = Y
        self.strength = 1
        ##self.rad = 10
    
    def rotate(self,angle):
        self.rotation +=angle
        while(self.rotation<0):self.rotation+=360
        while(self.rotation>359):self.rotation-=360

class field:
    def __init__(self,x_count,y_count):
        self.x_count = x_count
        self.y_count = y_count
        self.arrow_list=range(x_count)
        for i in range(x_count):
            self.arrow_list[i]=range(y_count)
        for i in range(x_count):
            for j in range(y_count):
                self.arrow_list[i][j]=arrow(i*10,j*10)
    
    def process_fields(self):
        for i in self.arrow_list:
            for j in i:
                #print j.X
                summ=0
                if(j.X/10+1<=self.x_count):summ+=self.arrow_list[j.X/10+1][j.Y/10].rotation
                #if(j.Y/10+1<=self.y_count):summ+=self.arrow_list[j.X/10][j.Y/10+1].rotation
                if(j.Y/10-1>=0):summ+=self.arrow_list[j.X/10][j.Y/10-1].rotation
        
#testtesttest

xCount=5
yCount=10            
test = field(xCount,yCount)

test.process_fields()

for i in range(xCount):
    for j in range(yCount):
        print test.arrow_list[i][j].rotation,
    print ""
        