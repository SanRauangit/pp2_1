import pygame
import random
pygame.init() 
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Igra")
clock = pygame.time.Clock()

basket_x = 250
fruit_x = random.randint(0,580)
fruit_y = 0
fruit_speed = 5

score = 0
game_over=False
font=pygame.font.SysFont(None,40)

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    basket_x = 250
                    fruit_x = random.randint(0,580)
                    fruit_y = 0
                    fruit_speed = 5

                    score = 0
                    game_over=False
                if event.key == pygame.K_ESCAPE:
                    running=False
    if not game_over:
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 0:
            basket_x -= 5
        if keys[pygame.K_RIGHT] and basket_x < 600-80:
            basket_x += 5

        fruit_y += fruit_speed
        if fruit_y > 600:
            game_over = True
        basket_rect = pygame.Rect(basket_x,550,80,20)
        fruit_rect = pygame.Rect(fruit_x,fruit_y,20,20)
        
        if basket_rect.colliderect(fruit_rect):
            score += 1
            fruit_y = 0
            fruit_x = random.randint(0,580)
        
        screen.fill((255,255,255))
        
        pygame.draw.rect(screen,(0,0,255),(basket_x,550,80,20))
        pygame.draw.circle(screen,(255,0,0),(fruit_x,fruit_y),10)
        
        score_text=font.render(f"Score:{score}",True,(0,0,0))
        screen.blit(score_text,(10,10))

        pygame.display.update()
        clock.tick(60)
    else:
        screen.fill((0,0,0))
        over=font.render("GAME OVER",True,(255,0,0))
        scr = font.render(f"Your score:{score}",True,(255,255,255))
        restart = font.render(f"Press R to Restart | ESC to Quit",True,(255,255,255))
        screen.blit(over, (600//2 - over.get_width()//2, 220))
        screen.blit(scr, (600//2 - scr.get_width()//2, 280))
        screen.blit(restart, (600//2 - restart.get_width()//2, 340))

        pygame.display.update()
        clock.tick(60)
pygame.quit()
