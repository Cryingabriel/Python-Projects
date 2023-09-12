import pygame
#Constants
screens = (700,500)
color = (100,100,100)
#init
pygame.init()
screen = pygame.display.set_mode(screens)
pygame.display.set_caption("plat")

gover = False

while not gover:






    screen.fill(color)
    pygame.display.flip()
pygame.quit()