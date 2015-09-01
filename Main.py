# Name: Jason Wang
# Date: Dec. 23, 2011
# Class: ICS3U1
# Description: Summative - DEFEND YOUR BASE - Simple Shooter Game

# This is a simple shooter game. The objective of the games is for the player to
# survive incoming waves of zombies. The player can access to upgrade their 
# weapons to fight the zombies. There are two types of weapons (SMG & Assault).

# Import modules
import time
import random
import math
from pygame import *

# Initiate Pygame
init()

UPDATE = USEREVENT

# Title of Game displayed on the window
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
GOOP   = (46, 139, 87)
ORANGE = (255, 140, 0)
SILVER = (192, 192, 192)
TURQ   = (0, 100, 0)

#############################################
# Loads All of the Images Used
# -------------------------------------------
# Zombie Picture on Menu
zombiePic = image.load("zombie.png")
shop = image.load("shop.png")

# Weapon Images from Shop
MP7i = image.load("mp7.png")
AK47i = image.load("ak47.png")  

# Wooden Barricade (Full & Broken)
barricade = image.load("wood_barricade.png")
brokenbarricade = image.load("broken_barricade.png")

# Weapon images that player holds
aksmall = image.load("aksmall.png")
mpsmall = image.load("mpsmall.png")
pistolsmall = image.load("pistolsmall.png")

# Blood Splatter
blood = image.load("blood.png")
###############################################

###############################################
# Setting Up Lists and Variables
# ------------------------------------------
# X & Y positiions of bullets
bulletX = []
bulletY = []
bullets = []
increase = []
bulletStart = []
SPEED = 2

# Sets all variables needed for shop and gameplay
cash = 0
weapons = ['Glock34', 'MP7', 'AK47']
ammo    = [18, 30, 40]
damage  = [4, 5, 8]

# If Player has weapon it is True(1), else it is False(0)
glock34 = True
MP7 = True
AK47 = True

# If Player has all the weapons then True means it is equipped or not
pistolE = True
smgE = False
AssaultE = False

# Global variable to move character (x & y positions)
charx = 90
chary = 300
movex = 0
movey = 0

# Player's Hitpoint Level
hp = 5000

# Number of zombies killed
zombiesKilled = 0

# Set Global Variables for the menu, instructions, shop & main game
#menuLoop = True
#menuScreen = 1

shops = False
menuRunning = True
instruction = False
mainGame = False
deadScreen = False

# Fonts
fonts = font.SysFont("Chiller", 45)
fontI = font.SysFont("Chiller", 55)
###############################################

# Method to get mouse positions 
# (Where the mouse moves or where and which button is pressed)
def getmouse():
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()[0]
    return mx, my, mb

# Method that draws the crosshair for weapons
def crosshair():
    
    # White Circle (Outside), Red dot (Inside)
    draw.circle(screen, WHITE, (mx, my), 12, 1)
    draw.circle(screen, RED, (mx, my), 2)

# Death Screen
def dead():
    
    global running, fonts, fontI, zombiesKilled
    
    zombiesKilled = str(zombiesKilled)
    screen.fill(BLACK)
    
    death = fontI.render("Oh Dear! You Are Dead!" , 10, (255, 0, 0))
    screen.blit(death, Rect(200, 90, 0, 0)) 
    
    score = fonts.render("Your Final Score: ", 10, (RED))
    scoreN = fonts.render(zombiesKilled, 10, (RED))
    screen.blit(score, Rect(220, 120, 0, 0))
    
    screen.blit(scoreN, Rect(260, 120, 0, 0))
    
    quits = fonts.render("QUIT" , 10, (255, 0, 0))
    screen.blit(quits, Rect(600, 400, 0, 0)) 
    
    quitbutton = Rect(600, 400, 80, 80)
    
    if quitbutton.collidepoint(mx,my):
        quits = fonts.render("QUIT" , 10, (0, 255, 0))
        screen.blit(quits, Rect(600, 400, 0, 0)) 
            
        if mb == 1:
            running = False
               
    
# Method for the menu screen
def menu():
    
    global menuRunning, instruction, mainGame, fonts
    
    # Will only run if menu is True
    if menuRunning == True:
        
        screen.fill(BLACK)
        
        # Zombie Picture
        screen.blit(zombiePic, Rect(65, 250, 105, 78))
    
        # Game Title
        title = fonts.render("- Defend Your Base -" , 10, (255, 0, 0))
        screen.blit(title, Rect(215, 75, 425, 85))
    
        # Indicator box for start button
        indicatorS = Rect(285, 250, 210, 35)
        start = fonts.render("Start Game" , 10, (255, 0, 0))
        screen.blit(start, Rect(285, 250, 425, 100))

        # Indicator box for instructions button
        indicatorI = Rect(285, 345, 285, 65)
        ins = fonts.render("Instructions" , 10, (255, 0, 0))
        screen.blit(ins, Rect(285, 345, 425, 100))
        
        # Start Game Button
        if indicatorS.collidepoint(mx,my):
            
            start = fonts.render("Start Game" , 10, (GREEN))
            screen.blit(start, Rect(285, 250, 0, 0))
            #draw.rect(screen, WHITE, Rect(285, 255, 150, 45), 1)
            if mb == 1:
                mainGame = True
                menuRunning = False
        
        # Instructions Button
        if indicatorI.collidepoint(mx,my):
            
            ins = fonts.render("Instructions" , 10, (GREEN))
            screen.blit(ins, Rect(285, 345, 0, 0))
            #draw.rect(screen, WHITE, Rect(285, 255, 150, 45), 1)
            if mb == 1:
                menuRunning = False
                instruction = True

# Method for instructions
def instructions():    
    global instruction, mainGame
    # Displays the instructions page if it is True
    if instruction == True:
        
        # Fills Black Screen
        screen.fill(BLACK)
        
        # The standard font size of chiller used in Instructions Page
        fonts = font.SysFont("Chiller", 25)
        
        # Big Font for INSTRUCTIONS Heading
        fontI = font.SysFont("Chiller", 55)
        ins = fontI.render("Instructions" , 10, (255, 0, 0))
        screen.blit(ins, Rect(285, 55, 425, 100))
        
        # Overview of game (3 lines) in the Instructions Page
        one = fonts.render('The Objective of the game is to survive as long as possible.', 10, (255, 0, 0))
        two = fonts.render('Change Weapons with number 1, 2 or 3.', 10, (255, 0, 0))
        three = fonts.render('Win and Survive.', 10, (255, 0, 0))
        screen.blit(one, Rect(160, 150, 425, 100))
        screen.blit(two, Rect(205, 175, 425, 100))
        screen.blit(three, Rect(300, 200, 425, 100))
        
        # Character instructions - Move with WASD
        draw.rect(screen, CHOCO, Rect(105, 300, 50, 30))
        draw.circle(screen, GREEN, (130, 300), 15)
        char = fonts.render("Move Your character with the WASD keys." , 10, (255, 0, 0))
        screen.blit(char, Rect(300, 300, 425, 100))
        
        # Draws the Start Game Button
        start_indicator = Rect(600, 420, 75, 30)
        draw.rect(screen, RED, Rect(600, 420, 75, 30))
        start = fonts.render('START', 10, (BLACK))
        screen.blit(start, Rect(610, 420, 0, 0))
        
        # If mouse moves over button, turns green
        if start_indicator.collidepoint(mx, my):
            start = fonts.render('START', 10, (GREEN))
            screen.blit(start, Rect(610, 420, 0, 0))
            if mb == 1:
                mainGame = True
                instruction = False

# Method for the shop menu
def shopMenu():
    
    global cash, AK47, MP7, shops, shopping, running, mainGame
    
    # If shop Menu is True
    if shops == True:
        
        screen.fill(BLACK)
        
        # The background of the shop menu
        screen.blit(shop, Rect(0, 0, 0, 0))
        
        # Size 25 Chiller Font
        fonts = font.SysFont("Chiller", 25)
        
        # Displays Amount of Cash Player has (bottom left of the screen)
        cashs = str(cash)
        cashA = fonts.render('CASH: $', 10, (WHITE))
        cashB = fonts.render(cashs, 10, (WHITE))
        screen.blit(cashA, Rect(30, 450, 0, 0))
        screen.blit(cashB, Rect(110, 450, 0, 0))
        
        # Big Shop Title
        #fontI = font.SysFont("Chiller", 55)
        ins = fontI.render("Shop" , 10, (255, 0, 0))
        screen.blit(ins, Rect(345, 60, 425, 100))
        
        # Draws the Start Game Button
        start_indicator = Rect(600, 420, 75, 30)
        draw.rect(screen, RED, Rect(600, 420, 75, 30))
        start = fonts.render('START', 10, (BLACK))
        screen.blit(start, Rect(610, 420, 0, 0))
        
        # If collides with START button
        if start_indicator.collidepoint(mx, my):
            start = fonts.render('START', 10, (GREEN))
            screen.blit(start, Rect(610, 420, 0, 0))
            if mb == 1:
                mainGame = True
                
        
        # MP7 Gun Image
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
                    
## Global variable to move character (x & y positions)
#charx = 90
#chary = 300
#movex = 0
#movey = 0

## Hitpoints Level
#hp = 5000

## Number of zombies killed
#zombiesKilled = 0

# Method for Main Character
def mainChar():
    
    global charx, chary, movex, movey, hp, mainGame, deadScreen
    
    # If Hitpoints is less than 0: Game Over    
    if hp <= 0:
        mainGame = False
        deadScreen = True
    
    # Body
    draw.rect(screen, CHOCO, Rect(charx - 25, chary - 25, 30, 50))
    draw.rect(screen, BLACK, Rect(charx - 25, chary - 25, 30, 50), 1)
        
    # Head
    draw.circle(screen, GREEN, (charx, chary), 15)
    draw.circle(screen, BLACK, (charx, chary), 15, 1)
        
# Lists for x and y position of zombies and their health
zombieX = []
zombieY = []
zombieH = []

# Total Number of Zombies
zombieN = 0

# Draws the initial postion of the zombies to the screen
def zombieUpdate():
    
    # Zombie - global variables (related to zombies)
    global zombieN, zombieX, zombieY, zombieH
    # Other global variables
    global charx, chary, hp, bullets, cash, charIndicator, bulletX, bulletY
    
    while zombieN != 5:
        
        # Creates Random Positions that zombies spawn
        rx = random.randint(1, 800)
        ry = random.randint(1, 500) 
        
        # Boundaries
        if 700 < rx < 1000 and 20 < ry < 480:
            
            # Appends zombie Positions to lists
            zombieX.append(rx)
            zombieY.append(ry)
            zombieH.append(10)
            zombieN += 1
             
    ## Loop checks if zombie is hit by bullet
    #for count in range(0, len(zombieX)):
        #if zombieX[count]-20 < bullets[count][0] < zombieX[count]+20 :
            #if zombieY[count]-20 < bullets[count][1] < zombieY[count]+20 : 
                #zombieH[count] -= 1
            
    # Loop that goes through zombie HP list
    for count in range(0, len(zombieH)):
        
        # If zombie has no HP, remove from lists
        if zombieH[count] <= 0:
            zombieX.remove(zombieX[count])
            zombieY.remove(zombieY[count])
            cash += 100
           
    randoms = random.randint(0, 2)
    
    # If Top Barricade is False (Not There)
    if barricadeV[0] == False:
        for count in range(0, len(zombieX)):
            if 0 < zombieY[count] < 500:
                if zombieX[count] <= 210:
                    if zombieX[count] == charx and zombieY[count] == chary:
                        hp -= 1
                    if zombieX[count] > charx:
                        zombieX[count] -= randoms
                    if zombieX[count] < charx:
                        zombieX[count] += randoms
                    if zombieY[count] > chary:
                        zombieY[count] -= randoms
                    if zombieY[count] < chary:
                        zombieY[count] += randoms
                        
    # If Top Barricade is True (There)             
    if barricadeV[0] == True:
        for count in range(0, len(zombieX)):
            randomy = random.randint(-3, 3)
            if zombieX[count] > 210:
                zombieX[count] -= randoms
            if zombieY[count] < 0 or zombieY[count] < 500:
                zombieY[count] -= 0
                
    # If Middle Barricade is False             
    if barricadeV[1] == False:
        for count in range(0, len(zombieX)):
            if 0 < zombieY[count] < 500: 
                if zombieX[count] <= 210:
                    if zombieX[count] == charx and zombieY[count] == chary:
                        hp -= 1
                    if zombieX[count] > charx:
                        zombieX[count] -= randoms
                    if zombieX[count] < charx:
                        zombieX[count] += randoms
                    if zombieY[count] > chary:
                        zombieY[count] -= randoms
                    if zombieY[count] < chary:
                        zombieY[count] += randoms
                        
    # If Middle Barricade is True                     
    if barricadeV[1] == True:
        for count in range(0, len(zombieX)):
            randomy = random.randint(-3, 3)
            if zombieX[count] > 210:
                zombieX[count] -= randoms
            if zombieY[count] < 0 or zombieY[count] < 500:
                zombieY[count] -= 0
                
    # If Bottom Barricade is False              
    if barricadeV[2] == False:
        for count in range(0, len(zombieX)):
            if 0 < zombieY[count] < 500: 
                if zombieX[count] <= 210:
                    if zombieX[count] == charx and zombieY[count] == chary:
                        hp -= 1
                    if zombieX[count] > charx:
                        zombieX[count] -= randoms
                    if zombieX[count] < charx:
                        zombieX[count] += randoms
                    if zombieY[count] > chary:
                        zombieY[count] -= randoms
                    if zombieY[count] < chary:
                        zombieY[count] += randoms
                        
    # If Bottom Barricade is True                      
    if barricadeV[2] == True:
        for count in range(0, len(zombieX)):
            randomy = random.randint(-3, 3)
            if zombieX[count] > 210:
                zombieX[count] -= randoms
            if zombieY[count] < 0 or zombieY[count] < 500:
                zombieY[count] -= 0

# Updates the zombie images by drawing them
def zombieDraw():                            
    
    global zombieX, zombieY, spawn, count, shops, mainGame
    
    #if spawn == 10:
        
        ## Body
        #draw.rect(screen, CHOCO, Rect(zombieX[count], zombieY[count] - 20, 20, 40))
        #draw.rect(screen, BLACK, Rect(zombieX[count], zombieY[count] - 20, 20, 40), 1)
        
        ## Arms
        #draw.rect(screen, GOOP, Rect(zombieX[count] - 20, zombieY[count] - 20, 20, 10))
        #draw.rect(screen, BLACK, Rect(zombieX[count] - 20, zombieY[count] - 20, 20, 10), 1)
        #draw.rect(screen, GOOP, Rect(zombieX[count] - 20, zombieY[count] + 10, 20, 10))
        #draw.rect(screen, BLACK, Rect(zombieX[count] - 20, zombieY[count] + 10, 20, 10), 1)

        ## Head
        #draw.circle(screen, GREEN, (zombieX[count], zombieY[count]), 12)
        #draw.circle(screen, BLACK, (zombieX[count], zombieY[count]), 12, 1)

    for count in range(0, len(zombieX)):
    
        # Body
        draw.rect(screen, CHOCO, Rect(zombieX[count], zombieY[count] - 20, 20, 40))
        draw.rect(screen, BLACK, Rect(zombieX[count], zombieY[count] - 20, 20, 40), 1)
        
        # Arms
        draw.rect(screen, GOOP, Rect(zombieX[count] - 20, zombieY[count] - 20, 20, 10))
        draw.rect(screen, BLACK, Rect(zombieX[count] - 20, zombieY[count] - 20, 20, 10), 1)
        draw.rect(screen, GOOP, Rect(zombieX[count] - 20, zombieY[count] + 10, 20, 10))
        draw.rect(screen, BLACK, Rect(zombieX[count] - 20, zombieY[count] + 10, 20, 10), 1)

        # Head
        draw.circle(screen, GREEN, (zombieX[count], zombieY[count]), 12)
        draw.circle(screen, BLACK, (zombieX[count], zombieY[count]), 12, 1)
        
    #if zombiesKilled >= 10:
        #mainGame = False
        
        #shops = True
        
# List for position of barricades and the health 
# Positions (Top , Middle, Bottom)
barricadePos = [[150, 0], [150, 200], [150, 400]]
barricadeV = [True, True, True]
barricadeH = [5000, 5000, 5000]

# Method to Update Barricade Positions     
def BarricadeUpdate():
    
    global barricadeH, zombieX, zombieY, barricadePos, barricadeV
    
    for count in range(0, len(zombieX)):
        
        # If zombie is at position health - 1
        if zombieX[count] - 25 < barricadePos[0][0]+42:
            barricadeH[0] -= 1
        
        # If health == 0 barricade is False
        if barricadeH[0] == 0:
            barricadeV[0] = False
            
        # If zombie is at position health - 1    
        if zombieX[count] - 25 < barricadePos[1][0]+42:
            barricadeH[1] -= 1
            
        # If health == 0 barricade is False   
        if barricadeH[1] == 0:
            barricadeV[1] = False
            
        # If zombie is at position health - 1    
        if zombieX[count] - 25 < barricadePos[2][0]+42:
            barricadeH[2] -= 1
            
        # If health == 0 barricade is False    
        if barricadeH[2] == 0:
            barricadeV[2] = False 

# Method that Draws Barricades
def Barricade():
    
    global barricadeH, zombieX, zombieY, barricadePos, barricadeV
    
    # Top Barricade
    if barricadeV[0] == True:
        if barricadeH[0] <= 2500:
            screen.blit(brokenbarricade, Rect(barricadePos[0][0], barricadePos[0][1], 0, 0))
        else:
            screen.blit(barricade, Rect(barricadePos[0][0], barricadePos[0][1], 0, 0))
            
    # Middle Barricade       
    if barricadeV[1] == True: 
        if barricadeH[1] <= 2500:
            screen.blit(brokenbarricade, Rect(barricadePos[1][0], barricadePos[1][1], 0, 0))
        else:
            screen.blit(barricade, Rect(barricadePos[1][0], barricadePos[1][1], 0, 0))
            
    # Bottom Barricade       
    if barricadeV[2] == True:   
        if barricadeH[2] <= 2500:
            screen.blit(brokenbarricade, Rect(barricadePos[2][0], barricadePos[2][1], 0, 0))
        else:
            screen.blit(barricade, Rect(barricadePos[2][0], barricadePos[2][1], 0, 0))

# Check which weapon is equipped
def weaponEquip():
    
    global pistolE, smgE, AssaultE, glock34, MP7, AK47
    
    key_pressed = key.get_pressed()
    
    # If 1 is pressed == Pistol
    if key_pressed[K_1]:
        if glock34 == True:
            
            pistolE = True
            smgE = False
            AssaultE = False
    
    # If 2 is pressed == MP5
    elif key_pressed[K_2]:
        if MP7 == True:
            
            pistolE = False
            smgE = True
            AssaultE = False
            
    # If 3 is pressed == AK47    
    elif key_pressed[K_3]:
        if AK47 == True:
            
            pistolE = False
            smgE = False
            AssaultE = True
            
# Method that draws weapons
def weaponDraw():
    
    global pistolE, smgE, AssaultE, charx, chary
    
    # If pistol is equipped
    if pistolE == True:
        screen.blit(pistolsmall, Rect(charx, chary + 15, 45, 10))
    
    # If MP5 is equipped
    if smgE == True:
        screen.blit(mpsmall, Rect(charx, chary + 15, 45, 10))
    
    # If AK47 is equipped
    if AssaultE == True:  
        screen.blit(aksmall, Rect(charx, chary + 15, 45, 10))

# Method that updates bullet Positions
def bulletUpdate():
    
    global SPEED, bulletStart, bullets
    
    if mb == 1:
        bullets.append([mx, my])
        bulletStart.append([charx, chary])
    
    for count in range(0, len(bullets)):
        changeX = bullets[count][0] - bulletStart[count][0] # x2 - x1
        changeY = bullets[count][1] - bulletStart[count][1] # y2 - y1
        
        radian = math.atan2(changeY,changeX) # angle in radians
        #radian = math.atan2(changeX,changeY) 
            
        xplus = round(math.cos(radian)*SPEED) # Increase of X
        yplus = round(math.sin(radian)*SPEED) # Increase of Y
        xplus = int(xplus)
        yplus = int(yplus)
        
        if bullets[count][0] < 800 and bullets[count][1] != 800 or bullets[count][1] != -100:
            bulletStart[count][0]+= xplus # adds X
            bulletStart[count][1]+= yplus # adds Y
                
# Method that draws bullets
def bullet():
    
    global bulletX, bulletY
    
    # Draws out all the bullets in the bullets List
    for count in range(0, len(bullets)):
        draw.rect(screen, WHITE, Rect(bulletStart[count][0], bulletStart[count][1], 2, 2))
              
# Draws the background for Main Game Loop        
def drawScene():
    screen.fill(TURQ)

# Method for Main Game events
def main():
    
    global mainGame, cash, weapons, ammo, damage, glock34, MP7, AK47, hp, zombiesKilled
    
    if mainGame == True:
        
        # Set Mouse to invisible
        mouse.set_visible(False)
        
        # Updates everything here
        bulletUpdate()
        BarricadeUpdate()
        weaponEquip()
        zombieUpdate()
        
        # Goes through zombie X pos List
        for count in range(0, len(zombieX)):
            zombieIndicator = Rect(zombieX[count] - 20, zombieY[count] - 20, 40, 40)
        charIndicator = Rect(charx - 25, chary - 25, 30, 50)
        
        # IF character colides with zombie, he loses HP
        if charIndicator.colliderect(zombieIndicator):
            hp -= 1
            draw.rect(screen, BLACK, Rect(200, 400, 100, 100))
        
        # If bullet collides with zombies
        for count in range(0, len(bullets)):
            bulletIndicator = Rect(bullets[count][0], bullets[count][1], 2, 2)
            
        # Add cash, add zombiesKilled
        if bulletIndicator.colliderect(zombieIndicator):
            zombiesKilled += 1
            cash += 200
            print zombiesKilled
                
        # Fill Screen Here
        drawScene()
        
        # Draws everything to screen
        weaponDraw()
        Barricade()
        zombieDraw()
        bullet()
        mainChar()
        crosshair()

#Main Game Loop
running = 1
myClock = time.Clock()
    
while running:
    
    # Get Mouse Buttons
    mx, my, mb = getmouse()
    
    for evnt in event.get():
        if evnt.type == QUIT:
            running = 0
            
        if evnt.type == KEYDOWN:
        
            if evnt.key == K_w:
                movey -= 4
            if evnt.key == K_a:
                movex -= 4
            if evnt.key == K_s:
                movey += 4
            if evnt.key == K_d:
                movex += 4
                
        if evnt.type == KEYUP:
                
            if evnt.key == K_w:
                movey = 0
            if evnt.key == K_a:
                movex = 0
            if evnt.key == K_s:
                movey = 0
            if evnt.key == K_d:
                movex = 0
                
    if charx >= 130:
      
        charx = 130
          
    if chary <= 25:
          
        chary = 25
          
    if charx <= 30:
        
        charx = 30
        
    if chary >= 470:
        
        chary = 470
        
    charx += movex
    chary += movey
    
    if menuRunning == True:
        menu()
    if instruction == True:
        instructions()
    if mainGame == True:
        main()
    if shops == True:
        mouse.set_visible(True)
        shopMenu()
    if deadScreen == True:
        mouse.set_visible(True)
        dead()
    
    myClock.tick(60)
    display.flip()
    
# Exit               
quit()