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

# Player Variables
xpos = 350
ypos = 0
pvx = 0
pvy = -10
isground = False
Rocketon = False
Crashed = False

# Font Variables
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
text1 = font.render('Vertical velocity:', False , (0, 200, 200))
text2 = font.render(str(int(pvy)), 1 , (0, 200, 200))
text3 = font.render('You Crashed!', False, (200, 50, 50))
text4 = font.render('Vertical velocity:', False, (200, 20, 20))
text5 = font.render(str(int(pvy)), 1 , (200, 20, 20))
text6 = font.render('Height', False, (20, 20, 200))
text4 = font.render(str(int(ypos)), 1 , (20, 20, 200))


# Game Loop___________________________________________________________________________________________
while Exit == False:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit = True
    pygame.quit()