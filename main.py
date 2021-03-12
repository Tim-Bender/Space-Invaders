import pygame
import os
import time
import random

# Load assets
RED_SPACE_SHIP = pygame.image.load(os.path.join("images", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("images", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("images", "pixel_ship_blue_small.png"))

YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("images", "pixel_ship_yellow.png"))

RED_LASER = pygame.image.load(os.path.join("images", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("images", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("images", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("images", "pixel_laser_yellow.png"))

BG = pygame.image.load(os.path.join("images", "background-black.png"))

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")


def main():
    run = True
    fps = 60
    clock = pygame.time.Clock()
    while run:
        clock.tick(fps)
        for event in pygame.event.get():


