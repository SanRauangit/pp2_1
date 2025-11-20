import pygame,math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint")
    clock = pygame.time.Clock()
    
    # Simple settings
    brush_size = 15
    color = (0, 0, 255)  # Start with blue
    tool = 'line'  # line by default
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
                
                # Tool selection - FIXED: Use consistent names
                if event.key == pygame.K_l:
                    tool = 'line'
                elif event.key == pygame.K_t:
                    tool = 'rect'
                elif event.key == pygame.K_o:
                    tool = 'circle'
                elif event.key == pygame.K_e:
                    tool = 'erase'
                elif event.key == pygame.K_s:
                    tool = 'square'
                elif event.key == pygame.K_i:
                    tool = 'right_triangle'  # Fixed: consistent name
                elif event.key == pygame.K_q:
                    tool = 'equilateral'  # Fixed: consistent name
                elif event.key == pygame.K_h:
                    tool = 'rhombus'
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
                    brush_size = max(1, brush_size - 1)
            
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if drawing and start_pos:
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
                    elif tool == 'square':
                        side = max(abs(current_pos[0]-start_pos[0]), abs(current_pos[1]-start_pos[1]))
                        if side > 2:  # Make sure square has some size
                            shapes.append(('square', start_pos, side, color, max(1, brush_size//3)))
                    elif tool == 'right_triangle':  # Fixed: consistent name
                        if abs(current_pos[0] - start_pos[0]) > 2 and abs(current_pos[1] - start_pos[1]) > 2:
                            shapes.append(('right_triangle', start_pos, current_pos, color, max(1, brush_size//3)))
                    elif tool == 'equilateral':  # Fixed: consistent name
                        side = abs(current_pos[0] - start_pos[0])
                        if side > 2:  # Make sure triangle has some size
                            shapes.append(('equilateral', start_pos, side, color, max(1, brush_size//3)))
                    elif tool == 'rhombus':
                        if abs(current_pos[0] - start_pos[0]) > 2 and abs(current_pos[1] - start_pos[1]) > 2:
                            shapes.append(('rhombus', start_pos, current_pos, color, max(1, brush_size//3)))
                        
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
            
            # Line 
            if item[0] == 'point':
                # Connect points for smooth lines
                if i < len(shapes) - 1 and shapes[i+1][0] == 'point':
                    draw_smooth_line(screen, item[1], shapes[i+1][1], item[2], item[3])
                pygame.draw.circle(screen, item[3], item[1], item[2])
            
            # Rectangle
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
            
            # Circle
            elif item[0] == 'circle':
                center, radius, col, width = item[1], item[2], item[3], item[4]
                pygame.draw.circle(screen, col, center, radius, width)
            
            # Square
            elif item[0] == 'square':
                x,y = item[1]
                side = item[2]
                rect = pygame.Rect(x,y,side,side)
                pygame.draw.rect(screen,item[3],rect,item[4])
            
            # Right triangle
            elif item[0] == 'right_triangle':
                x1,y1 = item[1]
                x2,y2 = item[2]
                points = [(x1,y1),(x2,y1),(x1,y2)]
                pygame.draw.polygon(screen,item[3],points,item[4])
            
            # Equilateral triangle - FIXED: correct calculation
            elif item[0] == 'equilateral':
                x,y = item[1]
                side = item[2]
                h = int((math.sqrt(3)/2) * side)  # Fixed: correct height calculation
                points=[(x,y),(x+side,y),(x+side//2,y-h)]
                pygame.draw.polygon(screen,item[3],points,item[4])
            
            # Rhombus
            elif item[0] == 'rhombus':
                x1,y1 = item[1]
                x2,y2 = item[2]
                midx = (x1 + x2) // 2
                midy = (y1 + y2) // 2
                points = [
                    (midx,y1),
                    (x2,midy),
                    (midx,y2),
                    (x1,midy)]
                pygame.draw.polygon(screen,item[3],points,item[4])

            i += 1
        
        # Show preview for shapes while drawing
        if drawing and start_pos:
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
                    pygame.draw.circle(screen, color, start_pos, radius, max(1,brush_size//3))
        
            elif tool == 'square':
                side = max(abs(current_pos[0]-start_pos[0]),abs(current_pos[1]-start_pos[1]))
                rect = pygame.Rect(start_pos[0],start_pos[1],side,side)
                pygame.draw.rect(screen,color,rect,max(1,brush_size//3))

            elif tool == 'right_triangle':  # Fixed: consistent name
                x1,y1 = start_pos
                x2,y2 = current_pos
                points = [(x1,y1),(x2,y1),(x1,y2)]
                pygame.draw.polygon(screen,color,points,max(1,brush_size//3))

            elif tool == 'equilateral':  # Fixed: consistent name
                x,y = start_pos
                side = abs(current_pos[0]-start_pos[0])
                h = int((math.sqrt(3)/2)*side)
                points = [(x,y),(x+side,y),(x+side//2,y-h)]
                pygame.draw.polygon(screen,color,points,max(1,brush_size//3))    

            elif tool == 'rhombus':
                x1,y1 = start_pos
                x2,y2 = current_pos
                midx = (x1 + x2) // 2
                midy = (y1 + y2) // 2
                points = [
                    (midx,y1),
                    (x2,midy),
                    (midx,y2),
                    (x1,midy)
                ]
                pygame.draw.polygon(screen,color,points,max(1,brush_size//3))

        # Simple info
        font = pygame.font.Font(None, 24)
        info = font.render(f"Tool: {tool} | Size: {brush_size}", True, (255, 255, 255))
        screen.blit(info, (10, 10))
        
        # Help text - Updated to match fixed tool names
        help_text = font.render("L:Line T:Rect O:Circle S:Square I:Right triangle ", True, (200, 200, 200))
        screen.blit(help_text, (10, 40))
        
        help2_text=font.render("Q:Equilateral triangle H:Rhombus E:Eraser SPACE:Clear",True,(200,200,200))
        screen.blit(help2_text, (10,70))

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