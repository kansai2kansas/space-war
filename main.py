import pygame
import os
import time
import random


pygame.font.init()

WIDTH, HEIGHT = 888, 888 # can be modified later if we want
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
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

class Ship:
	def __init__(self, x, y, health=100):
		self.x = x
		self.y = y
		self.health = health
		self.laser_img = None
		self.lasers = []
		self.cool_down_counter = 0

	def draw(self, window):
		pygame.draw.rect


def main():
	run = True
	FPS = 60 # frame per sec - the higher the number, the faster it is
	level = 1
	lives = 5
	main_font = pygame.font.SysFont("comicsans", 50)

	clock = pygame.time.Clock()

	def redraw_window():
		WIN.blit(BG, (0,0)) # win is a surface, and blit() takes one of the pygame images such as a ship or laser, and draws it to the WIN surface
							# (0,0) is at the TOP-LEFT, not BOTTOM-LEFT like in Cartesian coordinates
		lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
		level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

		WIN.blit(lives_label, (10, 10))
		WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))



		pygame.display.update() #refreshes the display

	while run:
		clock.tick(FPS) # to ensure game stays consistent regardless of the device being used
		redraw_window()
		for event in pygame.event.get(): # if event occurs, such as pressing a key, continue looping
			if event.type == pygame.QUIT:
				run = False

main()