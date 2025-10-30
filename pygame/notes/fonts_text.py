import pygame
pygame.init()
screen=pygame.display.set_mode((640,480))
clock=pygame.time.Clock()
done=False
font=pygame.font.SysFont("conicsansms",72)
text=font.render("Hello,World",True,(0,128,0))
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            done=True
    screen.fill((255,255,255))
    screen.blit(text,(320-text.get_width()//2,240-text.get_height()//2))
    pygame.display.flip()
    clock.tick(60)




# PyGame has a way to enumerate all the fonts available on the machine:
# all_fonts = pygame.font.get_fonts()


# Additionally, there's a way to instantiate the default system font:
# font = pygame.font.Font(None, size)


# And alternatively, you can pass in the name of a font file you include along with your code instead of None to guarantee the existence of the perfect font:
# font = pygame.font.Font("myresources/fonts/Papyrus.ttf", 26)


# Using any combination of the above, you can write a better font creation function. For example, here's a function that takes a list of font names, a font size and will create a font instance for the first available font in the list. If none are available, it'll use the default system font.

# def make_font(fonts, size):
#     available = pygame.font.get_fonts()
#     # get_fonts() returns a list of lowercase spaceless font names
#     choices = map(lambda x:x.lower().replace(' ', ''), fonts)
#     for choice in choices:
#         if choice in available:
#             return pygame.font.SysFont(choice, size)
#     return pygame.font.Font(None, size)



#You can even further improve it by caching the font instance by font name and size.

# _cached_fonts = {}
# def get_font(font_preferences, size):
#     global _cached_fonts
#     key = str(font_preferences) + '|' + str(size)
#     font = _cached_fonts.get(key, None)
#     if font == None:
#         font = make_font(font_preferences, size)
#         _cached_fonts[key] = font
#     return font 


# You can take it a step further and actually cache the rendered text itself. Storing an image is cheaper than rendering a new one, especially if you plan on having the same text show up for more than one consecutive frame. Yes. That is your plan if you want it to be readable.

# _cached_text = {}
# def create_text(text, fonts, size, color):
#     global _cached_text
#     key = '|'.join(map(str, (fonts, size, color, text)))
#     image = _cached_text.get(key, None)
#     if image == None:
#         font = get_font(fonts, size)
#         image = font.render(text, True, color)
#         _cached_text[key] = image
#     return image