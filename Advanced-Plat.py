import pygame as pg
import sys
import random
from pygame.math import Vector2
#Constants
screens = (800, 800)
color = (0,0,0)
clock = pg.time.Clock()
#init
pg.init()
screen = pg.display.set_mode(screens)
pg.display.set_caption("plat with inheritance")

playerpos = Vector2(100, 780)


LEFT = 0 
RIGHT = 1 
UP = 2
keys = [False, False, False]

gover = False



class platform():
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos, ypos)

    def draw(self):
        pg.draw.rect(screen, (100, 50, 100), (self.pos.x, self.pos.y, 80, 30))
    
    def move(self):
        pass
    def collide(self):
        pass

class mblock(platform):
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos, ypos)
        self.startx = self.pos.x
        self.starty = self.pos.y
        self.direction = 1

    
    def draw(self):
        pg.draw.rect(screen, (100, 50, 200), (self.pos.x, self.pos.y, 80, 30))
    
    def move(self):
        if self.direction == 1:
            if self.pos.x < self.startx:
                self.direction*=-1
            else:
                self.pos.x-= random.randint(0,3)
        else:
            if self.pos.x > self.startx +200:
                self.direction*=-1
            else:
                self.pos.x+= random.randint(0,2)
    def collide(self):
        pass

class conblock(platform):
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos, ypos)
    
    def draw(self):
        pg.draw.rect(screen, (50, 50, 50), (self.pos.x, self.pos.y, 80, 30))
    def move(self):
        pass
    def collide(self):
        pass

class trampoline(platform):
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos, ypos)
    def draw(self):
        pg.draw.rect(screen, (255, 255, 255), (self.pos.x, self.pos.y, 80, 30))
    def move(self):
        pass
    def collide(self):
        pass

class Iceblock(platform):

    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos, ypos)
    
    def draw(self):
        pg.draw.rect(screen, (100, 150, 255), (self.pos.x, self.pos.y, 80, 30))
    def move(self):
        pass
    def collide(self):
        pass

class breakblock(platform):
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos, ypos)
        self.isAlive = True
        self.lives = 2
    
    def draw(self):
        if self.isAlive == True:
            pg.draw.rect(screen, (0, 150, 0), (self.pos.x, self.pos.y, 80, 30))
        if self.lives == 0:
            self.isAlive = False
        print(self.lives)
    def move(self):
        pass
    def collide(self):
        pass

class player(breakblock):
    def __init__(self, xpos , ypos):
        self.pos = Vector2(xpos,ypos)
        self.isonground = False
        self.vx = 0
        self.vy = 0
        self.ticker = 0
        self.framenum = 0
        self.rownum = 0
        self.link = pg.image.load('boxpep.png')
        self.link.set_colorkey((200,0,255))
        self.framewidth = 20
        self.frameheight = 40
        self.currentplat = 0
        super().__init__(xpos, ypos)


    def draw(self):
        screen.blit(self.link, (self.pos.x, self.pos.y), (self.framewidth*self.framenum, self.rownum*self.frameheight, self.framewidth, self.frameheight))


    def animate(self):
        #Fixed animations
        if self.vx < 0:
            self.ticker+=1
            self.rownum = 0
            if self.ticker%10==0:
                self.framenum+=1
            
            if self.framenum > 6:
                self.framenum = 0
        
        if self.vx > 0:
            self.ticker+=1
            self.rownum = 1
            if self.ticker%10==0:
                self.framenum+=1
            if self.framenum > 6:
                self.framenum = 0
        
        if self.vy < 0:
            self.ticker+=1
            self.rownum = 2
            if self.ticker%10==0:
                self.framenum+=1
            if self.framenum > 6:
                self.framenum = 0
        
    def move(self,keys):
        for event in pg.event.get(): #quit game if x is pressed in top corner
        
            if event.type == pg.KEYDOWN: #keyboard input
                if event.key == pg.K_LEFT:
                    keys[LEFT]=True

                if event.key == pg.K_UP:
                    keys[UP]=True
                
                if event.key == pg.K_RIGHT:
                    keys[RIGHT]=True
            
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    keys[LEFT]=False

                if event.key == pg.K_UP:
                    keys[UP]=False
                
                if event.key == pg.K_RIGHT:
                    keys[RIGHT]=False
        if keys[LEFT]==True:
            self.vx=-3   
        elif keys[RIGHT]==True:
            self.vx=3
            #JUMPING
        elif keys[UP] == True and self.isonground == True:
            self.vy = -8
            self.isonground = False
        #turn off velocity
        else:
            self.vx = 0
        
        if self.isonground == False:
            self.vy+=.2 #notice this grows over time, aka ACCELERATION

        if self.pos.y <=0:
            self.vy+=1
        
        if self.currentplat == 2:
            self.vx += self.vx +6
            self.isonground = True

        if self.currentplat == 4:
            self.vy -= 4
        if self.currentplat == 5:
            f = random.randint(1,2)
            if f == 1:
                self.vx-=2
            elif f == 2:
                self.vx+=2
        if self.currentplat == 6:
            self.lives -= 1

        self.pos += (self.vx, self.vy)

        return self.lives

    def collide(self,plats):
        colliding = False

        if self.pos.x < 0:
            self.pos.x = 0
        elif self.pos.x+20 > 800:
            self.pos.x = 780

    
        if self.pos.y > 760:
            colliding = True
            self.isonground = True
            self.pos.y = 760

        playerrect = pg.rect.Rect(self.pos, (self.framewidth, self.frameheight))        
        for plat in plats:
            platrect = pg.rect.Rect(plat.pos.x, plat.pos.y, 80, 30)
            if playerrect.colliderect(platrect):
                colliding = True
                if isinstance(plat, conblock):
                    self.currentplat = 2
                elif isinstance(plat, mblock):
                    self.currentplat = 3
                elif isinstance(plat, trampoline):
                    self.currentplat = 4
                elif isinstance(plat, Iceblock):
                    self.currentplat = 5
                elif isinstance(plat, breakblock):
                    self.currentplat = 6
                else:
                    self.currentplat = 1

        if colliding:        
            self.isonground = True
            if self.vy > 0:
                self.vy = 0
                self.pos.y -= 1
                #gravity
        else:
            self.currentplat = 0
            self.isonground = False

class goal():
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def draw(self, screen):
        pg.draw.rect(screen, (250, 0, 0), (self.xpos, self.ypos, 20,20))

goals = [] #you can have more than one in each level :)



plats = []
for i in range(5):
    plats.append(platform(random.randrange(50, 700), random.randrange(50, 700)))
for i in range(3):
    plats.append(mblock(random.randrange(50, 600), random.randrange(50, 700)))
for i in range(4):
    plats.append(conblock(random.randrange(50, 700), random.randrange(50, 500)))

for i in range(2):
    plats.append(trampoline(random.randrange(50, 500), random.randrange(50, 700)))

for i in range(4):
    plats.append(Iceblock(random.randrange(100, 700), random.randrange(100, 700)))

for i in range(1):
    plats.append(breakblock(random.randrange(100, 150), random.randrange(700, 750)))

ah = player(playerpos.x, playerpos.y)
while(1):
    clock.tick(60)


    for i in range(len(plats)):
        plats[i].move()
        plats[i].collide()
    
    ah.collide(plats)
    #l.collide(player)
    ah.move(keys)
    
    #render section
    screen.fill(color)
    for i in range(len(plats)):
        plats[i].draw()
    
    ah.draw()
    ah.animate()

    pg.display.flip()
pg.quit()