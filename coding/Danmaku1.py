'''
Created on 11.04.2013

@author: user
'''
import sys
import pygame
import math
import time
import random
import pygame.gfxdraw as gfxdraw
pygame.init() 
random.seed()


class spawner_list:
    def __init__(self):
        self.list=[]
        self.type=1
        if(self.type==1):
            self.pattern1()
    
    def create_spawner(self,X,Y):
        self.list.append(bullet_spawner(X,Y))
    
    def process_spawners_bullet_movement(self):
        for i in self.list:
            i.process_movement()
            i.drawSimpleCircle()
            
    def process_spawners_movement(self):
        if(self.type==1):
            self.pattern1_move()
        
    def move_spawner(self,sp_id,X,Y):
        self.playerBulletList[sp_id].globalX+=X
        self.playerBulletList[sp_id].globalY+=Y
        if (check_borders(self.playerBulletList[sp_id].globalX,self.playerBulletList[sp_id].globalY)==1) and (self.playerBulletList[sp_id].Bullet_list==[]):
            del self.list[sp_id]
            #print self.playerBulletList, sp_id
            
    def pattern1(self):
        self.create_spawner(100, 100)
        self.create_spawner(380, 540)
        self.create_spawner(100, 540)
        self.create_spawner(380, 100)
    
    def pattern1_move(self):
        self.move_spawner(0, 0.1, 0.1)
        
class bullet_spawner:
    def __init__(self,X,Y):
        self.globalX=X
        self.globalY=Y
        self.bullet_count = 0
        self.phase = 0
        self.Bullet_list=[]
        self.spawn()
    
        
        
    def drawSimpleCircle(self):
        #pygame.drawSimpleCircle.rect(window, (0, 0, 0), (0, 0, screen_borderX, screen_borderY))
        pygame.drawSimpleCircle.circle(window,(255, 255, 255),(int(self.globalX),int(self.globalY)),5)
        for i in self.Bullet_list:
            
            i.drawSimpleCircle()
                
        
    def spawn(self):
        #self.spawncount = 100
        
        self.spawning = True
        #for i in range(self.spawncount):
        self.phase += 0.5
        self.Bullet_list.append(Bullet(int(self.globalX),int(self.globalY),math.sin(self.phase)*1,math.cos(self.phase)*1)   ) 
        #print self.Bullet_list
        
    def process_movement(self):
        for i in self.Bullet_list:
            i.move()
            if (check_borders(i.globalX,i.globalY)==1): 
                self.Bullet_list.remove(i)
                
class Bullet:
    def __init__(self,X,Y,speedX,speedY):
        #self.bulletid=bulletid
        self.globalX = X
        self.globalY = Y
        self.speedX=speedX
        self.speedY=speedY
        #self.framespeed=1/30
        self.color=(random.randrange(0, 256),random.randrange(0, 256),random.randrange(0, 256))
        
    def drawSimpleCircle(self): 
        gfxdraw.aacircle(window, int(self.globalX),int(self.globalY),6,self.color)
        gfxdraw.aacircle(window, int(self.globalX),int(self.globalY),5, (255,255,255))
        
    def move(self):
        self.globalX = self.globalX + self.speedX
        self.globalY = self.globalY + self.speedY
        if abs(self.globalX-pygame.mouse.get_pos()[0])<5 and abs(self.globalY-pygame.mouse.get_pos()[1])<5:
            print "hit"

        
def redraw():
    pygame.drawSimpleCircle.rect(window, (0, 0, 0), (0, 0, screen_borderX, screen_borderY))
    attack1.process_spawners_bullet_movement()
    attack1.process_spawners_movement()
    pygame.display.flip()

def check_borders(X,Y):
    if(X>screen_borderX) or (Y>screen_borderY) or (X<0) or (Y<0):
        return 1
    return 0

screen_borderX=480
screen_borderY=640
    
window = pygame.display.set_mode((screen_borderX, screen_borderY)) 
#spawner1 = bullet_spawner(100,100)
#spawner2 = bullet_spawner(380,540)
attack1 = spawner_list()
#attack1.create_spawner(100, 100)
#attack1.create_spawner(380, 540)
#attack1.create_spawner(100, 540)
#attack1.create_spawner(380, 100)
#spawner1.drawSimpleCircle()

#print pygame.mouse.get_pos()[0]
pygame.display.flip()        
running = True
timeSpawn = time.time()
timeRedraw=time.time()
while running == True: 
    if (time.time()-timeSpawn>0.1):
        for i in attack1.list:
            i.spawn()
            
        timeSpawn = time.time()
    if (time.time()-timeRedraw>1/60):
        redraw()
        #attack1.move_spawner(0, 0.1, 0.1)
        timeRedraw = time.time()
    
    
    for event in pygame.event.get():   
        if event.type == pygame.QUIT: 
            sys.exit(0) 