'''
Created on 12.02.2014

@author: user
'''

import pygame
import sys
import math
import pygame.gfxdraw as gfxdraw
pygame.init()

x1=120
y1=25
x2=160
y2=20
x3=130
y3=25

A = x2 - x1
B = y2 - y1
C = x3 - x1
D = y3 - y1
E = A * (x1 + x2) + B * (y1 + y2)
F = C * (x1 + x3) + D * (y1 + y3)
G = 2 * (A * (y3 - y2) - B * (x3 - x2))
#if G = 0 then Exit;
Cx = (D * E - B * F) / G
Cy = (A * F - C * E) / G

print Cx, Cy

rad = math.sqrt((x1-Cx)**2+(y1-Cy)**2)

print rad

window = pygame.display.set_mode((480, 640)) 
pygame.draw.circle(window,(255, 255, 255),(x1,y1),3)
pygame.draw.circle(window,(255, 255, 255),(x2,y2),3)
pygame.draw.circle(window,(255, 255, 255),(x3,y3),3)
pygame.draw.circle(window,(255, 255, 0),(Cx,Cy),3)
pygame.draw.circle(window,(255, 255, 0),(Cx,Cy),3)
gfxdraw.aacircle(window, int(Cx),int(Cy),int(rad), (255,255,255))
pygame.display.flip()

running = True
while running == True: 
    for event in pygame.event.get():   
        if event.type == pygame.QUIT: 
            sys.exit(0) 