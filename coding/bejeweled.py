'''
Created on 15.10.2013

@author: user
'''

import pygame
import sys
import random
import pygame.gfxdraw as gfxdraw


windowX=10
windowY=10

whiteColor=(255,255,255)
colorCount=6

cellSize=50
jewelSize=cellSize/2-3

pygame.init()
window = pygame.display.set_mode((windowX*cellSize, windowY*cellSize)) 

class Jewel:
    def __init__(self,x,y,static):
        self.boardX=x
        self.boardY=y
        self.globalY=(cellSize*y)-1+cellSize/2
        self.globalX=(cellSize*x)-1+cellSize/2
        self.type=random.randrange(1, colorCount)
        self.color=pick_color(self.type)
        self.static=static
        self.removeMark=0
        
        
    def draw(self):
        gfxdraw.filled_circle(window, self.globalX ,self.globalY ,jewelSize-1,self.color)
        if(self.removeMark==1): gfxdraw.filled_circle(window, self.globalX ,self.globalY ,jewelSize-5,(255,255,255))
def pick_color(colorNum):
    
    
    if(colorNum==1):
        return (255,0,0)
    elif(colorNum==2):
        return (0,255,0)
    elif(colorNum==3):
        return (0,0,255)
    elif(colorNum==4):
        return (255,127,0)
    elif(colorNum==5):
        return (0,255,127)    

def update_screen():
    pygame.draw.rect(window, (0, 0, 0), (0, 0, windowX*cellSize, windowY*cellSize))
    for i in range(windowY):
        gfxdraw.line(window, 0,cellSize*i,windowX*cellSize,cellSize*i,whiteColor)
    for i in range(windowX):
        gfxdraw.line(window, cellSize*i,0,cellSize*i,windowY*cellSize,whiteColor)
        
    for i in range(windowX):
        for j in board[i]:
            j.draw()
    
    pygame.display.flip()

def process_board():
    changed=0
    for i in range(windowX):
        hitCount=0
        tempColor=0
        for j in range(windowY):
            if(board[i][j].type==tempColor): 
                if(hitCount<2):hitCount+=1
                else:
                    board[i][j].removeMark=1
                    board[i][j-1].removeMark=1
                    board[i][j-2].removeMark=1
                    changed=1
            else:
                hitCount=1
                tempColor=board[i][j].type
            
    for j in range(windowY):
        hitCount=0
        tempColor=0
        for i in range(windowX):
            if(board[i][j].type==tempColor): 
                if(hitCount<2):hitCount+=1
                else:
                    board[i-1][j].removeMark=1
                    board[i-2][j].removeMark=1
                    board[i][j].removeMark=1
                    changed=1
            else:
                hitCount=1
                tempColor=board[i][j].type
    return changed

#pygame.draw.circle(window,whiteColor , (cellSize/2,0), jewelSize, 0)

#gfxdraw.aacircle(window, cellSize/2 ,0 ,jewelSize,whiteColor)



board = range(windowX)
for i in range(windowX):
    board[i] = range(windowY)
    for j in range(windowY):
        board[i][j]=Jewel(j,i,1)

process_board()
update_screen()



running = True
while running == True: 
    for event in pygame.event.get():   
        if event.type == pygame.QUIT: 
            sys.exit(0) 