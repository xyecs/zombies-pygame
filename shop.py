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

AK47 = 0
MP7 = 0
cash = 1000

# Method for the shop menu
def shopMenu():
    
    global cash, AK47, MP7
    
    # The background of the shop menu
    shop = image.load("shop.png")
    screen.blit(shop, Rect(0, 0, 800, 500))
    
    # Size 25 Chiller Font
    fonts = font.SysFont("Chiller", 25)
    
    # Displays Amount of Cash Player has (bottom left of the screen)
    cashs = str(cash)
    cashA = fonts.render('CASH: $', 10, (WHITE))
    cashB = fonts.render(cashs, 10, (WHITE))
    screen.blit(cashA, Rect(30, 450, 0, 0))
    screen.blit(cashB, Rect(110, 450, 0, 0))
    
    # Big Shop Title
    fontI = font.SysFont("Chiller", 55)
    ins = fontI.render("Shop" , 10, (255, 0, 0))
    screen.blit(ins, Rect(345, 60, 425, 100))
    
    # Draws the Start Game Button
    start_indicator = Rect(600, 420, 75, 30)
    draw.rect(screen, RED, Rect(600, 420, 75, 30))
    start = fonts.render('START', 10, (BLACK))
    screen.blit(start, Rect(610, 420, 0, 0))
    
    if start_indicator.collidepoint(mx, my):
        start = fonts.render('START', 10, (GREEN))
        screen.blit(start, Rect(610, 420, 0, 0))
        if mb == 1:
            mainGame = 1
            shopMenu = 0
    
    # MP7 Gun Image
    MP7i = image.load("mp7.png")
    screen.blit(MP7i, Rect(140, 140, 0, 0))
    draw.rect(screen, WHITE, Rect(140, 140, 180, 90), 1)
    
    # MP7 Buy Button + Cost
    buyindicatorM = Rect(340, 200, 100, 30)
    buyMP7 = fonts.render('BUY    $1000', 10, (WHITE))
    screen.blit(buyMP7, Rect(340, 200, 100, 30))
    
    # If the Player does not have a MP7
    if MP7 == 0:
        
        # If mouse moves over BUY, the button turns red
        if buyindicatorM.collidepoint(mx,my):
            buyMP7 = fonts.render('BUY    $1000', 10, (RED))
            screen.blit(buyMP7, Rect(340, 200, 0, 0))
        
            # If BUY button is pressed with mouse left-click, MP7 is True
            # meaning the player now has an mp7
            if mb == 1 and cash >= 1000:
                MP7 = 1
                cash -= 1000
            
    # AK - 47 Gun Image
    AK47i = image.load("ak47.png")
    screen.blit(AK47i, Rect(140, 255, 0, 0))
    draw.rect(screen, WHITE, Rect(140, 255, 180, 90), 1)
    
    # AK - 47Buy Button + Cost
    buyindicatorA = Rect(340, 315, 100, 30)
    buyAK = fonts.render('BUY    $5000', 10, (WHITE))
    screen.blit(buyAK, Rect(340, 315, 0, 0))
    
    # If the Player does not have an AK - 47
    if AK47 == 0:
        # If mouse moves over BUY, the button turns red
        if buyindicatorA.collidepoint(mx,my):
            buyAK = fonts.render('BUY    $5000', 10, (RED))
            screen.blit(buyAK, Rect(340, 315, 0, 0))
        
            # If BUY button is pressed with mouse left-click, AK47 is True
            # meaning the player now has an ak
            if mb == 1 and cash >= 5000:
                AK47 = 1
                cash -= 5000
    
    
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
            
    shopMenu()       
   
quit()
