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
#Icon
icon = pygame.image.load(icon_image)
pygame.display.set_icon(icon)
#Title
pygame.display.set_caption(window_title)


class Start:
	"""Class used to create the start of the game"""
	def __init__(self, file):
		self.file = file
		self.structure = 0


class Person:
	"""Class used to create a character"""
	def __init__(self, right, left, top, bottom, start):
		#Character sprites
		self.right = self.left = self.top = self.bottom = pygame.image.load(right).convert_alpha()
		#Position of the character in squares and pixels
		self.box_x = 0
		self.box_y = 0
		self.x = 0
		self.y = 0
		#Default direction
		self.direction = self.right
		#Start of the game
		self.start = start