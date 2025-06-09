import random
import pygame

# Simulation parameters
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)  # white background (transparent box concept)
BALL_COLOR = (30, 144, 255)  # dodger blue
NUM_BALLS = 20
BALL_RADIUS = 10
MAX_SPEED = 5

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Brownian Motion Simulation')
clock = pygame.time.Clock()

class Ball:
    def __init__(self):
        self.x = random.uniform(BALL_RADIUS, WIDTH - BALL_RADIUS)
        self.y = random.uniform(BALL_RADIUS, HEIGHT - BALL_RADIUS)
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)

    def update(self):
        # Add small random acceleration to simulate Brownian noise
        self.vx += random.uniform(-1, 1)
        self.vy += random.uniform(-1, 1)

        # Limit speed
        self.vx = max(min(self.vx, MAX_SPEED), -MAX_SPEED)
        self.vy = max(min(self.vy, MAX_SPEED), -MAX_SPEED)

        self.x += self.vx
        self.y += self.vy

        # Bounce off walls
        if self.x <= BALL_RADIUS or self.x >= WIDTH - BALL_RADIUS:
            self.vx = -self.vx
            self.x = max(BALL_RADIUS, min(self.x, WIDTH - BALL_RADIUS))
        if self.y <= BALL_RADIUS or self.y >= HEIGHT - BALL_RADIUS:
            self.vy = -self.vy
            self.y = max(BALL_RADIUS, min(self.y, HEIGHT - BALL_RADIUS))

    def draw(self, surface):
        pygame.draw.circle(surface, BALL_COLOR, (int(self.x), int(self.y)), BALL_RADIUS)

balls = [Ball() for _ in range(NUM_BALLS)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    for ball in balls:
        ball.update()
        ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)  # Limit to 60 FPS

pygame.quit()
