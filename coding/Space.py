'''
Created on 02.10.2013

@author: user
'''
import pygame
import sys
import math
import time
import random
import pygame.gfxdraw as gfxdraw



windowX=1024
windowY=768

pygame.init()
window = pygame.display.set_mode((windowX, windowY)) 
pygame.display.flip()


class Bullet:
    def __init__(self,X,Y,speedX,speedY):
        #self.bulletid=bulletid
        self.globalX = X
        self.globalY = Y
        self.speedX=speedX
        self.speedY=speedY
        #self.framespeed=1/30
        self.color=(random.randrange(0, 256),random.randrange(0, 256),random.randrange(0, 256))
        
    def draw(self): 
        gfxdraw.aacircle(window, int(self.globalX),int(self.globalY),3,self.color)
        gfxdraw.aacircle(window, int(self.globalX),int(self.globalY),2, (255,255,255))
       
        
    def move(self):
        self.globalX = self.globalX + self.speedX
        self.globalY = self.globalY + self.speedY
        
#        if abs(self.globalX-pygame.mouse.get_pos()[0])<5 and abs(self.globalY-pygame.mouse.get_pos()[1])<5:
#            print "hit"

class Bullet_list:
    def __init__(self):

        self.bullet_list=[]
          
    def draw(self):
        #pygame.draw.rect(window, (0, 0, 0), (0, 0, screen_borderX, screen_borderY))
        for i in self.bullet_list:
            i.draw()
            
    def process_movement(self):
        for i in self.bullet_list:
            i.move()
            if (check_borders(i.globalX,i.globalY)==1): 
                self.bullet_list.remove(i)

def redraw_screen():
    global gunX
    global gunY
    pygame.draw.rect(window, (0, 0, 0), (0, 0, windowX, windowY))
    if(mouseX==playerX and mouseY==playerY):
        gunX=mouseX
        gunY=mouseY  
    else:
        gunX=playerX+playerSize*(mouseX-playerX)/math.sqrt((mouseX-playerX)**2+(mouseY-playerY)**2)
        gunY=playerY+playerSize*(mouseY-playerY)/math.sqrt((mouseX-playerX)**2+(mouseY-playerY)**2)
    gfxdraw.aacircle(window, int(playerX),int(playerY),playerSize,(255,255,255))
    #gfxdraw.line(window,int(playerX),int(playerY),int(gunX),int(gunY),(255,255,255))
    pygame.draw.aaline(window, (255,255,255),(int(playerX),int(playerY)),(int(gunX),int(gunY)))
    playerBulletList.draw()
    pygame.display.flip()
    

def process_movement():
    
    global playerX
    global playerY
    global moveX
    global moveY
    global playerBulletList
    global inertiaX
    global inertiaY
    
    playerBulletList.process_movement()
    
    if(moveX<>0 and moveY<>0):
        moveX*=0.707
        moveY*=0.707
    if((playerX-playerSize-playerSpeed<0 and moveX<0) or ((playerX+playerSize+playerSpeed>windowX and moveX>0))): moveX=0
    if((playerY-playerSize-playerSpeed<0 and moveY<0) or ((playerY+playerSize+playerSpeed>windowY and moveY>0))): moveY=0
        
    inertiaX=inertiaX+moveX*inertia
    inertiaY=inertiaY+moveY*inertia
    if(inertiaX>1):inertiaX=1
    if(inertiaY>1):inertiaX=1
    moveX+=inertiaX
    moveY+=inertiaY
    if(moveX>1):moveX=1
    if(moveY>1):moveY=1
    playerX+=playerSpeed*moveX
    playerY+=playerSpeed*moveY
    inertiaX=inertiaX*(1-inertia)
    inertiaY=inertiaY*(1-inertia)


def check_borders(X,Y):
    if(X>windowX) or (Y>windowY) or (X<0) or (Y<0):
        return 1
    return 0

def fire():
    global shotReady
    global firing
    global gunX
    global gunY
    if(playerX==gunX and playerY==gunY): gunX=1
    if(firing==1): 
        if(shotReady>=1):
            playerBulletList.bullet_list.append(Bullet(gunX,gunY,-(playerX-gunX)*bulletSpeed,-(playerY-gunY)*bulletSpeed))
            shotReady=0
        else: shotReady+=gunSpeed


playerX=windowX/2
playerY=windowY/2
playerSize=20
playerSpeed=2

bulletSpeed=0.05*5
gunSpeed=0.1

mouseX=1000
mouseY=221

gunX=0
gunY=0

inertiaX=0
inertiaY=0

inertia=0.05

playerBulletList=Bullet_list()

#gfxdraw.line(window,int(playerX),int(playerY),int(gunX),int(gunY),(255,255,255))

#gfxdraw.aacircle(window, int(playerX),int(playerY),playerSize,(255,255,255))
pygame.display.flip()

frameSwitch=1
firing=0

running = True
while running == True: 
    moveX=0
    moveY=0
    if(frameSwitch==1): startTime=time.time()
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        moveY=-1
    if key[pygame.K_s]:
        moveY=1
    if key[pygame.K_a]:
        moveX=-1
    if key[pygame.K_d]:
        moveX=1
    
    startTime=time.time()

    for event in pygame.event.get():   
        if event.type == pygame.QUIT: 
            sys.exit(0) 
            
        elif event.type == pygame.MOUSEMOTION:
            mouseX=event.pos[0]
            mouseY=event.pos[1]
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            firing=1
            shotReady=1
                               
                
        elif event.type == pygame.MOUSEBUTTONUP:
            firing=0
            
            
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_q]:
                running = False
                pygame.quit()
                
    if time.time()-startTime>1/60:
        process_movement()
        fire()

        redraw_screen()
        frameSwitch=1

    else: frameSwitch=0
            