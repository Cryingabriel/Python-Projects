import pygame as pg
import sys
import pygame.font
from pygame.math import Vector2
import random

playerpos = Vector2(100, 100)
pygame.init()


#platform class-------------------------------------------------------------
class platform():
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos, ypos)

    def draw(self, screen):
        pg.draw.rect(screen, (100, 50, 100), (self.pos.x, self.pos.y, 80, 30))
        
    def move(self):
        pass
    def collide(self):
        pass

class breakblock(platform):
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos, ypos)
        self.isAlive = True
        self.lives = 2
    
    def draw(self, screen):
        if self.isAlive == True:
            pg.draw.rect(screen, (0, 150, 0), (self.pos.x, self.pos.y, 80, 30))
        if self.lives == 0:
            self.isAlive = False
        print(self.lives)
    def move(self):
        pass
    def collide(self):
        pass

class Iceblock(platform):

    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos, ypos)
    
    def draw(self, screen):
        pg.draw.rect(screen, (100, 150, 255), (self.pos.x, self.pos.y, 80, 30))
    def move(self):
        pass
    def collide(self):
        pass

class trampoline(platform):

    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos, ypos)
    def draw(self, screen):
        pg.draw.rect(screen, (255, 255, 255), (self.pos.x, self.pos.y, 80, 30))
    def move(self):
        pass
    def collide(self):
        pass

class conblock(platform):
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos, ypos)
    
    def draw(self,screen):
        pg.draw.rect(screen, (50, 50, 50), (self.pos.x, self.pos.y, 80, 30))
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

    
    def draw(self, screen):
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





plats = [] #list to hold platforms

#goal class-------------------------------------------------------------
class goal():
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def draw(self, screen):
        pg.draw.rect(screen, (250, 0, 0), (self.xpos, self.ypos, 20,20))

goals = [] #you can have more than one in each level :)

#--------------------------------------------------------------------------------

#player class
class player():
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos,ypos)
        self.xvel = 0
        self.yvel = 0
        self.isonground = False
        self.ticker = 0
        self.framenum = 0
        self.rownum = 0
        self.link = pg.image.load('boxpep.png')
        self.link.set_colorkey((200,0,255))
        self.framewidth = 20
        self.frameheight = 40
        self.currentplat = 0
       
    def draw(self, screen):
        screen.blit(self.link, (self.pos.x, self.pos.y), (self.framewidth*self.framenum, self.rownum*self.frameheight, self.framewidth, self.frameheight))

       
    def move_left(self):
        self.xvel = -5
       
    def move_right(self):
        self.xvel = 5
       
    def stop(self):
        self.xvel = 0
       
    def jump(self):
        if self.isonground == True:
            self.yvel = -8    
    
    def animate(self):
        #Fixed animations
        if self.xvel < 0:
            self.ticker+=1
            self.rownum = 0
            if self.ticker%10==0:
                self.framenum+=1
            
            if self.framenum > 6:
                self.framenum = 0
        
        if self.xvel > 0:
            self.ticker+=1
            self.rownum = 1
            if self.ticker%10==0:
                self.framenum+=1
            if self.framenum > 6:
                self.framenum = 0
        
        if self.yvel < 0:
            self.ticker+=1
            self.rownum = 2
            if self.ticker%10==0:
                self.framenum+=1
            if self.framenum > 6:
                self.framenum = 0
    def update(self, platforms):
       
        self.pos += (self.xvel, self.yvel)
       
        if self.pos.y > 760:
            self.isonground = True
            self.yvel = 0
            self.ypos = 760
           
        if self.isonground == False:
            self.yvel+=.2
        
        if self.currentplat == 2:
            self.xvel += self.xvel +6
            self.isonground = True

        if self.currentplat == 4:
            self.yvel -= 4
        if self.currentplat == 5:
            f = random.randint(1,2)
            if f == 1:
                self.xvel-=2
            elif f == 2:
                self.xvel+=2
           
        for goal in goals:
            if self.pos.x + 10 >= goal.xpos and self.pos.x <= goal.xpos + 20:
                if self.pos.y + 30 >= goal.ypos and self.pos.y + 30 <= goal.ypos + 20:
                    print("goal hit!")
                    self.xpos = 100
                    self.ypos = 100
                    return True  # Change state when player touches a red square
           
    def collision(self, platforms):
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
        for plat in platforms:
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
            if self.yvel > 0:
                self.yvel = 0
                self.pos.y -= 1
                #gravity
        else:
            self.currentplat = 0
            self.isonground = False
        #for plat in platforms:
        #    if self.pos.x + 10 >= plat.pos.x and self.pos.x <= plat.pos.x + 80:
        #        if self.pos.y + 30 >= plat.pos.y and self.pos.y + 30 <= plat.pos.y + 30:
        #            return True
        #return False
       
p1 = player(playerpos.x,playerpos.y)

#--------------------------------------------------------------------------------
#the parent class!
#stuff you want to persist should go in here (i.e. fonts, player health, etc)
class States(object):
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None
        self.font = pg.font.Font(None, 36)
       
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                p1.move_left()
            elif event.key == pg.K_RIGHT:
                p1.move_right()
            elif event.key == pg.K_UP:
                p1.jump()
        elif event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                p1.stop()
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.done = True

#--------------------------------------------------------------------------------
class End(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'LevelOne'
       
    def cleanup(self):
        print('cleaning up End state stuff')
       
    def startup(self):
        print('starting End state stuff')

    def update(self, screen, dt):
        self.draw(screen)
        if p1.update(plats)==True:
            self.done = True
       
    def draw(self, screen):
        screen.fill((0,0,80))
        text = self.font.render("You Win!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 400))  
        screen.blit(text, text_rect)

#--------------------------------------------------------------------------------

class LevelOne(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'LevelTwo'
       
       
    def cleanup(self):
        print('cleaning up Level 1 stuff')
        plats.clear()
       
    def startup(self):
        print('Level 1!')
        plats.append(platform(200, 400))
        plats.append(platform(500, 200))
        plats.append(platform(400, 500))
        plats.append(platform(100, 200))
        goals.append(goal(250, 350))
       

    def update(self, screen, dt):
        self.draw(screen)
        if p1.update(plats)==True:
            self.done = True
       
    def draw(self, screen):
        screen.fill((0,0,0))
        p1.draw(screen)
        for i in range (len(plats)):
            plats[i].draw(screen)
            plats[i].move()
            plats[i].collide()
        for i in range (len(goals)):
            goals[i].draw(screen)
        p1.collision(plats)
        text = self.font.render("Level 1", True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 20))  
        screen.blit(text, text_rect)
       
       
#--------------------------------------------------------------------------------

class LevelTwo(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'End'
       
    def cleanup(self):
        print('cleaning up Level 2 stuff')
        plats.clear()
       
    def startup(self):
        print('Level 2!')
        plats.append(platform(100, 500))
        plats.append(mblock(400, 300))
        plats.append(platform(400, 600))
        plats.append(trampoline(600, 700))
        goals.append(goal(250, 350))

    def update(self, screen, dt):
        self.draw(screen)
        if p1.update(plats)== True:
            self.done = True
       
    def draw(self, screen):
        screen.fill((0,0,255))
        p1.draw(screen)
        for i in range (len(plats)):
            plats[i].draw(screen)
            plats[i].move()
            plats[i].collide()
        for i in range (len(goals)):
            goals[i].draw(screen)
        p1.collision(plats)
        text = self.font.render("Level 2", True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 20))  
        screen.blit(text, text_rect)
#--------------------------------------------------------------------------------      
class Control:
    def __init__(self, **settings): # ** denotes a KWARG, which lets you have an unknown num of parameters
        self.__dict__.update(settings) #double underscore helps to avoid naming conflicts in subclasses
        self.done = False
        self.screen = pg.display.set_mode(settings["size"])
        self.clock = pg.time.Clock()
       
       
    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name] #state has been set to an OBJECT
       
       
    def flip_state(self):
        self.state.done = False #we are referencing the variable of whatever OBJECT is in "state"
        previous,self.state_name = self.state_name, self.state.next
        self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup()
        self.state.previous = previous
       
    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen, dt)
       
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.state.get_event(event)
           
    def main_game_loop(self):
        while not self.done:
            delta_time = self.clock.tick(settings["fps"])/1000.0
            self.event_loop()
            self.update(delta_time)
            pg.display.update()
 
#--------------------------------------------------------------------------------
#"main"
           
#a dictionary containing the settings
settings = {
    'size':(800,800),
    'fps' :60
}

#a dictionary containing all the different states available
state_dict = {
    'End': End(),
    'LevelOne': LevelOne(),
    'LevelTwo': LevelTwo()
}

#------------------------------------
#instantiate a control object named "app"
#after running this constructor, "app" will have 4 variables:
#a copy of the settings dictionary, a boolean named "done" set to False,
#a screen variable holding the pygame display, and a clock variable
app = Control(**settings)
#------------------------------------

#------------------------------------
#the setup_states function passes in the dictionary of available states
#and also sets what the begnning state will be
app.setup_states(state_dict, 'LevelOne')
app.state.startup() #call startup for the initial state, Level One
#------------------------------------

#------------------------------------
app.main_game_loop() #OMG GAME LUP!


pg.quit()
sys.exit()