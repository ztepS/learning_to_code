'''
Created on 01.04.2013

@author: user
'''
import sys
import pygame
import time
import random
pygame.init() 
random.seed()
# TODO:
# end game issues
# error on quit?


def check_lines():
    for i in range(12):
        countDots = 0
        for j in range(10):
            if(screenArray[i][j] == 1):
                countDots += 1
            if (countDots == 10) and (abs(fig.Y - i) > fig.shapeDimY): 
                    deleteline(i)
                    check_lines()
                    fig.score += 1000
                    print fig.score
def redraw():
    pygame.draw.rect(window, (0, 0, 0), (0, 0, 480, 640))
    for i in range(12):
        for j in range(10):
            if(screenArray[i][j] == 1):
                pygame.draw.rect(window, (255, 255, 255), ((48 * j) + 5, 596 - ((48 * i) + 5), 36, 36)) 
    pygame.display.flip()
    
def deleteline(lineN):

    fig.draw(0)
    for k in range((lineN), 11):
        # screenArray[k]=screenArray[k+1]
        for i in range(10):
            screenArray[k][i] = screenArray[k + 1][i]
    for k in range(10):
        screenArray[11][k] = 0
    redraw()
    
class figure:
    def __init__(self):
        self.score = 0
        self.firstrun = 1
        self.reinit()
        
    def draw(self, data):
        for i in range(self.shapeDimX):
            for j in range(self.shapeDimY):
                if (self.shape[i][j] == 1): 
                    screenArray[self.Y - 1 - j][self.X - 1 + i] = data
                    
    def reinit(self):
        self.X = 4
        self.Y = 12
        if self.firstrun == 0: 
            self.draw(0)
            check_lines()
        self.type = random.randrange(1, 8)
        if (self.type > 2):
            self.shapeDimX = 3
            self.shapeDimY = 2
        elif(self.type == 1):
            self.shapeDimX = 4
            self.shapeDimY = 1
        elif(self.type == 2): 
            self.shapeDimX = 2
            self.shapeDimY = 2
        self.shape = 0    
        self.shape = range(self.shapeDimX)
        for i in range(self.shapeDimX):
            self.shape[i] = range(self.shapeDimY)
            for j in range(self.shapeDimY):
                self.shape[i][j] = 0
        self.draw(0)
        if (self.type == 1): 
            self.shape[0][0] = 1
            self.shape[1][0] = 1
            self.shape[2][0] = 1
            self.shape[3][0] = 1
        elif (self.type == 5):
            self.shape[0][0] = 1
            self.shape[1][0] = 1
            self.shape[2][0] = 1
            self.shape[1][1] = 1
        elif (self.type == 3):
            self.shape[0][0] = 1
            self.shape[1][0] = 1
            self.shape[2][1] = 1
            self.shape[1][1] = 1    
        elif (self.type == 4):
            self.shape[0][1] = 1
            self.shape[1][1] = 1
            self.shape[2][0] = 1
            self.shape[1][0] = 1 
        elif (self.type == 2):  
            self.shape[0][0] = 1
            self.shape[0][1] = 1
            self.shape[1][0] = 1
            self.shape[1][1] = 1
        elif (self.type == 6):
            self.shape[2][0] = 1
            self.shape[2][1] = 1
            self.shape[0][1] = 1
            self.shape[1][1] = 1
        elif (self.type == 7):
            self.shape[0][0] = 1
            self.shape[0][1] = 1
            self.shape[1][1] = 1
            self.shape[2][1] = 1
        self.check_lose()
        self.draw(1)
        redraw()
        self.firstrun = 0
        
    def check_lose(self):
        if self.check_rotate() == 1: 
            pygame.quit()
            sys.exit(0)
        
    def check_down(self):
        for i in range(self.shapeDimX):
            self.lowestDot = 0
            k = self.shapeDimY - 1
         
            while(k > 0):
                if self.shape[i][k] == 1 :
                    self.lowestDot = k
                    k = 0
                k = k - 1
            
            if(screenArray[self.Y - self.lowestDot - 2][self.X + i - 1] == 1): return 1
        if (self.Y - self.shapeDimY < 1) :
            return 1
        else: return 0
        
    def check_left(self):
        for i in range(self.shapeDimY):
            self.lowestDot = self.shapeDimY
            k = 0
         
            while(k < self.shapeDimX):
                if self.shape[k][i] == 1 :
                    self.lowestDot = k
                    k = self.shapeDimX
                k = k + 1
            if(screenArray[self.Y - i - 1][self.X + self.lowestDot - 2] == 1): return 1
        else: return 0
        
    def check_right(self):
        for i in range(self.shapeDimY):
            self.lowestDot = 0
            k = self.shapeDimX - 1
         
            while(k > 0):
                if self.shape[k][i] == 1 :
                    self.lowestDot = k
                    k = 0
                k = k - 1
            try:
                if(screenArray[self.Y - i - 1][self.X + self.lowestDot] == 1): return 1
            except IndexError: return 1
        else: return 0
        
    def move(self, moveId):
        self.draw(0)
        if (moveId == 0):
            if(self.check_down() == 0):
                self.Y = self.Y - 1
            else:
                self.draw(1) 
                self.reinit()

        elif(moveId == 1):
            if (self.X + self.shapeDimX < 11) and (self.check_right() == 0):
                self.X = self.X + 1 
        elif(moveId == 2):
            if (self.X > 1) and (self.check_left() == 0):
                self.X = self.X - 1 
            
        self.draw(1)
        redraw() 
    
    def check_rotate(self):
        if(self.X + self.shapeDimY < 12) and self.check_down() == 0 and self.check_left() == 0 and self.check_right() == 0:
            for i in range(self.shapeDimX):
                for j in range(self.shapeDimY):
                    try:
                        if(screenArray[self.Y - 1 - i][self.X - 1 + j] == 1) and self.shape[j][i] == 0: return 1
                    except IndexError: return 1
            return 0
        
    def rotate(self):
        if(self.check_rotate() == 0):
            self.draw(0)
            self.shape2 = self.shape
            
            
            self.var = self.shapeDimX
            self.shapeDimX = self.shapeDimY
            self.shapeDimY = self.var
            
            self.shape = range(self.shapeDimX)
            for i in range(self.shapeDimX):
                self.shape[i] = range(self.shapeDimY)
                for j in range(self.shapeDimY):
                    self.shape[i][j] = self.shape2[j][self.shapeDimX - i - 1]
           
          
            self.draw(1) 
            redraw() 
        
        
window = pygame.display.set_mode((480, 640)) 

screenArray = range(12)
for i in range(12):
    screenArray[i] = range(10)
    for j in range(10):
        screenArray[i][j] = 0
        
       
fig = figure()
timeSpawn = time.time()
redraw()
running = True
while running == True: 
    if (time.time() - timeSpawn > 0.5):  # set difficulty
        fig.move(0)
        timeSpawn = time.time()
        
 
    for event in pygame.event.get():   
        if event.type == pygame.QUIT: 
            sys.exit(0) 
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_q]:
                running = False
                pygame.quit()
                sys.exit(0)   
            elif key[pygame.K_a]:
                fig.move(2)
            elif key[pygame.K_d]:
                fig.move(1)
            elif key[pygame.K_s]:
                while(fig.check_down() == 0):
                    fig.move(0)
            elif key[pygame.K_e]:
                fig.rotate()
            elif key[pygame.K_f]:
                print screenArray
