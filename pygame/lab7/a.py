import pygame
import datetime
pygame.init()
x,y=1920,1080
center=(x//2,y//2)
clock=pygame.time.Clock()
done=False

micky=pygame.image.load('base_micky.jpg')
micky=pygame.transform.scale(micky,(x,y))

second=pygame.image.load('second.png')
minute=pygame.image.load('minute.png')

second=pygame.transform.scale(second,(center))
minute=pygame.transform.scale(minute,(center))

screen=pygame.display.set_mode((x,y))

def rotate_hand(hand_surface,angle,pivot):
    rotated_hand=pygame.transform.rotate(hand_surface,-angle)
    rotated_rect=rotated_hand.get_rect(center=pivot)
    return rotated_hand,rotated_rect

done=True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=False
        if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            done=False
    screen.blit(micky,(0,0))
    now=datetime.datetime.now()
    minutes=now.minute
    seconds=now.second
    
    second_angle=seconds*6
    minute_angle=minutes*6
    rotated_second,second_rect=rotate_hand(second,second_angle,center)
    screen.blit(rotated_second,second_rect.topleft)

    rotated_minute,minute_rect=rotate_hand(minute,minute_angle,center)
    screen.blit(rotated_minute,minute_rect.topleft)

    pygame.display.flip()
    clock.tick(60)