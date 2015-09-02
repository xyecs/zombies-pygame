# Import modules
import time
import random
import math
from pygame import *
from pygame.locals import *

init()

display.set_caption("Defend Your Base - Zombie Attack")

# Set screen size
SIZE = width, height = (800, 500)
screen = display.set_mode(SIZE)

# RGB values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
CHOCO = (139, 69, 19)
GOOP  = (46, 139, 87)

# Method to get mouse positions 
# (Where the mouse moves or which button is pressed)
def getmouse():
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()[0]
    return mx, my, mb

zombieX = []
zombieY = []
zombieH = []

def zombies():
    zombieN = 10
    while zombieN != 0:
        rx = random.randint(1, 800)
        ry = random.randint(1, 500) 
        if 0 < ry < 100 or 0 < rx < 100 or 500 > ry > 400 or 800 > rx > 700:
            draw.circle(screen, GREEN, (rx, ry), 12)
            zombieX.append(rx)
            zombieY.append(ry)
            zombieH.append(10)
            zombieN -= 1
            
            time.wait(60)
            
    display.flip()
    
# If zombie postitions not equal to barricade move positions closer
#def zombieMove():
    #posX = 0
    #posY = 0
    
    #for i in zombieX:
        #if i != 400:
            #i += 1
            #zombieX[posX] = i
            #posX += 1
            
    #for q in zombieY:
        #if q != 250:
            #q += 1
            #zombieY[posY] = i
            #posX += 1
            
def zombieUpdate():        
    zy = 0
    for zx in zombieX:
        
        # Body
        draw.rect(screen, CHOCO, Rect(zx - 20, zombieY[zy] - 20, 20, 40))
        # Arms
        draw.rect(screen, GOOP, Rect(zx, zombieY[zy] - 20, 20, 10))
        draw.rect(screen, GOOP, Rect(zx, zombieY[zy] + 10, 20, 10))
        # Head
        draw.circle(screen, GREEN, (zx, zombieY[zy]), 12)
        
        
        zy += 1
        
        time.wait(100)
    
    display.flip()
    
#Main Game Loop
running = 1
myClock = time.Clock()

zombies()
while running:
    
    mx, my, mb = getmouse()
    
    for evnt in event.get():
        
        if evnt.type == QUIT:
            running = 0
            
    #zombieMove()
    zombieUpdate()
    myClock.tick(60)
    
    
# Exit               
quit()