import pygame
color=((0,128,255))
surface=pygame.display.set_mode((400,300))
# Rectangle
# pygame.draw.rect(surface, color, pygame.Rect(left, top, width, height))

# Circle
# pygame.draw.circle(surface, color, (x, y), radius)

# Built in Outlines
# draw a rectangle
pygame.draw.rect(surface, color, pygame.Rect(10, 10, 100, 100), 10)
# draw a circle
pygame.draw.circle(surface, color, (300, 60), 50, 10)
# Moral of the story: when you draw a polygon, rectangle, circle, etc, draw it filled in or with 1-pixel thickness. Everything else is not very well implemented.


# Acceptable outlines
import math
def do_nice_outlines(surface, counter):
        color = (0, 128, 0) # green
        
        # draw a rectangle
        pygame.draw.rect(surface, color, pygame.Rect(10, 10, 100, 10))
        pygame.draw.rect(surface, color, pygame.Rect(10, 10, 10, 100))
        pygame.draw.rect(surface, color, pygame.Rect(100, 10, 10, 100))
        pygame.draw.rect(surface, color, pygame.Rect(10, 100, 100, 10))
        
        # draw a circle
        center_x = 300
        center_y = 60
        radius = 45
        iterations = 150
        for i in range(iterations):
                ang = i * 3.14159 * 2 / iterations
                dx = int(math.cos(ang) * radius)
                dy = int(math.sin(ang) * radius)
                x = center_x + dx
                y = center_y + dy
                pygame.draw.circle(surface, color, (x, y), 5)

# Polygons
# pygame.draw.polygon(surface, color, point_list)

# Lines
# pygame.draw.line(surface, color, (startX, startY), (endX, endY), width)

# 