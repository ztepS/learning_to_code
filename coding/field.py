'''
Created on 27.05.2013

@author: user
'''

import pygame
import sys
import math
import random
random.seed()

class arrow:
    def __init__(self,X,Y):
        self.rotation = random.randrange(0, 359)
        self.X = X
        self.Y = Y
        self.strength = random.randrange(0, 10)*0.1
       
        ##self.rad = 10
    
    def draw(self,color):
        #pygame.draw.line(window,(color,color,color),((self.X+5),(self.Y+5)),((self.X+5)+math.cos(self.rotation*3.14/180)*5,(self.Y+5)+math.sin(self.rotation*3.14/180)*5))
        if(self.strength>0):
            pygame.draw.line(window,(color,color,color),((self.X+5),(self.Y+5)),((self.X+5)+math.cos(self.rotation*3.14/180)*self.strength*50,(self.Y+5)+math.sin(self.rotation*3.14/180)*self.strength*50))
        #print pygame.draw.circle(window,(255, 255, 255),(self.X+5,self.Y+5),5)
        
    def rotate(self,angle,strength):
        if(abs(self.rotation+90-angle)<abs(self.rotation-90-angle)):self.rotation +=strength*abs(self.rotation-angle)
        else:self.rotation -=strength*abs(self.rotation-angle)
        self.strength*=1-(self.strength-strength)*strength*0.1
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
    
        self.previous_list=range(x_count)
        for i in range(x_count):
            self.previous_list[i]=range(y_count)
    
    def process_fields(self):
        
        #pygame.draw.rect(window, (0, 0, 0), (0, 0, xCount*10, yCount*10))
        for i in range(self.x_count):
            for j in range(self.y_count):
                #print self.arrow_list[i][j].rotation
                self.previous_list[i][j]=self.arrow_list[i][j].rotation

        for i in self.arrow_list:
            for j in i:
                #print j.X
                #summ=0
                j.draw(0)
                if(j.X/10+1<=self.x_count-1):j.rotate(self.previous_list[j.X/10+1][j.Y/10], self.arrow_list[j.X/10+1][j.Y/10].strength)
                if(j.Y/10+1<=self.y_count-1):j.rotate(self.previous_list[j.X/10][j.Y/10+1], self.arrow_list[j.X/10][j.Y/10+1].strength)
                if(j.Y/10-1>=0):j.rotate(self.previous_list[j.X/10][j.Y/10-1], self.arrow_list[j.X/10][j.Y/10-1].strength)
                if(j.X/10-1>=0):j.rotate(self.previous_list[j.X/10-1][j.Y/10], self.arrow_list[j.X/10-1][j.Y/10].strength)
                
                j.draw(255)
                pygame.display.flip()
                #print summ
    
    def print_rotation(self):
        for i in range(xCount):
            for j in range(yCount):
                print self.arrow_list[i][j].rotation,
            print ""
        

xCount=40
yCount=30            
test = field(xCount,yCount)


    
pygame.init() 
window = pygame.display.set_mode((xCount*10,yCount*10))    
    
#test.arrow_list[0][0].rotation = 90
#test.arrow_list[4][9].rotation = 270

test.process_fields()
    #test.print_rotation()    

processing=False
    
running = True
while running == True: 
    if(processing==True):test.process_fields()
    for event in pygame.event.get():   
        if event.type == pygame.QUIT: 
            sys.exit(0) 
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_q]:test.process_fields()
            elif key[pygame.K_w]: 
                if(processing==True):
                    processing=False 
                else: processing = True
                       
        