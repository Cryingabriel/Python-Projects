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

    def collide(self, x, y):
        if math.sqrt((self.xpos - x)**2+(self.ypos - y)**2) < (self.radius+5):
            self.xpos = random.randrange(0, 800)
            self.ypos = random.randrange(0, 800)
            self.red = random.randrange(0, 255)
            self.green = random.randrange(0, 255)
            self.blue = random.randrange(0, 255)
            self.radius = random.randrange(0, 30)
            return True

#pellet crap
pelletnum = 20
pelletbag = list()
for i in range(pelletnum):
    pelletbag.append(pellet(random.randrange(0, 800), random.randrange(0, 800), random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 30)))

#tail code
class tailseg():
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    
    def update(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    
    def draw(self):
        r = random.randrange(0, 255)
        g = random.randrange(0, 255)
        b = random.randrange(0, 255)
        pygame.draw.circle(screen, (r, g, b), (self.xpos, self.ypos), 10)

tailcrap = list()

oldx = 400
oldy = 400
counter = 0
mousepos = (0, 0)

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and mousepos[0] > xpos:
                vx = 2.2
            elif event.key == pygame.K_SPACE and mousepos[0] < xpos:
                vx = -2.2
            if event.key == pygame.K_SPACE and mousepos[1] > ypos:
                vy = 2.2
            if event.key == pygame.K_SPACE and mousepos[1] < ypos:
                vy = -2.2
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                vx = 1
                vy = 1


    #Physics Section

    counter+=1 #update counter
    if counter == 20: #create a delay so the segments follow behind
        counter = 0 #reset counter every 20 ticks
        oldx = xpos #hold onto the old player position from 20 ticks ago
        oldy = ypos

        if (len(tailcrap) > 1): #don't push the numbers if there are no nodes yet
            for i in range(len(tailcrap)): #loop for each slot in list
                #star the last position, push the *second to last* into it, repeat til at beginning
                tailcrap[len(tailcrap)-i-1].xpos = tailcrap[len(tailcrap)-i-2].xpos
                tailcrap[len(tailcrap)-i-1].ypos = tailcrap[len(tailcrap)-i-2].ypos

        if(len(tailcrap) > 0): # if you have at least one segment, push old head position into that
            tailcrap[0].update(oldx,oldy) #push ead position into the first position of list


    xpos += vx
    ypos += vy
    #Render Section
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (200, 0, 200), (xpos, ypos), 10)
    for i in range(pelletnum):
        pelletbag[i].draw()
    
    for i in range(pelletnum):
       if pelletbag[i].collide(xpos, ypos) == True:
           tailcrap.append(tailseg(oldx, oldy))

    for i in range(len(tailcrap)):
        tailcrap[i].draw()

    pygame.display.flip()
pygame.quit()