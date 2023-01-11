import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Two-Player Pong")

# Define some colors
white = (255, 255, 255)
black = (0, 0, 0)

# Create the player paddles
paddle1 = pygame.Rect(20, 250, 20, 100)
paddle2 = pygame.Rect(760, 250, 20, 100)

# Create the ball
ball = pygame.Rect(390, 290, 20, 20)

# Set the initial speed of the ball
ball_speed = [1, -1]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player 1's paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.y -= 5
    if keys[pygame.K_s]:
        paddle1.y += 5

    # Move player 2's paddle
    if keys[pygame.K_i]:
        paddle2.y -= 5
    if keys[pygame.K_k]:
        paddle2.y += 5

    # Move the ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Check for collision with top and bottom of screen
    if ball.top <= 0 or ball.bottom >= 600:
        ball_speed[1] = -ball_speed[1]

    # Check for collision with left and right of screen
    if ball.left <= 0:
        ball_speed[0] = -ball_speed[0]
    if ball.right >= 800:
        ball_speed[0] = -ball_speed[0]

    # Check for collision with player paddles
    if ball.colliderect(paddle1):
        ball_speed[0] = abs(ball_speed[0])
    elif ball.colliderect(paddle2):
        ball_speed[0] = -abs(ball_speed[0])

    # Draw everything
    screen.fill(black)
    pygame.draw.rect(screen, white, paddle1)
    pygame.draw.rect(screen, white, paddle2)
    pygame.draw.ellipse(screen, white, ball)
    pygame.display.flip()

# Clean up Pygame
pygame.quit()
