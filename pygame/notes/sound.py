import pygame
# Playing a song once:
pygame.mixer.music.load('foo.mp3')
pygame.mixer.music.play(0)

# Playing a song infinitely:
pygame.mixer.music.load('foo.mp3')
pygame.mixer.music.play(-1)

# Queuing a Song:
pygame.mixer.music.queue('next_song.mp3')

# Stopping a Song:
pygame.mixer.music.stop()

# Doing Something When a Song Ends:

SONG_END = pygame.USEREVENT + 1

pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play()


...

while True:
    ...
    for event in pygame.event.get():
        ...
        if event.type == SONG_END:
            print("the song ended!")

# If, for example, you wanted to play randomly from a list of 5 songs, one could create a list of the songs as a global:
_songs = ['song_1.mp3', 'song_2.mp3', 'song_3.mp3', 'song_4.mp3', 'song_5.mp3']

# Add a flag indicating which song is currently playing:
_currently_playing_song = None

# And write a function that chooses a different song randomly that gets called each time the SONG_END event is fired:
import random

def play_a_different_song():
    global _currently_playing_song, _songs
    next_song = random.choice(_songs)
    while next_song == _currently_playing_song:
        next_song = random.choice(_songs)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()

# Or if you want them to play in the same sequence each time:
def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

# The music API is very centralized. However sounds require the creation of sound objects that you have to hold on to. Much like images. Sounds have a simple .play() method that will start playing the sound.

effect = pygame.mixer.Sound('beep.wav')
effect.play()

# Because you can make the mistake of storing sound instances redundantly, I suggest creating a sound library much like the image library from part 2.
_sound_library = {}
def play_sound(path):
  global _sound_library
  sound = _sound_library.get(path)
  if sound == None:
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    sound = pygame.mixer.Sound(canonicalized_path)
    _sound_library[path] = sound
  sound.play()

# 