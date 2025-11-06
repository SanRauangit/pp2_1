import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint")
    clock = pygame.time.Clock()
    
    # Simple settings
    brush_size = 15
    color = (0, 0, 255)  # Start with blue
    tool = 'line'  # line, rect, circle, erase
    shapes = []  # Store all drawings
    drawing = False
    start_pos = None
    
    # Available colors
    colors = {
        'r': (255, 0, 0),    'g': (0, 255, 0),    'b': (0, 0, 255),
        'y': (255, 255, 0),  'c': (0, 255, 255),  'm': (255, 0, 255),
        'w': (255, 255, 255),'k': (0, 0, 0)
    }
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Color selection
                if event.unicode in colors:
                    color = colors[event.unicode]
                
                # Tool selection
                if event.key == pygame.K_l:
                    tool = 'line'
                elif event.key == pygame.K_t:
                    tool = 'rect'
                elif event.key == pygame.K_o:
                    tool = 'circle'
                elif event.key == pygame.K_e:
                    tool = 'erase'
                elif event.key == pygame.K_SPACE:
                    shapes = []
                    screen.fill((0, 0, 0))
            
            # Mouse events (clicks)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    drawing = True
                    start_pos = event.pos
                    
                    # For line/eraser, start drawing immediately
                    if tool in ['line', 'erase']:
                        current_color = (0, 0, 0) if tool == 'erase' else color
                        shapes.append(('point', event.pos, brush_size, current_color))
                
                elif event.button == 3:  # Right click - change brush size
                    if tool in ['line', 'erase']:
                        brush_size = max(1, brush_size - 1)
                    else:
                        brush_size = max(1, brush_size - 1)  # Also work for shapes
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing and start_pos:
                    current_pos = event.pos
                    # For shapes, store when mouse released
                    if tool == 'rect':
                        # Make sure rectangle has some size
                        if abs(current_pos[0] - start_pos[0]) > 2 and abs(current_pos[1] - start_pos[1]) > 2:
                            shapes.append(('rect', start_pos, current_pos, color, max(1, brush_size//3)))
                    elif tool == 'circle':
                        # Calculate radius from center to current position
                        radius = int(((current_pos[0]-start_pos[0])**2 + (current_pos[1]-start_pos[1])**2)**0.5)
                        if radius > 2:  # Make sure circle has some size
                            shapes.append(('circle', start_pos, radius, color, max(1, brush_size//3)))
                    drawing = False
            
            if event.type == pygame.MOUSEMOTION:
                if drawing and tool in ['line', 'erase']:
                    current_color = (0, 0, 0) if tool == 'erase' else color
                    shapes.append(('point', event.pos, brush_size, current_color))
        
        # Draw everything
        screen.fill((0, 0, 0))
        
        # Draw all stored shapes
        i = 0
        while i < len(shapes):
            item = shapes[i]
            
            if item[0] == 'point':
                # Connect points for smooth lines
                if i < len(shapes) - 1 and shapes[i+1][0] == 'point':
                    draw_smooth_line(screen, item[1], shapes[i+1][1], item[2], item[3])
                pygame.draw.circle(screen, item[3], item[1], item[2])
            
            elif item[0] == 'rect':
                start, end, col, width = item[1], item[2], item[3], item[4]
                # Create rectangle from two points
                rect = pygame.Rect(
                    min(start[0], end[0]), 
                    min(start[1], end[1]),
                    abs(end[0] - start[0]), 
                    abs(end[1] - start[1])
                )
                pygame.draw.rect(screen, col, rect, width)
            
            elif item[0] == 'circle':
                center, radius, col, width = item[1], item[2], item[3], item[4]
                pygame.draw.circle(screen, col, center, radius, width)
            
            i += 1
        
        # Show preview for shapes while drawing
        if drawing and tool in ['rect', 'circle'] and start_pos:
            current_pos = pygame.mouse.get_pos()
            if tool == 'rect':
                # Draw preview rectangle
                rect = pygame.Rect(
                    min(start_pos[0], current_pos[0]), 
                    min(start_pos[1], current_pos[1]),
                    abs(current_pos[0] - start_pos[0]), 
                    abs(current_pos[1] - start_pos[1])
                )
                pygame.draw.rect(screen, color, rect, max(1, brush_size//3))
            
            elif tool == 'circle':
                # Draw preview circle
                radius = int(((current_pos[0]-start_pos[0])**2 + (current_pos[1]-start_pos[1])**2)**0.5)
                if radius > 1:  # Only draw if radius is meaningful
                    pygame.draw.circle(screen, color, start_pos, radius, max(1, brush_size//3))
        
        # Simple info
        font = pygame.font.Font(None, 24)
        info = font.render(f"Tool: {tool} | Size: {brush_size}", True, (255, 255, 255))
        screen.blit(info, (10, 10))
        
        # Help text
        help_text = font.render("L:Line T:Rect O:Circle E:Eraser SPACE:Clear", True, (200, 200, 200))
        screen.blit(help_text, (10, 40))
        
        pygame.display.flip()
        clock.tick(60)

def draw_smooth_line(screen, start, end, width, color):
    # Simple line drawing between points
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    steps = max(abs(dx), abs(dy))
    
    if steps == 0:  # Same point
        pygame.draw.circle(screen, color, start, width)
        return
    
    for i in range(steps):
        progress = i / steps
        x = int(start[0] + dx * progress)
        y = int(start[1] + dy * progress)
        pygame.draw.circle(screen, color, (x, y), width)

main()