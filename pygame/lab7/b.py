import pygame
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((640,480))
clock=pygame.time.Clock()
done=True

current_song=0
playlist=['Flashing_lights.mp3','Better.mp3','Hymn_for_the_weekend.mp3']
paused=False

pygame.mixer.music.load(playlist[current_song])
pygame.mixer.music.play()

while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
        if event.type==pygame.KEYDOWN: 
            if event.key==pygame.K_ESCAPE:
                done=False
            if event.key==pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused=False
                else:
                    pygame.mixer.music.pause()
                    paused=True
            elif event.key==pygame.K_RIGHT:
                current_song=(current_song+1)%len(playlist)
                pygame.mixer.music.load(playlist[current_song])
                pygame.mixer.music.play()
                paused=False
            elif event.key==pygame.K_LEFT:
                current_song=(current_song-1)%len(playlist)
                pygame.mixer.music.load(playlist[current_song])
                pygame.mixer.music.play()
                paused=False
    screen.fill((0,0,0))
    font=pygame.font.Font(None,36)
    text=font.render(f"Song: {playlist[current_song]}",True,(255,255,255))
    screen.blit(text,(150,150))
    pygame.display.flip()
    clock.tick(60)