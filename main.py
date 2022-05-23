import os
import time
import random
import pygame

WIDTH, HEIGHT = 750, 750 # can be modified later if we want
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space War")

# Load Images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png")) #from assets folder, load the red-small PNG file
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Player Ship

YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png")) #an alternative way to import file other than the os.path.join above

# Lasers

RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

#Background
BG = pygame.image.load(os.path.join("assets", "background-black.png"))

def main():
	run = True
	FPS = 60 # frame per sec - the higher the number, the faster it is
	clock = pygame.time.Clock()

	while run:
		clock.tick(FPS) # to ensure game stays consistent regardless of the device being used

		for event in pygame.event.get(): # if event occurs, such as pressing a key, continue looping
			if event.type == pygame.QUIT:
				run = False

main()