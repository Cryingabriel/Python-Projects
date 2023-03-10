import pygame
pygame.init()  
pygame.display.set_caption('adding image')  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

pixel = pygame.transform.scale(pygame.image.load("pixilart-drawing.png"), (100,100))

link = pygame.image.load('boxpep.png')
link.set_colorkey((200,0,255))
enemyi = pygame.image.load('enemy.png')
enemyi.set_colorkey((200,0,200))
#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3

#animation variables
framewidth = 20
frameheight = 40
rownum = 0
framenum = 0
ticker = 0

framewidth1 = 20
frameheight1 = 30
rownum1 = 0
framenum1 = 0
ticker1 = 0

#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform
health = 100
#enemy variables
enemy1=[200, 620, 0]
enemy2 = [400,420,0]
enemy3 = [500,320,0]
def enmove(enemyinfo):
    enemyinfo[2] +=1
    if enemyinfo[2]<=80:
        enemyinfo[0]+=1
    elif enemyinfo[2]<=160:
        enemyinfo[0]-=1
    else:
        enemyinfo[2] = 0 #resetting timer
    
def enmove2(enemyinfo2):
    enemyinfo2[2] +=1
    if enemyinfo2[2]<=40:
        enemyinfo2[0]+=2
    elif enemyinfo2[2]<=80:
        enemyinfo2[0]-=2
    else:
        enemyinfo2[2] = 0
def enmove3(enemyinfo3):
    enemyinfo3[2] +=1
    if enemyinfo3[2]<=20:
        enemyinfo3[0]+=4
    elif enemyinfo3[2]<=40:
        enemyinfo3[0]-=4
    else:
        enemyinfo3[2] = 0
        
def enemyC(enemyinfo, xpos, ypos):
    if xpos +20> enemyinfo[0]: #right of player and leftside of enemy 
        if xpos < enemyinfo[0]+20: #left of player and right of enemy
            if ypos < enemyinfo[1]+20: #top of the player and bottom of the the enemy
                if ypos+20 > enemyinfo[1]: #bottom of the player and top of the enemy
                    return True
    else:
        return False

def enemyC2(enemyinfo2, xpos, ypos):
    if xpos +20> enemyinfo2[0]: #right of player and leftside of enemy 
        if xpos < enemyinfo2[0]+20: #left of player and right of enemy
            if ypos < enemyinfo2[1]+20: #top of the player and bottom of the the enemy
                if ypos+20 > enemyinfo2[1]: #bottom of the player and top of the enemy
                    return True
    else:
        return False
def enemyC3(enemyinfo3, xpos, ypos):
    if xpos +20> enemyinfo3[0]: #right of player and leftside of enemy 
        if xpos < enemyinfo3[0]+20: #left of player and right of enemy
            if ypos < enemyinfo3[1]+20: #top of the player and bottom of the the enemy
                if ypos+20 > enemyinfo3[1]: #bottom of the player and top of the enemy
                    return True
    else:
        return False

#
jump = pygame.mixer.Sound('jump.wav')#load in sound effect
music = pygame.mixer.music.load('believe-in-miracle.mp3')#load in background music
pygame.mixer.music.play(-1)#start background music
#Controller Input
controller = pygame.joystick.Joystick(0) 
controller.init()


while not gameover and health > 0: #GAME LOOP############################################################
    clock.tick(60) #FPS
    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True

            elif event.key == pygame.K_UP:
                keys[UP]=True
            
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False

            elif event.key == pygame.K_UP:
                keys[UP]=False
            
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False


    #physics section--------------------------------------------------------------------
    #Player Movement
    xvel = controller.get_axis(0)
    yvel = controller.get_axis(1)
    cxvel = controller.get_axis(0)
    cyvel = controller.get_axis(1)
    if keys[LEFT]==True:
        vx=-3
        direction = LEFT    
    elif keys[RIGHT]==True:
        vx=3
        direction = RIGHT
        #JUMPING
    elif keys[UP] == True and isOnGround == True:
        vy = -8
        isOnGround = False
        direction = UP
    #turn off velocity
    else:
        vx = 0
    
    xpos += int(xvel * 10)
    ypos += int(yvel * 10)
    enmove(enemy1) 

    enmove(enemy2) 

    enmove(enemy3)

    #enemy collision
    if enemyC(enemy1,xpos,ypos) == True:
        print("hit")
        health-=1
        print(health)
    if enemyC2(enemy2,xpos,ypos) == True:
        print("hit")
        health-=1
        print(health)
    if enemyC3(enemy3,xpos,ypos) == True:
        print("hit")
        health-=1
        print(health)
    #COLLISION
    if xpos>100 and xpos<200 and ypos+40 >750 and ypos+40 <770:
        ypos = 750-40
        isOnGround = True
        vy = 0
    elif xpos>200 and xpos<300 and ypos+40 >650 and ypos+40 <670:
        ypos = 650-40
        isOnGround = True
        vy = 0
    elif xpos>300 and xpos<400 and ypos+40 >550 and ypos+40 <570:
        ypos = 550-40
        isOnGround = True
        vy = 0
    elif xpos>400 and xpos<500 and ypos+40 >450 and ypos+40 <470:
        ypos = 450-40
        isOnGround = True
        vy = 0
    elif xpos>500 and xpos<600 and ypos+40 >350 and ypos+40 <370:
        ypos = 350-40
        isOnGround = True
        vy = 0
    elif xpos<=0:
        xpos = 0
    elif xpos+20>=800:
        xpos = 800-20
    elif ypos <=0:
        ypos = 0
        yvel = 0
    else:
        isOnGround = False


    
    #stop falling if on bottom of game screen
    if ypos > 760:
        isOnGround = True
        vy = 0
        ypos = 760
    
    #gravity
    if isOnGround == False:
        vy+=.2 #notice this grows over time, aka ACCELERATION
    

    #update player position
    xpos+=vx 
    ypos+=vy
    
    if vx < 0:
        ticker+=1
        if ticker%10==0:
            rownum = 1
            framenum+=1
        if framenum > 6:
            framenum = 0
    if vx > 0:
        ticker+=1
        if ticker%10==0:
            rownum = 0
            framenum+=1
        if framenum > 6:
            framenum = 0
    if vy < 0:
        ticker+=1
        if ticker%10==0:
            rownum = 2
            framenum+=1
        if framenum > 6:
            framenum = 0
    if vy > 0:
        ticker+=1
        if ticker%10==0:
            rownum = 3
            framenum+=1
        if framenum > 6:
            framenum = 0
    if enemy1[0] > 0:
        ticker1+=1
        if ticker1%10==0:
            rownum1 = 0
            framenum1+=1
        if framenum1 > 6:
                framenum1=0
    if enemy1[0] < 0:
        ticker1+=1
        if ticker1%10==0:
            rownum1 = 1
            framenum1+=1
        if framenum1 > 6:
                framenum1=0
    if enemy2[0] > 0:
        ticker1+=1
        if ticker1%10==0:
            rownum1 = 0
            framenum1+=1
        if framenum1 > 6:
                framenum1=0
    if enemy2[0] < 0:
        ticker1+=1
        if ticker1%10==0:
            rownum1 = 1
            framenum1+=1
        if framenum1 > 6:
                framenum1=0
    if enemy3[0] > 0:
        ticker1+=1
        if ticker1%10==0:
            rownum1 = 0
            framenum1+=1
        if framenum1 > 6:
                framenum1=0
    if enemy3[0] < 0:
        ticker1+=1
        if ticker1%10==0:
            rownum1 = 1
            framenum1+=1
        if framenum1 > 6:
                framenum1=0
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    font = pygame.font.Font(None, 74)
    text = font.render(str(health), 1, (255,255,0))
    screen.blit(text, (250,10))
    #player
    #enemies=
    #first platform
    pygame.draw.rect(screen, (200, 0, 100), (100, 750, 100, 20))
    
    #second platform
    pygame.draw.rect(screen, (100, 0, 200), (200, 650, 100, 20))
    
    #third platform
    pygame.draw.rect(screen, (255, 40, 120), (300, 550, 100, 20))
    
    #fourth platform
    pygame.draw.rect(screen, (200, 100, 120), (400, 450, 100, 20))
    
    #fith platform
    pygame.draw.rect(screen, (135, 80, 250), (500, 350, 100, 20))
    
    screen.blit(pixel, (0,100))
    screen.blit(link, (xpos, ypos), (framewidth*framenum, rownum*frameheight, framewidth, frameheight))
    screen.blit(enemyi, (enemy1[0], enemy1[1]), (framewidth1*framenum1, rownum1*frameheight1, framewidth1, frameheight1))
    screen.blit(enemyi, (enemy2[0], enemy2[1]), (framewidth1*framenum1, rownum1*frameheight1, framewidth1, frameheight1))
    screen.blit(enemyi, (enemy3[0], enemy3[1]), (framewidth1*framenum1, rownum1*frameheight1, framewidth1, frameheight1))
    pygame.display.flip()#this actually puts the pixel on the screen
    
    

#end game loop------------------------------------------------------------------------------
if health <= 0:
    print("you've died")
pygame.quit()