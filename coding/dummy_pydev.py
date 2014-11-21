'''
Created on 11.08.2014

@author: user
'''
import pygame
import sys

pygame.init() 

window = pygame.display.set_mode((480, 640)) 

running = True
while running == True: 
    for event in pygame.event.get():   
        if event.type == pygame.QUIT: 
            sys.exit(0) 
            
            