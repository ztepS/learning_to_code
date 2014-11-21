'''
Created on 11.08.2014

@author: user
'''
import pygame
import sys
import pygame.gfxdraw as gfxdraw
import math

windowX=480
windowY=640

pygame.init() 

window = pygame.display.set_mode((windowX, windowY)) 



collisionArray=range(windowX)
simpleCollision=range(windowX)
for i in range(windowX):
    collisionArray[i]=range(windowY)
    simpleCollision[i]=range(windowY)
    
    

def collision_initialize():
    for i in range(windowX):
        for j in range(windowY):
            collisionArray[i][j]=0
            simpleCollision[i][j]=0

class Bubble:
    def __init__(self,x,y,size):
        self.x=x
        self.y=y
        self.size=size
        
    def drawSimpleCircle(self):
        gfxdraw.aacircle(window, self.x,self.y,self.size, (255,255,255))
        
        
    def putCollision(self):
        
        #screen borders go here
        
        for i in range(self.x-self.size, self.x+self.size):
            for j in range(self.y-self.size, self.y+self.size):
                distance = abs(math.sqrt((i-self.x)**2+(j-self.y)**2))
                if(distance<=self.size):
                    if(simpleCollision[i][j]<2):collisionArray[i][j]+=(self.size-distance)
                    else:collisionArray[i][j]-=(self.size-distance)
                    if(collisionArray[i][j]<0):collisionArray[i][j]=0
                    
    def findCollision(self):
        for i in range(self.x-self.size, self.x+self.size):
            for j in range(self.y-self.size, self.y+self.size):
                distance = abs(math.sqrt((i-self.x)**2+(j-self.y)**2))
                if(distance<=self.size):
                    simpleCollision[i][j]+=1
                       
 
collision_initialize()

#bubbleA=Bubble(200,200,35)
#bubbleB=Bubble(240,240,35)
#bubbleC=Bubble(180,240,35)

bubbleList=[]


def process():
    
#    for i in bubbleList:
#        i.findCollision()
    
    for i in bubbleList:
        i.putCollision()
   




    for i in range(windowX):
        for j in range(windowY):
            gfxdraw.pixel(window,i,j,(int(collisionArray[i][j])*7,0,0))
            if(collisionArray[i][j]-3<3 and collisionArray[i][j]-3 >0):gfxdraw.pixel(window,i,j,(255,255,255))

#bubbleA.drawSimpleCircle()
#bubbleB.drawSimpleCircle()

    pygame.display.flip()
    collision_initialize()

running = True
while running == True: 
    for event in pygame.event.get():   
        if event.type == pygame.QUIT: 
            sys.exit(0) 
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            bubbleList.append(Bubble(pos[0],pos[1],35))
            process()
            
                
            