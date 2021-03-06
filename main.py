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

class Laser:
	def __init__(self, x, y, img):
		self.x = x
		self.y = y
		self.img = img
		self.mask = pygame.mask



class Ship:
	def __init__(self, x, y, health=100):
		self.x = x
		self.y = y
		self.health = health
		self.ship_img = None
		self.laser_img = None
		self.lasers = []
		self.cool_down_counter = 0
		
		
	def get_width(self):
		return self.ship_img.get_width()

	def get_height(self):
		return self.ship_img.get_height()

	def draw(self, window):
		window.blit(self.ship_img, (self.x, self.y))
		# pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50), 0)
		# above is rectangle to be used as dummy object

class Player(Ship):
	def __init__(self, x, y, health = 100):
		super().__init__(x, y, health)
		self.ship_img = YELLOW_SPACE_SHIP
		self.laser_img = YELLOW_LASER
		self.mask = pygame.mask.from_surface(self.ship_img)
		self.max_health = health

class Enemy(Ship):
	COLOR_MAP = {
				"red": (RED_SPACE_SHIP, RED_LASER),
				"green": (GREEN_SPACE_SHIP, GREEN_LASER),
				"blue": (BLUE_SPACE_SHIP, BLUE_LASER)
				}
	def __init__(self, x, y, color, health = 100):
		super().__init__(x, y, health)
		self.ship_img, self.laser_img = self.COLOR_MAP[color]
		self.mask = pygame.mask.from_surface(self.ship_img)

	def move(self, vel):
		self.y += vel


def main():
	run = True
	FPS = 60 # frame per sec - the higher the number, the faster it is
	level = 0
	lives = 5
	main_font = pygame.font.SysFont("comicsans", 50)
	lost_font = pygame.font.SysFont("comicsans", 62)

	enemies = []

	enemy_vel = 1
	wave_length = 5

	player_vel = 5 # velocity of pixels moved every time a key is pressed

	player = Player(300, 650)



	clock = pygame.time.Clock()

	lost = False
	lost_count = 0

	def redraw_window():
		WIN.blit(BG, (0,0)) # win is a surface, and blit() takes one of the pygame images such as a ship or laser, and draws it to the WIN surface
							# (0,0) is at the TOP-LEFT, not BOTTOM-LEFT like in Cartesian coordinates
		lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
		level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

		WIN.blit(lives_label, (10, 10))
		WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

		for enemy in enemies:
			enemy.draw(WIN)

		player.draw(WIN) # draw PLAYER is after the draw of ENEMY, because we want the PLAYER to be visible on top of ENEMY

		if lost:
			lost_label = lost_font.render("You lost", 1, (255, 255, 255))
			WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

		pygame.display.update() #refreshes the display

	while run:
		clock.tick(FPS) # to ensure game stays consistent regardless of the device being used
		redraw_window()
		
		if lives <= 0 or player.health <= 0:
			lost = True
			lost_count += 1

		if lost:
			if lost_count  > FPS * 3: # once 3 seconds have passed, quit the game
				run = False # ends game
			else:
				continue

		if len(enemies)==0: # if no.enemies reach 0
			level += 1 # increment level
			wave_length += 5 # increment no. of enemies we'd have
			for i in range(wave_length):
				enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-2222, -88), random.choice(["red", "green", "blue"]))
				enemies.append(enemy)


		for event in pygame.event.get(): # if event occurs, such as pressing a key, continue looping
			if event.type == pygame.QUIT:
				run = False
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and player.x - player_vel > 0:
			player.x -= player_vel
		if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH:
			player.x += player_vel
		if keys[pygame.K_UP] and player.y - player_vel > 0:
			player.y -= player_vel
		if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() < HEIGHT:
			player.y += player_vel

		for enemy in enemies:
			enemy.move(enemy_vel)
			if enemy.y + enemy.get_height() > HEIGHT: # if "this" enemy goes off the screen,
				lives -= 1
				enemies.remove(enemy) # remove enemy from the enemies list


main()