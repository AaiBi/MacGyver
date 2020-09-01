"""Class of the maze game"""

import pygame
from pygame.locals import *
from constants_maze import *
import random


class Start:
    """Class used to create the start of the game"""

    def __init__(self, file):
        self.file = file
        self.structure = 0

    def generer(self):
        """Method for generating the start based on the file.
        we create a general list, containing one list per line to display"""
        # We open the file
        with open(self.file, "r") as file:
            structure_level = []
            # We browse the lines of the file
            for line in file:
                line_level = []
                # We browse the sprites (letters) contained in the file
                for sprite in line:
                    # We ignore the end of line "\ n"
                    if sprite != '\n':
                        # We add the sprite to the list of the line
                        line_level.append(sprite)
                # Add the line to the level list
                structure_level.append(line_level)

                # We go through the list of the level
                number_line = 0
                table_0 = []
                for line in structure_level:
                    # On parcourt les listes de lignes
                    num_case = 0
                    for sprite in line:
                        # We calculate the real position in pixels
                        x = num_case * sprite_size
                        y = number_line * sprite_size
                        if sprite == '0':  # 0 = empty space
                            table_0.append([x,y])

                            sampling = random.choices(table_0, k=3)
                            for value in sampling:
                                sprite = 's'

                        num_case += 1
                    number_line += 1
            print(table_0)

            print(sampling)
            # We save this structure
            self.structure = structure_level

    def show(self, window):
        """Méthode permettant d'afficher le niveau en fonction
        de la liste de structure renvoyée par generer()"""
        # Chargement des images (seule celle d'arrivée contient de la transparence)
        wall = pygame.image.load(wall_image).convert()
        departure = pygame.image.load(departure_image).convert_alpha()
        arrived = pygame.image.load(Gardien_image).convert_alpha()
        syringe = pygame.image.load(syringe_image).convert_alpha()

        # We go through the list of the level
        number_line = 0
        for line in self.structure:
            # On parcourt les listes de lignes
            num_case = 0
            for sprite in line:
                # We calculate the real position in pixels
                x = num_case * sprite_size
                y = number_line * sprite_size
                if sprite == 'w':  # w = Wall
                    window.blit(wall, (x, y))
                elif sprite == 'd':  # d = Départure
                    window.blit(departure, (x, y))
                elif sprite == 'a':  # a = Arrived
                    window.blit(arrived, (x, y))
                elif sprite == 's':  # s = syringe
                    window.blit(syringe, (x, y))

                num_case += 1
            number_line += 1


class Person:
    """Class used to create a character"""

    def __init__(self, right, left, top, bottom, start):
        # Character sprites
        self.right = self.left = self.top = self.bottom = pygame.image.load(right).convert_alpha()
        # Position of the character in squares and pixels
        self.box_x = 0
        self.box_y = 0
        self.x = 0
        self.y = 0
        # Default direction
        self.direction = self.right
        # Start of the game
        self.start = start

    def move(self, direction):
        """Method for moving the character"""

        # Moving to the right
        if direction == 'right':
            # Not to exceed the screen
            if self.box_x < (number_sprites_side - 1):
                # We check that the destination square is not a wall
                if self.start.structure[self.box_y][self.box_x + 1] != 'w':
                    # Moving a box
                    self.box_x += 1
                    # Calculation of the "real" position in pixels
                    self.x = self.box_x * sprite_size
            # main character image
            self.direction = self.right

        # Move to the left
        if direction == 'left':
            if self.box_x > 0:
                if self.start.structure[self.box_y][self.box_x - 1] != 'w':
                    self.box_x -= 1
                    self.x = self.box_x * sprite_size
            self.direction = self.left

        # Moving up
        if direction == 'top':
            if self.box_y > 0:
                if self.start.structure[self.box_y - 1][self.box_x] != 'w':
                    self.box_y -= 1
                    self.y = self.box_y * sprite_size
            self.direction = self.top

        # Moving down
        if direction == 'bottom':
            if self.box_y < (number_sprites_side - 1):
                if self.start.structure[self.box_y + 1][self.box_x] != 'w':
                    self.box_y += 1
                    self.y = self.box_y * sprite_size
            self.direction = self.bottom
