import pygame
pygame.init()  
pygame.display.set_caption('adding image')  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop


#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3


link = pygame.image.load('boxpep.png')

framewidth = 20
frameheight = 40
rownum = 0
framenum = 0
ticker = 0

#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform



class Goomba():
    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
        self.direction = 1
    
    def move(self, time):
        if ticker % 100==0:
            self.xpos+= 50*self.direction
        return time
        




while gameover == False:
    clock.tick(60) #FPS
    ticker += 1
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
    #collision
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




    #physics Section
    

     
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



    #Render section
    screen.fill((0,0,0))

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



    screen.blit(link, (xpos, ypos), (framewidth*framenum, rownum*frameheight, framewidth, frameheight))


    pygame.display.flip()#this actually puts the pixel on the screen