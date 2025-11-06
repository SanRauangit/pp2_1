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
    
    def move(self):
        # Get head position
        head_x, head_y = self.body[0]
        
        # Calculate new head position
        new_x = (head_x + self.direction[0]) % GRID_WIDTH
        new_y = (head_y + self.direction[1]) % GRID_HEIGHT
        new_head = (new_x, new_y)
        
        # Check if snake hits itself
        if new_head in self.body:
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
    def __init__(self, snake_body):
        self.position = self.get_random_position(snake_body)
    
    # spawn
    def get_random_position(self, snake_body):
        while True:
            pos = (random.randint(0, GRID_WIDTH - 1), 
                   random.randint(0, GRID_HEIGHT - 1))
            if pos not in snake_body:
                return pos
    
    # Draw
    def draw(self):
        rect = pygame.Rect(self.position[0] * GRID_SIZE, 
                          self.position[1] * GRID_SIZE, 
                          GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, RED, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)

def main():
    # Game variables
    snake = Snake()
    food = Food(snake.body)
    score = 0
    level = 1
    speed = 10
    foods_eaten = 0
    game_over = False
    
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
                    food = Food(snake.body)
                    score = 0
                    level = 1
                    speed = 10
                    foods_eaten = 0
                    game_over = False
        
        if not game_over:
            # Move snake
            if not snake.move():
                game_over = True
            
            # Check if snake eats food
            if snake.body[0] == food.position:
                snake.grow = True
                score += 10
                foods_eaten += 1
                food = Food(snake.body)
                
                # Level up every 3 foods
                if foods_eaten >= 3:
                    level += 1
                    speed += 2  # Increase speed
                    foods_eaten = 0
        
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