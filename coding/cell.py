'''
Created on 14.04.2014

@author: user
'''
import sys
import pygame
import pygame.gfxdraw as gfxdraw
import random
pygame.init() 
random.seed()

screenX=1024
screenY=768

window = pygame.display.set_mode((screenX, screenY))

lightMap=range(screenX)
for i in range(screenX):
    lightMap[i]=range(screenY)
    for j in range(screenY):
        lightMap[i][j]=(random.randrange(10, 200)+0.0)/3 # make some light generator later
        
collisionMap=range(screenX)
for i in range(screenX):
    collisionMap[i]=range(screenY)
    
def resetCollision():
    for i in range(screenX):
        for j in range(screenY):
            if(i==0 or j==0 or i==screenX or j==screenY):collisionMap[i][j]=1
            else: collisionMap[i][j]=0
            

def randomside():
    return random.randrange(-1, 2)


def place_check(X,Y,size):
#    for i in range(int(X-size),int(X+size)):
#        for j in range(int(Y-size),int(Y+size)):
#            if(collisionMap[i][j]==1):return 0
    if(X-size<2 or Y-size<2 or X+size>screenX-2 or Y+size>screenY-2): return -1
    if (collisionMap[int(X-size)-1][int(Y)]==1) or (collisionMap[int(X+size)+1][int(Y)]==1) or (collisionMap[int(X)][int(Y-size)-1]==1) or (collisionMap[int(X)][int(Y+size)+1]==1):
        return 0
    return 1

class cell:
    def __init__(self,X,Y,size):
        self.X=X
        self.Y=Y
        self.type="photo"
        self.size=size
        self.maxSize=8
        self.energy=100
        
        if(self.type=="photo"):self.color=(0,200,0)
    
    def move(self,X,Y):
        
#        if(self.X-self.size<2):
#            return 0
#            self.type="dead"
#        if(self.X+self.size>screenX-2):
#            return 0
#            self.type="dead"
#        if(self.Y-self.size<2):
#            return 0
#            self.type="dead"
#        if(self.Y+self.size>screenY-2):
#            return 0
#            self.type="dead"
        moved = place_check(self.X,self.Y,self.size)
        if(moved==-1): self.type="dead" 
        if(self.type=="dead"):
            self.color=(50,50,50)
            return 0
        self.X+=X
        self.Y+=Y
        
    def draw(self): 
        gfxdraw.aacircle(window, int(self.X),int(self.Y),int(self.size),self.color)
        
    def resize_cell(self):
        if(self.type=="photo" and place_check(self.X,self.Y,self.size)==1):
            self.size+=(lightMap[self.X][self.Y]/self.size)
            self.energy+=1
        else: 
            self.move(randomside(),randomside())
            self.energy-=1
        if(self.energy<=0):self.type="dead"
        if (self.size>self.maxSize): self.divide()
    
    def set_collision(self):
        for i in range(int(self.X-self.size),int(self.X+self.size)):
            for j in range(int(self.Y-self.size),int(self.Y+self.size)):
                try: collisionMap[i][j]=1
                except IndexError:print
    def divide(self):  
        self.size=self.size/2
        pool.create_cell(self.X+int(self.size*2+1)*randomside(), self.Y+int(self.size*2+1)*randomside(), self.size)
        

class cell_list:
    def __init__(self):
        self.list=[]

    def create_cell(self,X,Y,size):
        self.list.append(cell(X,Y,size))
        
    def process_cells(self):
        resetCollision()
        for i in self.list:
            i.set_collision()
        for i in self.list:
            i.resize_cell()
            #i.process_movement()
            i.draw()

def redraw():
    pygame.draw.rect(window, (0, 0, 0), (0, 0, screenX, screenY))
    
#    for i in range(screenX):
#        for j in range(screenY):
#            pygame.gfxdraw.pixel(window,i,j,(int(lightMap[i][j])*10,int(lightMap[i][j])*10,0))
            
    pool.process_cells()
    pygame.display.flip()



pool=cell_list()
pool.create_cell(screenX/2, screenY/2, 1)


running = True
while running == True: 
    redraw()

    for event in pygame.event.get():   
        if event.type == pygame.QUIT: 
            sys.exit(0) 