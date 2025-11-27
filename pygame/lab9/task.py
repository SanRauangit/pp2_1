import pygame,random
pygame.init()
screen=pygame.display.set_mode((950,800))
done=False
x=540
y=460
radius=20
clock=pygame.time.Clock()
color=(255,0,0)
enemy_y=random.randint(10,780)
enemy_x=0
enemy_speed=5
game_over=False

font=pygame.font.SysFont(None,40)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        if event.type == pygame.QUIT:
            done=True
        if game_over:
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        enemy_y=random.randint(10,780)
                        enemy_x=0
                        enemy_speed=5
                        game_over=False
                        x=540
                        y=460
                        radius=20
    if not game_over:
        

        pressed=pygame.key.get_pressed()    
        if pressed[pygame.K_w] and  y-radius > 0: y -=10
        if pressed[pygame.K_s] and  y+radius < 800: y +=10
        if pressed[pygame.K_a] and  x-radius > 0: x -=10
        if pressed[pygame.K_d] and  x+radius < 950: x +=10

        enemy_x+=enemy_speed
        enemy_rect=pygame.Rect((enemy_x,enemy_y,80,20))
        ball=pygame.Rect((x-radius,y-radius,20,20))
        if enemy_x >= 950:
            enemy_x=0
            enemy_y=random.randint(10,780)
        if enemy_rect.colliderect(ball):
            game_over=True

        screen.fill((255,255,255))
        pygame.draw.circle(screen,color,(x,y),radius)
        pygame.draw.rect(screen, (0, 0, 255), enemy_rect) 
        pygame.display.flip()
        clock.tick(60)
    else:
        screen.fill((0,0,0))
        over=font.render("GAME OVER",True,(255,0,0))
        screen.blit(over, (600//2 - over.get_width()//2, 220))
        pygame.display.flip()