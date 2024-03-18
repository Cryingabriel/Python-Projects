from random import randint as rr
from random import random as r
import pygame
from pygame.math import Vector2

pygame.init()
screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
mouse = False
mousepos = Vector2(500,500)
color = (rr(0,255),rr(0,255),rr(0,255))
runningawujdbqaidbaiwd = True
mouseDown = False
level = [[0 for i in range(200)] for j in range(200)]
font = pygame.font.Font('freesansbold.ttf', 5)
text = font.render('0', True, (255,255,255))
pygame.event.set_grab(True)
print(level)



while runningawujdbqaidbaiwd:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningawujdbqaidbaiwd = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False

        if event.type == pygame.MOUSEMOTION:
            mousepos = Vector2(event.pos)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                runningawujdbqaidbaiwd = False

    #UPDATE------------------------------------------------------------------------------------------
    if mouseDown == True:

        level[int(mousepos.y/5)][int(mousepos.x/5)]=1
        level[int(mousepos.y/5)][int((mousepos.x/5)-1)]=1
        level[int(mousepos.y/5)][int((mousepos.x/5)-2)]=1

        level[int((mousepos.y/5)-1)][int(mousepos.x/5)]=1
        level[int((mousepos.y/5)-2)][int((mousepos.x/5)-1)]=1
        level[int((mousepos.y/5)-3)][int((mousepos.x/5)-2)]=1
        # print(mousepos.x/5)

    for w in range(len(level)):
        for k in range(len(level[w])):
            if w < len(level)-1:
                if level[w][k]==1 and level[w+1][k] == 0:
                    level[w][k]=0
                    level[w+1][k]=1
            if r() < 0.5:
                if w < len(level)-1 and k > 0 and k < len(level)-1:
                    if level[w][k]==1 and level[w+1][k] == 1:
                        if r() < 0.5:
                            if level[w][k+1] == 0:
                                level[w][k]=0
                                level[w][k+1]=1
                        else:
                            if level[w][k-1] == 0:
                                level[w][k]=0
                                level[w][k-1]=1

    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                # pygame.draw.circle(screen,(255,255,255),(j*5,i*5),2)
                screen.blit(text, (j*5,i*5))
            else:
                pygame.draw.rect(screen,(0,0,0),(j*5,i*5,3,6))

    pygame.display.flip()
pygame.quit()