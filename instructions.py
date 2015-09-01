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
WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
GREEN  = (0, 255, 0)
RED    = (255, 0, 0)
CHOCO  = (139, 69, 19)
YELLOW = (255, 255, 0)

def getmouse():
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()[0]
    return mx, my, mb

def instructions():
    
    # Fill Black Screen
    screen.fill(BLACK)
    
    # Size 25 Chiller Font
    fonts = font.SysFont("Chiller", 25)
    
    # Big INSTRUCTIONS Title
    fontI = font.SysFont("Chiller", 55)
    ins = fontI.render("Instructions" , 10, (255, 0, 0))
    screen.blit(ins, Rect(285, 55, 425, 100))
    
    # Short Description of the game 
    one = fonts.render('The Objective of the game is to survive as long as possible.', 10, (255, 0, 0))
    two = fonts.render('Collect coins from zombies that you have killed.', 10, (255, 0, 0))
    three = fonts.render('At the end of each wave you can access the shop for upgrades.', 10, (255, 0, 0))
    screen.blit(one, Rect(160, 150, 425, 100))
    screen.blit(two, Rect(205, 175, 425, 100))
    screen.blit(three, Rect(150, 200, 425, 100))
    
    # Draws the Character
    draw.rect(screen, CHOCO, Rect(105, 300, 50, 30))
    draw.circle(screen, GREEN, (130, 300), 15)
    
    # Short Sentence of How to Move the Character
    char = fonts.render("Move Your character with the WASD keys." , 10, (255, 0, 0))
    screen.blit(char, Rect(300, 300, 425, 100))
    
    # Draws the Start Game Button
    draw.rect(screen, RED, Rect(600, 420, 75, 30))
    start = fonts.render('START', 10, (0, 0, 0))
    screen.blit(start, Rect(610, 420, 100, 30))
    display.flip()
    

running = 1
myClock = time.Clock()

while running:
    
    # Method for Mouse Movement
    mx, my, mb = getmouse()
    
    # Event Checking Loop
    for evnt in event.get():
        if evnt.type == QUIT:
            running = 0
            
    instructions()       

# Exits
quit()