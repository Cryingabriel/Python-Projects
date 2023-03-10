import pygame
pygame.init()


screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("ahhh")


mexit = False

clock = pygame.time.Clock()
#___player variables______________
p1x = 20
p1y = 200
p2x = 660
p2y = 200

p2Score = 0
p1Score = 0
#____ball variables____________________
bx = 350
by = 250
bVx = 5
bVy = 5

while not mexit:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mexit = True
            

    
    
    #_________________
    keys = pygame.key.get_pressed()
    if keys [pygame.K_w]:
        p1y-=10
    if keys [pygame.K_s]:
        p1y+=10
    if keys [pygame.K_UP]:
        p2y-=10
    if keys [pygame.K_DOWN]:
        p2y+=10
    
    
    #______Ball movement____________
    
    bx += bVx
    by += bVy
    
    #reflect ball
#     if bx < 0 or bx + 20 > 700:
#         bVx *= -1
    if by < 0 or by + 20 > 500:
        bVy *= -1
    if bx < p1x + 30 and by + 20 > p1y and by < p1y +100:
        bVx *= -1
    if bx > p2x - 10 and by + 20 > p2y and by < p2y +100:
        bVx *= -1
    if bx <= 0:
        bVx *= -1
        p2Score += 1
    elif bx >= 690:
        bVx *= -1
        p1Score += 1
    #----------render---------
    screen.fill((0,0,0))
    font = pygame.font.Font(None, 74)
    text = font.render(str(p1Score), 1, (255,255,0))
    screen.blit(text, (250,10))
    text = font.render(str(p2Score), 1, (255,0,255))
    screen.blit(text, (420,10))
    pygame.draw.rect(screen, (255,255,255), (p1x, p1y, 20, 100), 1)
    pygame.draw.rect(screen, (255,255,255), (p2x, p2y, 20, 100), 1)
    pygame.draw.circle(screen, (255,255,255), (bx, by), 10)
    pygame.draw.line(screen, (255,0,0), [349,0], [349,500], 3)


    pygame.display.flip()