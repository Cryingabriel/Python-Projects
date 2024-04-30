import pygame
from pygame.math import Vector2
from idlegame import screen
class Player():
    def __init__(self,xpos,ypos):
        self.pos = Vector2(xpos,ypos)
        self.health = 100
        self.attack = 10
    def draw(self):
        pygame.draw.circle(screen,(255,255,255), (800,400),10)