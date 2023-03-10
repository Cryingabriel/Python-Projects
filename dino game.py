import pygame
import random
pygame.init()


screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("dino")
mexit = False
clock = pygame.time.Clock()
#game variables______________________________
p1x = 20
p1y = 200
vx = 0
vy = 0
White=(0,0,0)
p1w =20
p1h =20
dinoimg = pygame.image.load('dino.png')
touchground = False
point = 0
#Cactus's Variables__________________________

cactush = [80,40,20,80,30]#creats and initializes a 5-slot list

cactusx = []#creats empty list

cactusimg = pygame.image.load('cactus.png')
for x in range(1,10):#runs this loop 5 times
    #append adds an entry into the array
    cactusx.append(random.randrange(200,3000))
#game loop___________________________________

while not mexit:
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mexit = True;
    
    #timer section___________________
    clock.tick(60)
    cactusx = [x-7 for x in cactusx]
    #gravity
    if touchground == False:
        vy+=.2
    if p1y > 460:
        touchground = True
        vy = 0
        p1y = 460
    #check for player/cactus collision
    for x, y in zip (cactusx, cactush):
        a = pygame.Rect((x, 480-y), (30,80))
        b = pygame.Rect((p1x,p1y), (30,30))
        if a.colliderect(b) == True:
            print("COLLISION")
            mexit=True
         #winsound.Beep(900,900)
    #update cactus location if they are off creen
    for x in range(len(cactusx)):
        if cactusx[x]<0:
            cactusx[x]=random.randrange(640,5000)
            print("reset to ", cactusx[x]) #used for testing
    
    
    #input section___________________
    keys = pygame.key.get_pressed()
    if keys [pygame.K_w] and touchground == True:
        vy = -7.5
        touchground = False
    
    
    p1x+=vx
    p1y+=vy
    point +=1
    print(point)
    #render section__________________
    screen.fill((0,0,0))
    #________________________________
    for x, y in zip(cactusx, cactush):
        screen.blit(cactusimg,(x-15,480-y))
    font = pygame.font.Font(None, 74)
    text = font.render(str(point), 1, (255,255,0))
    screen.blit(text, (250,10))
    
    pygame.draw.rect(screen,White, (p1x, p1y, p1w, p1h))
    screen.blit(dinoimg,(p1x, p1y))
    #________________________________
    pygame.display.flip()
    
#end loop____________________________
pygame.quit()