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
            i.draw()
            
    def process_spawners_movement(self):
        if(self.type==1):
            self.pattern1_move()
        
    def move_spawner(self,sp_id,X,Y):
        self.list[sp_id].X+=X
        self.list[sp_id].Y+=Y
        if (check_borders(self.list[sp_id].X,self.list[sp_id].Y)==1) and (self.list[sp_id].bullet_list==[]):
            del self.list[sp_id]
            #print self.list, sp_id
            
    def pattern1(self):
        self.create_spawner(100, 100)
        self.create_spawner(380, 540)
        self.create_spawner(100, 540)
        self.create_spawner(380, 100)
    
    def pattern1_move(self):
        self.move_spawner(0, 0.1, 0.1)
        
class bullet_spawner:
    def __init__(self,X,Y):
        self.X=X
        self.Y=Y
        self.bullet_count = 0
        self.phase = 0
        self.bullet_list=[]
        self.spawn()
    
        
        
    def draw(self):
        #pygame.draw.rect(window, (0, 0, 0), (0, 0, screen_borderX, screen_borderY))
        pygame.draw.circle(window,(255, 255, 255),(int(self.X),int(self.Y)),5)
        for i in self.bullet_list:
            
            i.draw()
                
        
    def spawn(self):
        #self.spawncount = 100
        
        self.spawning = True
        #for i in range(self.spawncount):
        self.phase += 0.5
        self.bullet_list.append(bullet(int(self.X),int(self.Y),math.sin(self.phase)*1,math.cos(self.phase)*1)   ) 
        #print self.bullet_list
        
    def process_movement(self):
        for i in self.bullet_list:
            i.move()
            if (check_borders(i.X,i.Y)==1): 
                self.bullet_list.remove(i)
                
class bullet:
    def __init__(self,X,Y,speedX,speedY):
        #self.bulletid=bulletid
        self.X = X
        self.Y = Y
        self.speedX=speedX
        self.speedY=speedY
        #self.framespeed=1/30
        self.color=(random.randrange(0, 256),random.randrange(0, 256),random.randrange(0, 256))
        
    def draw(self): 
        gfxdraw.aacircle(window, int(self.X),int(self.Y),6,self.color)
        gfxdraw.aacircle(window, int(self.X),int(self.Y),5, (255,255,255))
        
    def move(self):
        self.X = self.X + self.speedX
        self.Y = self.Y + self.speedY
        if abs(self.X-pygame.mouse.get_pos()[0])<5 and abs(self.Y-pygame.mouse.get_pos()[1])<5:
            print "hit"

        
def redraw():
    pygame.draw.rect(window, (0, 0, 0), (0, 0, screen_borderX, screen_borderY))
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
#spawner1.draw()

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