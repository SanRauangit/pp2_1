import pygame
pygame.init()
screen=pygame.display.set_mode((1080,820))
done=False
x=540
y=420
radius=25
clock=pygame.time.Clock()
color=(255,0,0)
while not done:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            done=True
        if event.type==pygame.QUIT:
            done=True

    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y-radius > 0:y-=20
    if pressed[pygame.K_DOWN] and y+radius < 820:y+=20
    if pressed[pygame.K_RIGHT] and x+radius <= 1200:
        x+=20
        if x+radius>=1080:
            x-=1080
    if pressed[pygame.K_LEFT] and x-radius > 0 :x-=20

    screen.fill((255,255,255))
    pygame.draw.circle(screen,color,(x,y),radius)
    pygame.display.flip()
    clock.tick(60)