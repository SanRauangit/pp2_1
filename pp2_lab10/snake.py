# Imports
import pygame
import random
import sys
import psycopg2
import json
from datetime import datetime

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

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
small_font = pygame.font.SysFont("Arial", 20)

class DatabaseManager:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="snake", 
            user="postgres",
            password="1204",  
            host="localhost",
            port="5432"
        )
    
    def get_or_create_user(self, username):
        with self.conn.cursor() as cur:
            # Check if user exists
            cur.execute("SELECT id, username FROM users WHERE username = %s", (username,))
            user = cur.fetchone()
            
            if user:
                return user[0]  # Return user_id
            else:
                # Create new user
                cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
                self.conn.commit()
                return cur.fetchone()[0]
    
    def get_user_stats(self, user_id):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT MAX(score), MAX(level) 
                FROM user_scores 
                WHERE user_id = %s
            """, (user_id,))
            result = cur.fetchone()
            return result if result else (0, 1)
    
    def save_game_state(self, user_id, score, level, foods_eaten, snake_body, walls, food_position, food_value):
        game_data = {
            "snake_body": snake_body,
            "walls": walls,
            "food_position": food_position,
            "food_value": food_value,
            "saved_at": datetime.now().isoformat()
        }
        
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO user_scores (user_id, score, level, foods_eaten, game_data)
                VALUES (%s, %s, %s, %s, %s)
            """, (user_id, score, level, foods_eaten, json.dumps(game_data)))
            self.conn.commit()
    
    def get_level_config(self, level):
        with self.conn.cursor() as cur:
            cur.execute("SELECT speed, walls_config, foods_for_next_level FROM game_levels WHERE level = %s", (level,))
            return cur.fetchone()
    
    def close(self):
        self.conn.close()

class Snake:
    def __init__(self, body=None):
        if body is None:
            self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        else:
            self.body = body
        self.direction = RIGHT
        self.grow = False
    
    def move(self, walls):
        head_x, head_y = self.body[0]
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
        if (new_dir[0] * -1, new_dir[1] * -1) != self.direction:
            self.direction = new_dir

    def draw(self):
        for segment in self.body:
            rect = pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, 
                             GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, GREEN, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

class Food:
    def __init__(self, snake_body, walls=None, position=None, value=None):
        if walls is None:
            walls = []
        
        if position and value:
            self.position = position
            self.value = value
        else:
            self.position = self.get_random_position(snake_body, walls)
            self.value = random.choice([1, 2, 5])
        
        self.lifetime = 180
    
    def get_random_position(self, snake_body, walls):
        while True:
            pos = (random.randint(0, GRID_WIDTH - 1), 
                   random.randint(0, GRID_HEIGHT - 1))
            if pos not in snake_body and pos not in walls:
                return pos
            
    def update_timer(self):
        self.lifetime -= 1
        return self.lifetime <= 0

    def draw(self):
        rect = pygame.Rect(self.position[0] * GRID_SIZE, 
                          self.position[1] * GRID_SIZE, 
                          GRID_SIZE, GRID_SIZE)
        if self.value == 1:
            color = (255, 120, 120)
        elif self.value == 2:
            color = (255, 70, 70)
        else:
            color = (200, 0, 0)

        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)

def create_walls(level):
    walls = []
    
    if level >= 2:
        # Horizontal barrier in the middle
        for x in range(5, GRID_WIDTH - 5):
            walls.append((x, GRID_HEIGHT // 2))

    if level >= 3:
        # Vertical barriers
        for y in range(5, GRID_HEIGHT - 5):
            walls.append((GRID_WIDTH // 4, y))
            walls.append((3 * GRID_WIDTH // 4, y))

    if level >= 4:
        # Cross pattern
        center_x, center_y = GRID_WIDTH // 2, GRID_HEIGHT // 2
        for i in range(-2, 3):
            walls.append((center_x + i, center_y))
            walls.append((center_x, center_y + i))
    
    if level >= 5:
        # Corner walls
        for i in range(3):
            walls.append((i, i))
            walls.append((GRID_WIDTH - 1 - i, i))
            walls.append((i, GRID_HEIGHT - 1 - i))
            walls.append((GRID_WIDTH - 1 - i, GRID_HEIGHT - 1 - i))
    
    return walls

def draw_walls(walls):
    for wall in walls:
        rect = pygame.Rect(wall[0] * GRID_SIZE, wall[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, BLUE, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)

def get_username():
    username = ""
    input_active = True
    
    while input_active:
        screen.fill(WHITE)
        
        # Display prompt
        prompt_text = font.render("Enter your username:", True, BLACK)
        username_text = font.render(username, True, BLACK)
        instruction_text = small_font.render("Press ENTER to continue", True, BLACK)
        
        screen.blit(prompt_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
        screen.blit(username_text, (WIDTH // 2 - 50, HEIGHT // 2))
        screen.blit(instruction_text, (WIDTH // 2 - 100, HEIGHT // 2 + 50))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and username:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    # Add character if it's alphanumeric and length is reasonable
                    if event.unicode.isalnum() and len(username) < 15:
                        username += event.unicode
        
        pygame.display.flip()
        clock.tick(30)
    
    return username

def show_user_stats(db, user_id):
    high_score, current_level = db.get_user_stats(user_id)
    
    showing = True
    while showing:
        screen.fill(WHITE)
        
        stats_text = font.render(f"Welcome back!", True, BLACK)
        level_text = font.render(f"Your current level: {current_level}", True, BLACK)
        score_text = font.render(f"Your highest score: {high_score}", True, BLACK)
        continue_text = font.render("Press SPACE to continue", True, BLACK)
        
        screen.blit(stats_text, (WIDTH // 2 - 80, HEIGHT // 2 - 60))
        screen.blit(level_text, (WIDTH // 2 - 120, HEIGHT // 2 - 20))
        screen.blit(score_text, (WIDTH // 2 - 120, HEIGHT // 2 + 20))
        screen.blit(continue_text, (WIDTH // 2 - 120, HEIGHT // 2 + 60))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    showing = False
        
        pygame.display.flip()
        clock.tick(30)

def show_pause_menu(db, user_id, score, level, foods_eaten, snake, walls, food):
    paused = True
    
    while paused:
        screen.fill(WHITE)
        
        pause_text = font.render("GAME PAUSED", True, BLACK)
        save_text = font.render("Press S to save game", True, BLACK)
        resume_text = font.render("Press P to resume", True, BLACK)
        quit_text = font.render("Press Q to quit", True, BLACK)
        
        screen.blit(pause_text, (WIDTH // 2 - 80, HEIGHT // 2 - 60))
        screen.blit(save_text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
        screen.blit(resume_text, (WIDTH // 2 - 80, HEIGHT // 2 + 20))
        screen.blit(quit_text, (WIDTH // 2 - 60, HEIGHT // 2 + 60))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                elif event.key == pygame.K_s:
                    # Save game state
                    db.save_game_state(user_id, score, level, foods_eaten, 
                                     snake.body, walls, food.position, food.value)
                    saved_text = font.render("Game saved!", True, GREEN)
                    screen.blit(saved_text, (WIDTH // 2 - 60, HEIGHT // 2 + 100))
                    pygame.display.flip()
                    pygame.time.wait(1000)
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        
        pygame.display.flip()
        clock.tick(30)
    
    return False

def main():
    # Initialize database
    db = DatabaseManager()
    
    # Get username
    username = get_username()
    user_id = db.get_or_create_user(username)
    
    # Show user stats if returning user
    show_user_stats(db, user_id)
    
    # Game variables
    snake = Snake()
    level = 1
    level_config = db.get_level_config(level)
    if level_config:
        base_speed, walls_config, foods_for_next_level = level_config
    else:
        base_speed, foods_for_next_level = 10, 3
        walls_config = {"walls": []}
    
    walls = create_walls(level)
    food = Food(snake.body, walls)
    score = 0
    speed = base_speed
    foods_eaten = 0
    game_over = False
    
    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                db.close()
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
                    # Pause game (shortcut: P key)
                    elif event.key == pygame.K_p:
                        show_pause_menu(db, user_id, score, level, foods_eaten, snake, walls, food)
                
                # Restart game
                if event.key == pygame.K_r and game_over:
                    snake = Snake()
                    level = 1
                    level_config = db.get_level_config(level)
                    if level_config:
                        base_speed, walls_config, foods_for_next_level = level_config
                    walls = create_walls(level)
                    food = Food(snake.body, walls)
                    score = 0
                    speed = base_speed
                    foods_eaten = 0
                    game_over = False
        
        if not game_over:
            # Move snake
            if not snake.move(walls):
                game_over = True
                # Save final score
                db.save_game_state(user_id, score, level, foods_eaten, 
                                 snake.body, walls, food.position, food.value)
            
            # Check if snake eats food
            if snake.body[0] == food.position:
                snake.grow = True
                score += food.value
                foods_eaten += 1
                food = Food(snake.body, walls)
                
                # Level up
                if foods_eaten >= foods_for_next_level:
                    level += 1
                    level_config = db.get_level_config(level)
                    if level_config:
                        base_speed, walls_config, foods_for_next_level = level_config
                    speed = base_speed
                    walls = create_walls(level)
                    foods_eaten = 0
                    food = Food(snake.body, walls)
            
            if food.update_timer():
                food = Food(snake.body, walls)
        
        # Draw everything
        screen.fill(WHITE)
        
        # Draw grid lines
        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, (200, 200, 200), (0, y), (WIDTH, y))
        
        # Draw game objects
        snake.draw()
        food.draw()
        draw_walls(walls)
        
        # Draw UI
        score_text = font.render(f"Score: {score}", True, BLACK)
        level_text = font.render(f"Level: {level}", True, BLACK)
        username_text = small_font.render(f"Player: {username}", True, BLACK)
        pause_text = small_font.render("Press P to pause", True, BLACK)
        
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 40))
        screen.blit(username_text, (10, 70))
        screen.blit(pause_text, (10, 100))
        
        # Game over screen
        if game_over:
            game_over_text = font.render("GAME OVER - Press R to restart", True, RED)
            screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))
        
        pygame.display.flip()
        clock.tick(speed)
    
    db.close()

if __name__ == "__main__":
    main()