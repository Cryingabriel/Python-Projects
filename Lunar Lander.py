import pygame
pygame.init()

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20,20)

#-----------------------------------------------
screen = pygame.display.set_mode((700, 1000))
pygame.display.set_caption("Lunar Lander Simulator")
# Game Variabels
Exit = False
clock = pygame.time.Clock()



#Images 
#@star = pygame.image.load('')

# Player Variables
xpos = 350
ypos = 0
pvx = 0
pvy = .10
isground = False
Rocketon = False
Crashed = False
meft = False
might = False
mup = False

# Font Variables
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
text1 = font.render('Vertical velocity:', False , (0, 200, 200))
text2 = font.render(str(int(pvy)), 1 , (0, 200, 200))
text3 = font.render('You Crashed!', False, (200, 50, 50))
text4 = font.render('Vertical velocity:', False, (200, 20, 20))
text5 = font.render(str(int(pvy)), 1 , (200, 20, 20))
text6 = font.render('Height', False, (20, 20, 200))
text7 = font.render(str(int(ypos)), 1 , (20, 20, 200))


# Game Loop___________________________________________________________________________________________
while Exit == False:
    clock.tick(60)
    #replace with keys.get
    meft = False
    might = False
    mup = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                meft = True
            if event.key == pygame.K_RIGHT:
                might = True
            if event.key == pygame.K_UP:
                mup = True

   
   
   
   
   #___________Physics Section_____________________________
   
   
    if meft == True:
        pvx -= 3
    if might == True:
        pvx += 3
    else:
        pvx = 0
    if mup == True:
        pvy -= 4.17/60
        isground = False
        Rocketon = True

    else:
        if isground == False:
            pvy += 1.65/60
        Rocketon = False


    if isground == True and abs(pvy) > .5:
        Crashed = True
        xpos = 350
        ypos = 0
        pvx = 0
        pvy = 0
        isground = False
    
    if isground == True and abs(pvy) < .5:
        Crashed = False
        pvy = 0
        pvx = 0
    
    if ypos >950:
        isground = True
        ypos = 950


    #______________Update Section__________________________________________
    #Updated Player
    xpos += pvx
    ypos += pvy
    #Updated Printed Velocity
    text2 = font.render(str("%.2f" %(pvy*-1)), 1, (0, 200, 200))
    text5 = font.render(str("%.2f" %(pvy*-1)), 1, (200, 20, 20))
    #Updated Printed Height
    text6 = font.render('Height:', False, (20, 20, 200))
    text7 = font.render(str(int(1000-pvy)), 1, (0, 200, 200))

    
#_________Render Section____________________________________
    screen.fill((0,0,0))
    if Crashed == True:
        screen.blit(text3, (200,500))
        pygame.display.flip()
        pygame.time.wait(1000)
    
    if abs(pvy) < .5:
        screen.blit(text1, (10, 10))
        screen.blit(text2, (250, 10))
    else:
        screen.blit(text4, (10, 10))
        screen.blit(text5, (250, 10))
    screen.blit(text6, (10, 60))
    screen.blit(text7, (150, 60))

    pygame.draw.rect(screen, (200, 200 ,200), (xpos, ypos, 50 ,50))

    pygame.display.flip()


    
pygame.quit()