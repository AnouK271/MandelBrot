import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600 
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player settings
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size
player_speed = 5
player_jump = -15
gravity = 1
falling = False  # Flag to track if the player has jumped

# Platform settings
platform_width = 100
platform_height = 10
platform_speed = 3
platform_gap = 300
platform_spawn_chance = 10

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doodle Jump")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Font for displaying score
font = pygame.font.Font(None, 36)


# Function to draw the player
def draw_player(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, player_size, player_size))


# Function to draw a platform
def draw_platform(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, platform_width, platform_height))


# Function to display the score
def display_score(score):
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))


# Game loop
score = 0
platforms = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Move player left and right
    player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed

    # Jump when the space key is pressed and the player is on the ground
    if keys[pygame.K_SPACE] and player_y >= HEIGHT - 2 * player_size and not falling:
        player_y += player_jump
        falling = True

    # Apply gravity to the player if falling
    if falling:
        player_y += gravity

    # Move platforms down
    for platform in platforms:
        platform[1] += platform_speed

    # Generate new platforms
    if random.randint(0, 100) < platform_spawn_chance:
        platforms.append([random.randint(0, WIDTH - platform_width), 0])

    # Check for collision with platforms
    for platform in platforms:
        if (
                player_y < platform[1] + platform_height
                and player_y + player_size > platform[1]
                and player_x < platform[0] + platform_width
                and player_x + player_size > platform[0]
        ):
            # Jump if there is a collision
            player_y = platform[1] - player_size
            falling = False  # Reset the falling flag
            score += 1  # Increase score when jumping on a platform

    # Remove off-screen platforms
    platforms = [platform for platform in platforms if platform[1] < HEIGHT]

    # Draw everything
    screen.fill(WHITE)
    draw_player(player_x, player_y)
    for platform in platforms:
        draw_platform(platform[0], platform[1])
    display_score(score)

    pygame.display.flip()
    clock.tick(FPS)








