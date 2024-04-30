import pygame
import math
import random
from random import randrange as rr
from pygame.math import Vector2

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("2024 Project")




gameloop = True


while gameloop == True:
    #Inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit = True
    #Render section
    screen.fill((0,0,0))
pygame.quit()
