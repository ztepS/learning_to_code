'''
Created on 19.06.2013

@author: user
'''
import sys
import pygame
#import time
import random
import pygame.gfxdraw as gfxdraw

pygame.init() 
random.seed()

class mob:
    def __init__(self,x,y,type1,side):
        self.side=side
        self.type=type1
        self.speed=3
        self.hp=100
        self.attack=10
        self.lane=2
        self.X = x
        self.Y = y
        self.currentTarget = 0
        if (self.side==1): self.color = (255,0,0) 
        else: self.color = (0,0,255) 
                  
    def draw(self):
        gfxdraw.aacircle(window, int(self.X), int(self.Y), 6, self.color)
        
    def move(self,x,y):
        self.X+=x
        self.Y+=y
    
    def find_target(self):
        ##doesn't work at all
        self.current_target = red_center.list[1]
        for i in red_center:
            if (sqrt(abs(self.currentTarget.X - i.X))+sqrt(abs(self.currentTarget.X - i.X))):self.currentTarget = i
        
    def movement(self):
        if(self.lane==2):self.move(self.X+self.speed/2,self.Y+self.speed/2)
        


class mob_spawner:
    def __init__(self,x,y,side):
        self.side=side
        self.X = x
        self.Y = y
        self.list=[]
        if (self.side==1): self.color = (255,0,0) 
        else: self.color = (0,0,255) 
        
    def spawn(self,type1):
        self.list.append(mob(self.X,self.Y,type1,self.side))
        
    def draw(self): 
        gfxdraw.aacircle(window, int(self.X), int(self.Y), 10, self.color)
        for i in self.list:
            i.movement()
            i.draw()
            
        
        
window = pygame.display.set_mode((640, 480)) 

blue_center = mob_spawner(50,430,0)
red_center = mob_spawner(590,50,1)


red_center.spawn(1)
red_center.draw()
blue_center.spawn(1)
blue_center.draw()

pygame.display.flip()

running = True

while running == True: 
        #pygame.display.flip()
        for event in pygame.event.get():   
            if event.type == pygame.QUIT: 
                sys.exit(0)