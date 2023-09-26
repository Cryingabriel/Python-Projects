import pygame
import math
import random

pygame.init()
pygame.display.set_caption("Slither")
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()



#Game Variables
gover = False


#Player Variables
xpos = 400
ypos = 400
vx = 1
vy = 1



class pellet:
    def __init__(self, xpos, ypos, red, green, blue, radius):
        self.xpos = xpos
        self.ypos = ypos
        self.red = red
        self.green = green
        self.blue = blue
        self.radius = radius
    
    def draw(self):
        pygame.draw.circle(screen, (self.red, self.green, self.blue), (self.xpos, self.ypos), self.radius)



p1 = pellet(200, 50, 100, 20, 220, 10)

while not gover:

    #Event Section
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gover = True

        if event.type == pygame.MOUSEMOTION:
            mousepos = event.pos
            if mousepos[0] > xpos:
                vx = 1
            elif mousepos[0] < xpos:
                vx = -1
            
            if mousepos[1] > ypos:
                vy = 1
            elif mousepos[1] < ypos:
                vy = -1


    #Physics Section

    xpos += vx
    ypos += vy
    #Render Section
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (200, 0, 200), (xpos, ypos), 10)
    p1.draw()

    pygame.display.flip()
pygame.quit()