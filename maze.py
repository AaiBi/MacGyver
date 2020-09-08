#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
MacGyver, maze game
MacGyver must move through a labyrinth to collect items that will allow him to kill the guardian and
finish the game.

files : maze.py, classes_maze.py, constants_maze.py. README.md
folder : ressource, .idea
"""

import random
import pygame
from pygame.locals import *

from classes_maze import *
from constants_maze import *

pygame.init()

#Opening the Pygame window (square: width = height)
window = pygame.display.set_mode((window_side, window_side))
#Title
pygame.display.set_caption(window_title)
font = pygame.font.Font(None, 24)
text = font.render("Biejdhsw	hkhwkjjwhkjkjdwkjjn ", 1, (255, 255, 255))

# Main loop
repeat = 1
while repeat:
	# Loading and viewing the home screen
	home = pygame.image.load(home_image).convert()
	window.blit(home, (0, 0))
	window.blit(text, (300, 300))

	# Refreshment
	pygame.display.flip()

	# We reset these variables to 1 at each loop round
	repeat_game = 1
	repeat_home = 1

	#Counter for the number of objects collected
	counter = 0

	# Home loop
	while repeat_home:

		# Loop speed limitation
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			# If the user quits, we put the variables loop to 0 to cycle through none and close
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				repeat_home = 0
				repeat_game = 0
				repeat = 0
				# Level choice variable
				choice = 0

			elif event.type == KEYDOWN:
				# Launch of the game
				if event.key == K_F1:
					repeat_home = 0  # we leaves the home page
					choice = 'maze_file'  # We launch the loading of maze_file which contains the labyrinth

	# We check that the player has clicked on F1 for not charge the file if he leaves
	if choice != 0:
		# launch of the background
		fond = pygame.image.load(background_image).convert()

		# Generation of the maze_file, file containing the labyrinth
		start = Start(choice)
		start.generer()
		start.show(window)

		# Creation of the game
		mg = Person(image_mac, image_mac, image_mac, image_mac, start)  # mg = MacGyver

	# Game loop
	while repeat_game:

			# Loop speed limitation
			pygame.time.Clock().tick(30)

			for event in pygame.event.get():

				# If the user quits, we set the variable that continues the game
				# ET the general variable to 0 to close the window
				if event.type == QUIT:
					repeat_game = 0
					repeat = 0

				elif event.type == KEYDOWN:
					# If the user presses Esc here, we only return to the menu
					if event.key == K_ESCAPE:
						repeat_game = 0

					# MacGyver navigation keys
					elif event.key == K_RIGHT:
						mg.move('right')
					elif event.key == K_LEFT:
						mg.move('left')
					elif event.key == K_UP:
						mg.move('top')
					elif event.key == K_DOWN:
						mg.move('bottom')

			# Displays at new positions
			window.blit(fond, (0, 0))
			start.show(window)
			window.blit(mg.direction, (mg.x, mg.y))  # direction
			pygame.display.flip()

			#We collect the serynge
			if start.structure[mg.box_y][mg.box_x] == 's':
				start.structure[mg.box_y][mg.box_x] = '0'
				counter += 1
				print("Seringue ramassé !")
			# We collect the plastic
			if start.structure[mg.box_y][mg.box_x] == 'p':
				start.structure[mg.box_y][mg.box_x] = '0'
				counter += 1
				print("Tube Plastique ramassé !")
			# We collect the needle
			if start.structure[mg.box_y][mg.box_x] == 'n':
				start.structure[mg.box_y][mg.box_x] = '0'
				counter += 1
				print("Aiguille ramassée !")
			# We collect the ether
			if start.structure[mg.box_y][mg.box_x] == 'e':
				start.structure[mg.box_y][mg.box_x] = '0'
				counter += 1
				print("Ether ramassé !")

			if counter >= 4:
				# Back to home page
				if start.structure[mg.box_y][mg.box_x] == 'a':
					repeat_game = 0
			elif counter != 0 and counter < 4 and start.structure[mg.box_y][mg.box_x] == 'a':
				print("GAME OVER !!!! Echec, mort de Mac Gyver")
				repeat_game = 0