import pygame
import random
pygame.init()  
pygame.display.set_caption('breakout')  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
my_font = pygame.font.SysFont('Comic Sans MS', 30)
screen.fill((0,0,0))
mexit = False
p1Score = 0
clock = pygame.time.Clock()
class brick:
    def __init__(self, xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.alive = True
    
    def draw(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        if self.alive is True:
            pygame.draw.rect(screen, (r, g, b), (self.xpos, self.ypos, 50,20))
        elif self.alive == False:
            pygame.draw.rect(screen, (0, 0, 0), (self.xpos, self.ypos, 50, 20))
    def collide(self,bx,by):
        global bVy
        global p1Score
        if self.alive: #hit only alive brick
                if bx >= self.xpos and by > self.ypos and bx <= self.xpos+50 and by < self.ypos+20:
                    bVy *= -1
                    self.alive = False
                    p1Score += 1
#______________________________


group: list[brick] = []
for i in range (12): #handles the rows
    for y in range (12): #handle colums
        group.append(brick(y*60+50, i*30+50))
bob = brick(10,20)

#++++++++++++++++++++++++++++++
p1x = 400
p1y = 650
#+++++++++++++++
bx = 350
by = 600
bVx = 5
bVy = 5
#______________________________
while not mexit:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mexit = True
    #++++++++++++++++++++++
    keys = pygame.key.get_pressed()
    if keys [pygame.K_LEFT]:
        if p1x <= 0:
            p1x = 0
        else:
            p1x -=10
    
    if keys [pygame.K_RIGHT]:
        if p1x+100 >= 800:
            p1x = 700
        else:
            p1x +=10
    bx += bVx
    by += bVy


    if by < 0 or by + 20 > 800:
        bVy *= -1
    if bx < 0 or bx+ 20 > 800:
        bVx *= -1
    if bx >= p1x and by > p1y and bx <= p1x+100 and by < p1y+20:
        bVy *= -1

    #BRICK COLLISION
    for i in range (len(group)):
                if group[i].alive == True:
                    group[i].collide(bx, by)
 
#++++++++++++++++++++++++++++    
    screen.fill((0,0,0))
    for i in range (len(group)):
        group[i].draw()
    font = pygame.font.Font(None, 74)
    text = font.render(str(p1Score), 1, (255,255,0))
    screen.blit(text, (250,10))
    if p1Score == 144:
        text_surface = my_font.render('YOU WIN!', False, (255,0,0))
        screen.blit(text_surface, (380,400))
    pygame.draw.rect(screen, (255,255,255), (p1x, p1y, 100, 20), 1)
    pygame.draw.circle(screen, (255,255,255), (bx, by), 10)
    pygame.display.flip()
