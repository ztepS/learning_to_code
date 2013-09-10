'''
Created on 20.08.2013

@author: user
'''
#import numpy
import pygame
import random
import sys
random.seed()

fieldX=300
fieldY=300
screenX=50
screenY=120
screenCoordX=0
screenCoordY=0


class Point:
    def __init__(self):
        self.terrainHeight=0
        self.stack=[]
        
    def return_symbol(self):
        if (self.stack==[]):return " "
        return self.stack[len(self.stack)-1].return_symbol()
        
    def return_color(self):
        if (self.stack==[]):return (0,0,0)
        return self.stack[len(self.stack)-1].return_color()
    
class Explosion_effect:    
    def __init__(self):
        self.hp=5
        
    def return_symbol(self):
        return "*"
    
    def return_color(self):
        #self.hp-=0.1
        if(self.hp<0 or self.hp>5): return(0,0,0)
        return(int(self.hp*50),0,0)
        
    def explode(self,strength):
        self.hp+=strength
        if(self.hp>5):self.hp=5
        return 0
          
          
class Fire:    
    def __init__(self):
        self.hp=5
        
    def return_symbol(self):
        return "*"
    
    def return_color(self):
        #self.hp-=0.1
        if(self.hp<0 or self.hp>5): return(0,0,0)
        return(int(self.hp*50),0,0)
        
    def explode(self,strength):
        self.hp+=strength
        if(self.hp>5):self.hp=5
        return 0
    
    def burn(self,strength):
        return 0
                    
def burn_process(x,y,hp):
    
    for k in field[x][y].stack:
        strength-=k.burn()

class Building:
    def __init__(self,stores):
        self.storesCount=stores
        self.hp=stores*10
    
    def explode(self,strength):
        self.hp-=strength
        return self.storesCount
        
    def return_symbol(self):
        if (self.hp<self.storesCount/2):return"*"
        if (self.storesCount<3):return"^"
        if (self.storesCount<15):return"#"
        return "H"
    
    def return_color(self):
        if (self.hp<self.storesCount/5):return (30,30,30)
        return (200,200,200)
    
    def burn(self,strength):
        if (self.storesCount<3):
            self.hp-=strength*2
            return 0.3
        else:
            self.hp-=strength*0.2
            return -0.5
    
    
class Road:
    def __init__(self,direction):
        self.direction = direction
        self.hp = 10
    
    def return_symbol(self):
        if (self.hp<5):return"*"
        if (self.direction==0): return"="
        if (self.direction==1): return"\""
        
    def explode(self,strength):
        self.hp-=strength
        return 0
    
    def return_color(self):
        if (self.hp<5):return (30,30,30)
        return (50,50,50)
    
class Water:
    def __init__(self):
        self.hp=20
    
    def return_symbol(self): return "~"
    
    def explode(self,strength):
        self.hp-=strength
        return 0
    
    def return_color(self):
        
        return (0,0,150)

def process_hp():
    for i in range(fieldX):
        for j in range(fieldY):
            for k in field[i][j].stack[:]:
                if k.__class__.__name__ == "Explosion_effect": k.hp-=0.1
                if k.__class__.__name__ == "Fire": burn_process(i,j,k.hp)
                if(k.hp<=0): 
                    field[i][j].stack.remove(k)
                
 


def explosion(x,y,strength,decay):
    
    for i in field[x][y].stack:
    
        strength -= i.explode(strength)
    if(x>fieldX-2 or y>fieldY-2 or x <1 or y < 1 or strength<=0): return -1
    
    field[x][y].stack.append(1)
    if(field[x+1][y].stack ==[] or field[x+1][y].stack[-1]!=1): explosion(x+1,y,strength-decay,decay)
    if(field[x-1][y].stack ==[] or field[x-1][y].stack[-1]!=1): explosion(x-1,y,strength-decay,decay)
    if(field[x][y+1].stack ==[] or field[x][y+1].stack[-1]!=1): explosion(x,y+1,strength-decay,decay)
    if(field[x][y-1].stack ==[] or field[x][y-1].stack[-1]!=1): explosion(x,y-1,strength-decay,decay)
    del field[x][y].stack[-1]
    field[x][y].stack.append(Explosion_effect())

def generate_town(field,startX,startY,size):
    #field[startX][startY].stack.append(Road(0))
    sys.setrecursionlimit(999999)
    #create_water(10,10)
    create_terrain()
    create_road(startX,startY,size,1)
    sys.setrecursionlimit(999)
    
    
def create_road(x,y,strength,direction):
    if(x<1 or y<1 or x>fieldX-2 or y> fieldX-2 or strength < 1):return -1
    field[x][y].stack.append(Road(direction)) 
    
    newStrength=strength-random.randrange(1,10)
    
    if(direction == 1 or random.randrange(0,10)==0):
        if(field[x+1][y].stack==[] ):create_road(x+1,y,newStrength,1)
        if(field[x-1][y].stack==[] ):create_road(x-1,y,newStrength,1)
    else: 
        if(field[x+1][y].stack==[]  and random.randrange(1,10)<5):field[x+1][y].stack.append(Building(int(newStrength/10+1)))
        if(field[x-1][y].stack==[]  and random.randrange(1,10)<5):field[x-1][y].stack.append(Building(int(newStrength/10+1)))
        
    if(direction == 0 or random.randrange(0,10)==0):
        if(field[x][y+1].stack==[] ):create_road(x,y+1,newStrength,0)
        if(field[x][y-1].stack==[] ):create_road(x,y-1,newStrength,0)
    else:
        if(field[x][y+1].stack==[]  and random.randrange(1,10)<5):field[x][y+1].stack.append(Building(int(newStrength/10+1)))
        if(field[x][y-1].stack==[]  and random.randrange(1,10)<5):field[x][y-1].stack.append(Building(int(newStrength/10+1)))

def create_water(x,y):
    field[x][y].stack.append(Water())
    
    if(x>fieldX-2 or y>fieldY-2 or x <1 or y < 1): return -1
    if (field[x+1][y].terrainHeight<=field[x][y].terrainHeight and field[x+1][y].stack==[] ):create_water(x+1,y)
    if (field[x-1][y].terrainHeight<=field[x][y].terrainHeight and field[x-1][y].stack==[]):create_water(x-1,y)
    if (field[x][y+1].terrainHeight<=field[x][y].terrainHeight and field[x][y+1].stack==[]):create_water(x,y+1)
    if (field[x][y-1].terrainHeight<=field[x][y].terrainHeight and field[x][y-1].stack==[]):create_water(x,y-1)

def make_sea(x,y,strength):
    if(x<0 or y<0 or x>fieldX-2 or y> fieldX-2 or strength < 1):
        return -1
    field[x][y].stack.append(Water())
    field[x][y].terrainHeight=field[x][y].terrainHeight-int(strength/3)
    if(field[x+1][y].stack==[]):make_sea(x+1,y,strength-random.randrange(0,20))
    if(field[x][y+1].stack==[]):make_sea(x,y+1,strength-random.randrange(0,20))
    


def handle_keys():
    global screenCoordX
    global screenCoordY
    key = pygame.key.get_pressed()
    if key[pygame.K_s]:
        if(screenX+screenCoordX<fieldX):screenCoordX+=1
    elif key[pygame.K_d]:
        if(screenY+screenCoordY<fieldY):screenCoordY+=1   
    elif key[pygame.K_w]:
        if(screenCoordX>0):screenCoordX-=1
    elif key[pygame.K_a]:
        if(screenCoordY>0):screenCoordY-=1

def create_terrain():
    #a=random.randrange(1,4)
    a=1
    if(a==1):
        make_sea(0,0,650)
        #create_water(2,2)

def simple_visualize():
    screen.fill((0, 0, 0))
    
    for i in range(screenX):
        for j in range(screenY):

            text = font.render(field[i+screenCoordX][j+screenCoordY].return_symbol(), True, field[i+screenCoordX][j+screenCoordY].return_color())
            screen.blit(text,(screenCoordY+j*fontSize,screenCoordX+i*fontSize ))

#field=numpy.zeros((fieldX,fieldY),dtype=Point)

field = range(fieldX)
for i in range(fieldX):
    field[i]=range(fieldY)
    for j in range(fieldY):
        field[i][j] = Point()


generate_town(field,40,50,500)
#explosion(40,60,10,1)
#process_hp()
#simple_visualize(field)

pygame.init()
screen = pygame.display.set_mode((1280, 800))
fontSize=12
font = pygame.font.SysFont("calibri", fontSize)





done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            explosion(int(pos[1]/fontSize)+screenCoordX,int(pos[0]/fontSize)+screenCoordY,8,1)
            
            
            
#    screen.fill((0, 0, 0))
#    screen.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
    handle_keys()
    process_hp()
    simple_visualize()    
    pygame.display.flip()

#field[30][30].stack.append(Road(0))
#field[30][30].stack.append(Building(3))
#print field[30][30].return_symbol()
#
#print field[30][30].stack



    
    
    
    