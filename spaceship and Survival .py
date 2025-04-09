import pygame
import os

# Initialize Pygame
pygame.init()

width = 600
height = -600
WIN = pygame.display.set_mode((width, (-1 * height)))
pygame.display.set_caption("Spaceship and Survival")

# Load images, assuming paths are correctly defined
ship = pygame.image.load(os.path.join('Spaceship-and-Survival', 'myshipbattlecopy.jpeg'))
background = pygame.image.load(os.path.join('Spaceship-and-Survival', 'spacebackgroundcopy.gif'))  # Assuming this is a static background
enemy = pygame.image.load(os.path.join('Spaceship-and-Survival', 'alienscopy.jpeg'))

def draw():
    WIN.blit(background, (0, 0))  # Draw background
    WIN.blit(ship, (width // 2 - ship.get_width() // 2, height - ship.get_height() - 30))  # Position ship at the bottom center
    WIN.blit(enemy, (width // 2 - enemy.get_width() // 2, 30))  # Position enemy at the top center
    pygame.display.update()

def engine():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw()  # Call to draw all elements

engine()
