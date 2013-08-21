'''
Created on 08.08.2013

@author: user
'''
import sys
import pygame
import pygame.gfxdraw as gfxdraw
import random
import time
pygame.init() 


def draw_o(x,y):
    gfxdraw.aacircle(window, 50+100*x,50+100*y,30,(255,0,0))
    
def draw_x(x,y):
    gfxdraw.line(window,20+100*x,20+100*y,80+100*x,80+100*y,(0,0,255))
    gfxdraw.line(window,80+100*x,20+100*y,20+100*x,80+100*y,(0,0,255))
    
def check_won(side,layout,active):
    countD=0
    countD2=0
    for i in range(3):
        countX=0
        countY=0
        if(layout.field[i][i]==side):countD+=1
        if(layout.field[2-i][i]==side):countD2+=1
        for j in range(3):
            if(layout.field[i][j]==side):countX+=1
            if(layout.field[j][i]==side):countY+=1
        if(countX==3):
                
            if(active==1): 
                gfxdraw.line(window,50+100*i,0,50+100*i,300,(255,255,255))
                pygame.display.flip()
                return 1
        if(countY==3):
            if(active==1): 
                gfxdraw.line(window,0,50+100*i,300,50+100*i,(255,255,255))
                pygame.display.flip()
            return 1
                
    if(countD==3):
        if(active==1): 
            gfxdraw.line(window,0,0,300,300,(255,255,255))
            pygame.display.flip()
        return 1
    if(countD2==3):
        if(active==1): 
            gfxdraw.line(window,0,300,300,0,(255,255,255))
            pygame.display.flip()
        return 1
    return 0
    
    
    
class Player:
    def move(self,side):
        
        running = True
        while running == True: 
    
            for event in pygame.event.get():   
                if event.type == pygame.QUIT: 
                    sys.exit(0) 
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    xInt=int(pos[0]/100)
                    yInt=int(pos[1]/100)
                    if(gameField.field[xInt][yInt]==0):
                        return(xInt,yInt)


class Easy_Ai:
    def move(self,side):
        found=0
        while(found==0):
            x=random.randrange(0, 3)
            y=random.randrange(0, 3)
            if(gameField.field[x][y]==0):found=1
        return(x,y)

#class Move:
#    def __init__(self,move):
#        self.move=move
#        self.won=0
#    
#class Position:
#    def __init__(self, pos):
#        self.position=pos
#        for i in range(3):
#            for j in range(3)
       

class Medium_Ai:
    #def __init__(self):
                        
        
    def move(self,side):
        

        for i in range(3):
            for j in range(3):
                if (gameField.field[i][j]==0):
                    tempField=Field()
                    
                    for k in range(3): 
                        for m in range(3): 
                            tempField.field[k][m]=gameField.field[k][m]
                    tempField.field[i][j]=((1-(side-1))+1)
                    #print tempField.field
                
                    a=check_won((1-(side-1))+1, tempField, 0)
                    tempField.clear()
                    if (a==1):return(i,j)
                    #print(a)
        found=0
        while(found==0):
            x=random.randrange(0, 3)
            y=random.randrange(0, 3)
            if(gameField.field[x][y]==0):found=1
        return(x,y)
           

class Judge:
    def __init__(self,pl1,pl2):
        self.turns=0
        
        while self.turns<9:
            sideA=pl1.move(1)
            gameField.draw(sideA[0],sideA[1],1)
            gameField.field[sideA[0]][sideA[1]]=1
            if(check_won(1,gameField,1)==1):self.turns=9
            self.turns+=1
            if(self.turns<8):sideB=pl2.move(2)
            gameField.draw(sideB[0],sideB[1],0)
            gameField.field[sideB[0]][sideB[1]]=2
            if(check_won(2,gameField,1)==1):self.turns=9
            self.turns+=1
        time.sleep(1)
        sys.exit(0)  
         
class Judge_stat:
    def __init__(self,pl1,pl2,times):
        won_a=0
        won_b=0
        
        for i in range(times):
            gameField.clear()
            self.turns=0
            while self.turns<9:
                sideA=pl1.move(1)
                #gameField.draw(sideA[0],sideA[1],1)
                gameField.field[sideA[0]][sideA[1]]=1
                if(check_won(1,gameField,1)==1):
                    self.turns=9
                    won_a+=1
                self.turns+=1
                if(self.turns<8):sideB=pl2.move(2)
                #gameField.draw(sideB[0],sideB[1],0)
                gameField.field[sideB[0]][sideB[1]]=2
                if(check_won(2,gameField,1)==1):
                    self.turns=9
                    won_b+=1
                self.turns+=1
        print won_a, " - " , won_b, "(", (times-(won_a+won_b)), " draws)"
        #time.sleep(1)
        sys.exit(0)  


class Field:
    
    def __init__(self):
        self.field=range(3)
        self.clear()
        
    
    def draw(self,x,y,side):
        
        if(side==1): draw_x(x,y)
        else: draw_o(x,y)
        
        pygame.display.flip()
#        for i in range(3):
#            for j in range(3):
#                print self.field[i][j],
#            print "\n"
    
    
    def clear(self):
        for i in range(3):
            self.field[i]=range(3)
            for j in range(3):
                self.field[i][j]=0
        
        gfxdraw.line(window,0,100,300,100,(255,255,255))
        gfxdraw.line(window,0,200,300,200,(255,255,255))
        gfxdraw.line(window,100,0,100,300,(255,255,255))
        gfxdraw.line(window,200,0,200,300,(255,255,255))
        pygame.display.flip()

window = pygame.display.set_mode((300, 300)) 


#def load_data():
#    f = open("tictactoe.txt", 'w')
#    f.write(str(gameField.field))

player1 = Player()
player2 = Player()
ai=Easy_Ai()
ai2=Medium_Ai()
ai3=Medium_Ai()
gameField = Field()
#ai=Easy_Ai()
#gameField.draw(0,2,1)

#judge=Judge(ai3,ai2)
judge_stat=Judge_stat(ai,ai2,1000)
                
                