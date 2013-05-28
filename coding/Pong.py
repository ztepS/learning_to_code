'''
Created on 19.03.2013

@author: user
'''
import sys
# import time
# import and init pygame
import pygame
pygame.init() 

screenWidth = 640
screenHeight = 480

paddleLength = 80
paddleSpeed = 0.3
paddleAPos = screenHeight / 2 - paddleLength / 2
paddleBPos = screenHeight / 2 - paddleLength / 2

ballSize = 10
ballXPos = screenWidth / 2 - ballSize / 2
ballYPos = screenHeight / 2 - ballSize / 2
ballXspeed = 0.08
ballYspeed = 0.08

scoreA = 0
scoreB = 0
# create the screen
window = pygame.display.set_mode((screenWidth, screenHeight)) 

# draw a line - see http://www.pygame.org/docs/ref/draw.html for more 
# pygame.draw.aaline(window, (255, 255, 255), (0, 0), (30, 50))
# pygame.draw.rect(window, (255, 255, 255), (ballXPos,ballYPos,ballSize,ballSize))
# draw it to the screen
# pygame.display.flip() 

i = 0
# input handling (somewhat boilerplate code):
while True: 
    
#    pygame.draw.rect(window, (0, 0, 0), (i,40,10,10))
#    i+=1
#    pygame.draw.rect(window, (255, 255, 255), (i,40,10,10))
#    time.sleep(1/60)
   
#   Ball handling
    pygame.draw.rect(window, (0, 0, 0), (ballXPos, ballYPos, ballSize, ballSize))
    ballXPos += ballXspeed
    ballYPos += ballYspeed
    ballXspeed *= 1.000001
    ballYspeed *= 1.000001
    
    if(ballYPos > screenHeight):
        ballYPos = screenHeight
        ballYspeed = -ballYspeed
    if(ballXPos > screenWidth - 10 - ballSize):
        if((ballYPos > paddleBPos) and ballYPos < (paddleBPos + paddleLength)):
            ballXspeed = -ballXspeed
            ballXPos = screenWidth - 12 - ballSize
    if(ballXPos < 10):
        if((ballYPos > paddleAPos) and ballYPos < (paddleAPos + paddleLength)):
            ballXpos = 12
            ballXspeed = -ballXspeed
    if(ballXPos < 0):
        ballXPos = screenWidth / 2 - ballSize / 2
        ballYPos = screenHeight / 2 - ballSize / 2
        ballXspeed = -ballXspeed
        scoreB += 1
        ballXspeed = 0.08
        ballYspeed = 0.08
        print scoreA, " - ", scoreB 
    if(ballXPos > screenWidth - ballSize):
        ballXPos = screenWidth / 2 - ballSize / 2
        ballYPos = screenHeight / 2 - ballSize / 2
        ballXspeed = -ballXspeed
        scoreA += 1
        ballXspeed = 0.08
        ballYspeed = 0.08
        print scoreA, " - ", scoreB 
    if(ballYPos < 0):
        ballYPos = 0
        ballYspeed = -ballYspeed
    pygame.draw.rect(window, (255, 255, 255), (ballXPos, ballYPos, ballSize, ballSize))
    
    pygame.draw.rect(window, (255, 255, 255), (0, paddleAPos, 10, paddleLength)) 
    
    # Player paddle handling
    key = pygame.key.get_pressed()
    if key[pygame.K_s]:
        if((paddleAPos + paddleLength) < screenHeight):
            pygame.draw.rect(window, (0, 0, 0), (0, paddleAPos, 10, paddleLength)) 
            paddleAPos += paddleSpeed
    elif key[pygame.K_w]:
        if(paddleAPos > 0):
            pygame.draw.rect(window, (0, 0, 0), (0, paddleAPos, 10, paddleLength)) 
            paddleAPos -= paddleSpeed
    pygame.draw.rect(window, (255, 255, 255), (0, paddleAPos, 10, paddleLength)) 
    
    
    # Enemy paddle handling
    pygame.draw.rect(window, (0, 0, 0), (screenWidth - 10, paddleBPos, screenWidth, paddleLength)) 
    if(paddleBPos + paddleLength < ballYPos):
        paddleBPos += paddleSpeed
    if(paddleBPos > ballYPos):
        paddleBPos -= paddleSpeed   
    pygame.draw.rect(window, (255, 255, 255), (screenWidth - 10, paddleBPos, screenWidth, paddleLength)) 
    
   
    # Draw screen
    pygame.display.flip()
    
    for event in pygame.event.get(): 
        
        if event.type == pygame.QUIT: 
            sys.exit(0) 
                                  
            
        # else: 
            # print scoreA, " - ", scoreB 
