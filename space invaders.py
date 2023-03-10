import pygame
import random


pygame.init()
pygame.display.set_caption("space invaders")
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render('LIVES:', False, (255,0,0))
gameover = False
timer = 0

#player variables-----------------
xpos = 400
ypos = 750
meft = False
might = False
shoot = False
lives = 3
#------------------------------------------------------------------------------------------------------------
#enemy Class
class Alien:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isa = True
        self.direction = 1
    def move(self, time):
        if time % 800 == 0:
            self.ypos += 100
            self.direction *=-1
            return 0 #resets timer to 0
        #moves everytime the timer increases by 100
        if timer % 100==0:
            self.xpos+=50 *self.direction
            #print("moving right)")
        return time
    def draw(self):
        if self.isa ==True:
            pygame.draw.rect(screen, (250, 250, 250), (self.xpos, self.ypos, 40, 40))
        elif self.isa == False:
            pygame.draw.rect(screen, (0, 0, 0), (self.xpos, self.ypos, 40, 40))
    def collide(self, BulletX, BulletY):
        global shoot
        if self.isa: #hit only alive aliens
            if BulletX > self.xpos:#check if the bulet is right of the left of the alien
                if BulletX < self.xpos + 40:#checks if the bullet is left of the right alien
                    if BulletY < self.ypos + 40:#checks if the bullet id above the alien
                        if BulletY > self.ypos:#checks if the bullet is below the alien
                           # print("hit!")#testing
                            self.isa = False#set the alien to dead
                            shoot = False
                            return False#set the bullet to dead
        return True#otherwise keep bullet alive
    
#------------------------------------------------------------------------------------------------------------
class Bullet:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isa = False
    def move(self, xpos, ypos):
        global shoot
        if self.isa == True: #only live shoot bullets
            self.ypos-=10 #move up when shot
        if self.ypos < 0:
            self.isa = False
            self.xpos = xpos
            self.ypos = ypos
            shoot = False
    def draw(self):
        pygame.draw.rect(screen, (250, 250, 250), (self.xpos, self.ypos, 3, 20))

#instantiate bullet object
bullet = Bullet(xpos+28, ypos)
group: list[Alien] = []#creat a list
for i in range (4): #handles the rows
    for y in range (9): #handle colums
        group.append(Alien(y*80+50, i*80+50))
Alfred = Alien(400, 400)#instantiating one


#------------------------------------------------------------------------------------------------------------
#WALLS
class wall:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.alive = True
        self.numh = 0
    def draw(self):
        if self.numh == 0:
            pygame.draw.rect(screen, (250,250,0), (self.xpos, self.ypos, 30, 30))
        if self.numh == 1:
            pygame.draw.rect(screen, (150,150, 10), (self.xpos, self.ypos, 30, 30))
        if self.numh == 2:
            pygame.draw.rect(screen, (50,50,0), (self.xpos, self.ypos, 30, 30))
    def collide(self,BulletX, BulletY):
        if self.numh <= 3:#only happens when the target if below 3 hits
            if BulletX > self.xpos:
                if BulletX < self.xpos + 30:
                    if BulletY > self.ypos:
                        if BulletY < self.ypos + 30:
                            #print("Wrong target!")
                            self.numh +=1
                            return self.numh
walls = []
Trump = wall(400, 670)
for k in range  (4):
    for l in range (2):
        for o in range (3):
            walls.append(wall(o*30+200*k+50, i*30+600))

#------------------------------------------------------------------------------------------------------------
class Missle:
    def __init__(self):
        self.xpos = -10
        self.ypos = -10
        self.isa = False
    def move(self):
        #print("i am a missile, I am ", self.isa)
        if self.isa == True: #only live shoot missle
            self.ypos += 5 #move down when shot
        if self.ypos >= 750:
            self.isa = False
            self.xpos = xpos
            self.ypos = ypos
    def draw(self):
        pygame.draw.rect(screen, (250, 250, 250), (self.xpos, self.ypos, 3, 20))

missle = []
for m in range (100):
    missle.append(Missle())
#GAME LOOP _______________________________________
while not gameover and lives >0:
    clock.tick(60)
    timer += 1
    #input section----------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True #quit game if x is pressed in top corner
        
        if event.type == pygame.KEYDOWN:#-----------------------
            if event.key == pygame.K_LEFT:
                meft = True
            if event.key == pygame.K_RIGHT:
                might = True
            if event.key == pygame.K_SPACE:
                shoot = True
        
        if event.type == pygame.KEYUP:#---------------------------
            if event.key == pygame.K_LEFT:
                meft = False
            if event.key == pygame.K_RIGHT:
                might = False

    #phyisics section------------------

    #check variables from the input section---------------
    if meft == True:
        vx =- 3
    else: vx = 0
    if might == True:
        vx =+ 3
    if shoot == True:
        bullet.isa = True
    if bullet.isa == True:
        bullet.move(xpos+28, ypos)
        if bullet.isa == True:
        #check for collision between bullet and enemy
            for i in range (len(group)):
                bullet.isa = group[i].collide(bullet.xpos, bullet.ypos)
                if bullet.isa == False:
                    break
        #check for collision between bullet and walls
        if bullet.isa == True:   
            for i in range (len(walls)):
                bullet.isa = walls[i].collide(bullet.xpos, bullet.ypos)
                if bullet.isa == False:
                    break
        
    else:
        bullet.xpos = xpos + 28
        bullet.ypos = ypos


#missile firing!
    fire = random.randrange(100)
    if fire < 20:
        p = random.randrange(len(group))#pick a random alien
        if group[p].isa == True:#only drop is alien is alive
            for i in range (len(missle)):#find the first alive missle
                if missle[i].isa == False:#fire missle that aren't already going
                    missle[i].isa = True#set it alive
                    missle[i].xpos = group[p].xpos+5#set the missle's position to aliens
                    missle[i].ypos = group[p].ypos+5

    #missle/wall collision
    for i in range (len(walls)):
            for k in range (len(missle)):
                if missle[k].isa == True:
                    if walls[i].collide(missle[k].xpos, missle[k].ypos) == False:
                        missle[k].isa = False
                        break




    #Collision for missle/player
    for i in range (len(missle)):
        if missle[i].isa:
            #print("missile is alive, checking for collision")
            if missle[i].xpos > xpos:
                if missle[i].xpos < xpos + 40:
                    print(missle[i].xpos, xpos)
                    if missle[i].ypos+10 > ypos :
                        if missle[i].ypos+20< ypos+30:   
                            pygame.draw.circle(screen, (255, 255, 0), (xpos, ypos), 30)
                            pygame.display.flip()
                            pygame.time.wait(50)
                            missle[i].isa = False
                            print("hit")
                            lives -= 1
                            xpos = 450
                            ypos = 750

    for i in range (len(group)):
        if group[i].isa:
            #print("Alien is alive, checking for collision")
            if group[i].xpos > xpos:
                if group[i].xpos < xpos + 40:
                    if group[i].ypos+30 > ypos :
                        if group[i].ypos+30< ypos+30:   
                            lives -= 3
    for i in range(len(missle)):
        missle[i].move()
    #update player position
    xpos += vx

    #Render section------------------------------------------------------------------------------------------
    screen.fill((0, 0, 0))
    
    for i in range (len(group)):
        group[i].draw()
    for i in range (len(group)):
        group[i].move(timer)
    for i in range (len(walls)):
        walls[i].draw()
    bullet.draw()
    for i in range (len(missle)):
        missle[i].draw()
    screen.blit(text_surface, (0,0))
    pygame.draw.rect(screen, (200, 200, 100), (xpos, 750, 60, 20))
    pygame.display.flip()
if lives <= 0:
    print("Game over!")
pygame.quit()