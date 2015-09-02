# Import modules
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


# Method to get mouse positions 
# (Where the mouse moves or which button is pressed)
def getmouse():
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()[0]
    return mx, my, mb



x = 105
y = 300
movex = 0
movey = 0

def mainC():
    
    global x, y
    
    screen.fill(BLACK)
    draw.rect(screen, CHOCO, Rect(x, y, 50, 30))
    draw.circle(screen, GREEN, (x + 25, y), 15)
    
    display.flip()
    
def move():
    
    global x, y, movex, movey
    
    if evnt.key == K_w:
        screen.fill(BLACK)
        draw.rect(screen, CHOCO, Rect(x, y, 50, 30))
        draw.circle(screen, GREEN, (x + 25, y), 15)
        movey -= 3
        
    if evnt.key == K_a:
        movex -= 3
        
    if evnt.key == K_s:
        screen.fill(BLACK)
        draw.rect(screen, CHOCO, Rect(x, y, 50, 30))
        draw.circle(screen, GREEN, (x + 25, y + 25), 15)
        movey += 3
    if evnt.key == K_d:
        movex += 3

def noMove():
    
    global x, y, movex, movey
            
    if evnt.key == K_w:
        movey = 0
    if evnt.key == K_a:
        movex = 0
    if evnt.key == K_s:
        movey = 0
    if evnt.key == K_d:
        movex = 0
        
def restrict():
    
    global x, y
    
    if x >= 750:
        
        x = 750
        
    if y <= 15:
        
        y = 15
        
    if x <= 0:
        
        x = 0
        
    if y >= 470:
        
        y = 470
        
    

#Main Game Loop
running = 1
myClock = time.Clock()

while running:
    
    mainC()
   
    #screen.fill(BLACK)
    mx, my, mb = getmouse()
    
    for evnt in event.get():
        
        if evnt.type == QUIT:
            running = 0
        if evnt.type == KEYDOWN:
            
            move()
                
        if evnt.type == KEYUP:
            
            noMove()
            
    x += movex
    y += movey 
    
        
    
    restrict()
    
    myClock.tick(60)
    
    
# Exit               
quit()