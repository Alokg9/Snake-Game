import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
block_size = 20
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Font
font_style = pygame.font.SysFont(None, 50)

# Snake parameters
snake_speed = 15
snake_block = 20
snake_list = []
snake_length = 1

# Accuracy variables
total_moves = 0
correct_moves = 0

# Functions
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])

def gameLoop():
    # Initialize variables
    game_over = False
    game_close = False
    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0
    global snake_length, total_moves, correct_moves

    # Generate random apple position
    apple_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
    apple_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size

    while not game_over:

        while game_close:
            screen.fill(white)
            display_message("You Lost! Press C to Play Again or Q to Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                total_moves += 1
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -block_size
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = block_size

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, red, [apple_x, apple_y, block_size, block_size])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        pygame.display.update()

        if x1 == apple_x and y1 == apple_y:
            apple_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
            apple_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size
            snake_length += 1
            correct_moves += 1

        clock = pygame.time.Clock()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
# Calculate accuracy
accuracy = (correct_moves / total_moves) * 100 if total_moves > 0 else 0
print("Accuracy: {:.2f}%".format(accuracy))
