"""Class of the maze game"""

import pygame
from pygame.locals import *
from constants_maze import *


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