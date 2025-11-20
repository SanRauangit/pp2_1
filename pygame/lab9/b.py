# Imports
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)

# Game settings
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("Arial", 25)

class Snake:
    def __init__(self):
        # Start in middle of screen
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.grow = False
    
    def move(self,walls):
        # Get head position
        head_x, head_y = self.body[0]
        
        # Calculate new head position
        new_x = head_x + self.direction[0]
        new_y = head_y + self.direction[1]
        new_head = (new_x, new_y)

        # Check wall collision
        if new_x < 0 or new_x >= GRID_WIDTH or new_y < 0 or new_y >= GRID_HEIGHT:
            return False
            
        
        # Check if snake hits itself
        if new_head in self.body:
            return False
        
        if new_head in walls:
            return False
        # Add new head
        self.body.insert(0, new_head)
        
        # Remove tail if not growing
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
            
        return True
    
    def change_direction(self, new_dir):
        # Prevent 180-degree turns
        if (new_dir[0] * -1, new_dir[1] * -1) != self.direction:
            self.direction = new_dir
    
    # Draw
    def draw(self):
        for segment in self.body:
            rect = pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, 
                             GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, GREEN, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

class Food:
    def __init__(self, snake_body,walls=None):
        if walls is None:
            walls = []
        self.position = self.get_random_position(snake_body,walls)
        self.value = random.choice([1,2,5])
        self.lifetime = 180 # approx 4 seconds
    
    # spawn
    def get_random_position(self, snake_body,walls):
        while True:
            pos = (random.randint(0, GRID_WIDTH - 1), 
                   random.randint(0, GRID_HEIGHT - 1))
            if pos not in snake_body and pos not in walls:
                return pos
            
    def update_timer(self):
        self.lifetime -= 1
        return self.lifetime <= 0
    
    # Draw
    def draw(self):
        rect = pygame.Rect(self.position[0] * GRID_SIZE, 
                          self.position[1] * GRID_SIZE, 
                          GRID_SIZE, GRID_SIZE)
        if self.value==1:
            color=(255,120,120)
        elif self.value==2:
            color=(255,70,70)
        else:
            color=(200,0,0)

        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)

def create_walls(level):
    walls=[]
    
    if level >= 2:
        # Horizontal barrier in the middle
        for x in range(5,GRID_WIDTH-5):
            walls.append((x,GRID_HEIGHT // 2))

    if level >= 3:
        # Vertical barriers
        for y in range(5,GRID_HEIGHT-5):
            walls.append((GRID_WIDTH // 4,y))
            walls.append((3*GRID_WIDTH // 4,y ))

    if level >= 4:
        # Cross pattern
        center_x,center_y = GRID_WIDTH // 2,GRID_HEIGHT // 2
        for i in range(-2,3):
            walls.append((center_x+i,center_y))
            walls.append((center_x,center_y+i))
    return walls

def draw_walls(walls):
    for wall in walls:
        rect=pygame.Rect(wall[0]*GRID_SIZE,wall[1]*GRID_SIZE,GRID_SIZE,GRID_SIZE)
        pygame.draw.rect(screen,BLUE,rect)
        pygame.draw.rect(screen,BLACK,rect,1)

def main():
    # Game variables
    snake = Snake()
    walls = create_walls(1)
    food = Food(snake.body,walls)
    score = 0
    level = 1
    base_speed = 10
    speed = base_speed
    foods_eaten = 0
    foods_for_next_level = 3
    game_over = False
    wall_collision_enabled = True
    
    # Main game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if not game_over:
                    # Change direction
                    if event.key == pygame.K_UP:
                        snake.change_direction(UP)
                    elif event.key == pygame.K_DOWN:
                        snake.change_direction(DOWN)
                    elif event.key == pygame.K_LEFT:
                        snake.change_direction(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        snake.change_direction(RIGHT)
                
                # Restart game
                if event.key == pygame.K_r and game_over:
                    snake = Snake()
                    walls = create_walls(level)
                    food = Food(snake.body,walls)
                    score = 0
                    level = 1
                    speed = 10
                    foods_eaten = 0
                    game_over = False
        
        if not game_over:
            # Move snake
            if not snake.move(walls):
                game_over = True
            
            # Check if snake eats food
            if snake.body[0] == food.position:
                snake.grow = True
                score += food.value
                foods_eaten += 1
                food = Food(snake.body,walls)
                
                # Level up every 3 foods
                if foods_eaten >= foods_for_next_level:
                    level += 1
                    speed = base_speed + (level-1) * 2  # Increase speed
                    walls = create_walls(level)
                    foods_eaten = 0
                    food = Food(snake.body,walls)
                
            if food.update_timer():
                food = Food(snake.body,walls)
        
        # fill w white
        screen.fill(WHITE)
        
        # Draw kletka lines
        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, (200, 200, 200), (0, y), (WIDTH, y))
        
        # Draw game objects
        snake.draw()
        food.draw()
        draw_walls(walls)
        # score,level texts
        score_text = font.render(f"Score: {score}", True, BLACK)
        level_text = font.render(f"Level: {level}", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 40))
        
        # Game over screen
        if game_over:
            game_over_text = font.render("GAME OVER - Press R to restart", True, RED)
            screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))
        
        # Update display
        pygame.display.flip()
        
        #game speed
        clock.tick(speed)

if __name__ == "__main__":
    main()