"""Class of the maze game"""

import random
import pygame

from constants_maze import WALL_IMAGE, DEPARTURE_IMAGE, GARDIAN_IMAGE, \
    ETHER_IMAGE, PLASTIC_IMAGE, SPRITE_SIZE, NUMBER_SPRITES_SIDE, SYRINGE_IMAGE, NEEDLE_IMAGE


class Start:
    """Class used to create the start of the game"""

    def __init__(self, file):
        self.file = file
        self.structure = 0

    def generate(self):
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
            # We save this structure
            self.structure = structure_level

            # We all browse the file, we save the i and j position of the empty space (0)
            pos_available = [(i, j) for j, line in enumerate(self.structure)
                             for i, val in enumerate(line)
                             if val == '0']
            random.shuffle(pos_available)
            i, j = pos_available.pop()  # We pop from a random position for the serynge(s)
            self.structure[j][i] = 's'
            i, j = pos_available.pop()  # We pop from a random position for the needle(n)
            self.structure[j][i] = 'n'
            i, j = pos_available.pop()  # We pop from a random position for the ether(e)
            self.structure[j][i] = 'e'
            i, j = pos_available.pop()  # We pop from a random position for the plastic(p)
            self.structure[j][i] = 'p'

    def show(self, window):
        """Method to display the level according to
        of the structure list returned by generate ()"""

        # Loading images (only the arrival one contains transparency)
        wall = pygame.image.load(WALL_IMAGE).convert()
        departure = pygame.image.load(DEPARTURE_IMAGE).convert_alpha()
        arrived = pygame.image.load(GARDIAN_IMAGE).convert_alpha()
        syringe = pygame.image.load(SYRINGE_IMAGE).convert_alpha()
        needle = pygame.image.load(NEEDLE_IMAGE).convert_alpha()
        ether = pygame.image.load(ETHER_IMAGE).convert_alpha()
        plastic = pygame.image.load(PLASTIC_IMAGE).convert_alpha()

        # We go through the list of the level
        number_line = 0
        for line in self.structure:
            # We go through the lists of lines
            num_case = 0
            for sprite in line:
                # We calculate the real position in pixels
                x = num_case * SPRITE_SIZE
                y = number_line * SPRITE_SIZE
                if sprite == 'w':  # w = Wall
                    window.blit(wall, (x, y))
                elif sprite == 'd':  # d = Departure
                    window.blit(departure, (x, y))
                elif sprite == 'a':  # a = Arrived
                    window.blit(arrived, (x, y))
                elif sprite == 's':  # s = syringe
                    window.blit(syringe, (x, y))
                elif sprite == 'n':  # n = needle
                    window.blit(needle, (x, y))
                elif sprite == 'e':  # e = ether
                    window.blit(ether, (x, y))
                elif sprite == 'p':  # p = plastic
                    window.blit(plastic, (x, y))

                num_case += 1
            number_line += 1


class Person:
    """Class used to create a character"""

    def __init__(self, right, left, top, bottom, start):
        # Character sprites
        self.right = pygame.image.load(right).convert_alpha()
        self.left = pygame.image.load(left).convert_alpha()
        self.top = pygame.image.load(top).convert_alpha()
        self.bottom = pygame.image.load(bottom).convert_alpha()
        # Position of the character in squares and pixels
        self.box_x = 0
        self.box_y = 0
        self.x = 0
        self.y = 0
        # Default direction
        self.direction = self.right
        # Start of the game
        self.start = start
        self.counter = 0

    def move(self, direction):
        """Method for moving the character"""

        # Moving to the right
        if direction == 'right':
            # Not to exceed the screen
            if self.box_x < (NUMBER_SPRITES_SIDE - 1):
                # We check that the destination square is not a wall
                if self.start.structure[self.box_y][self.box_x + 1] != 'w':
                    # Moving a box
                    self.box_x += 1
                    # Calculation of the "real" position in pixels
                    self.x = self.box_x * SPRITE_SIZE
            # main character image
            self.direction = self.right

        # Move to the left
        if direction == 'left':
            if self.box_x > 0:
                if self.start.structure[self.box_y][self.box_x - 1] != 'w':
                    self.box_x -= 1
                    self.x = self.box_x * SPRITE_SIZE
            self.direction = self.left

        # Moving up
        if direction == 'top':
            if self.box_y > 0:
                if self.start.structure[self.box_y - 1][self.box_x] != 'w':
                    self.box_y -= 1
                    self.y = self.box_y * SPRITE_SIZE
            self.direction = self.top

        # Moving down
        if direction == 'bottom':
            if self.box_y < (NUMBER_SPRITES_SIDE - 1):
                if self.start.structure[self.box_y + 1][self.box_x] != 'w':
                    self.box_y += 1
                    self.y = self.box_y * SPRITE_SIZE
            self.direction = self.bottom

        # We collect the serynge
        if self.start.structure[self.box_y][self.box_x] == 's':
            self.start.structure[self.box_y][self.box_x] = '0'
            self.counter += 1
            print("Seringue ramassé !")

        # We collect the plastic
        if self.start.structure[self.box_y][self.box_x] == 'p':
            self.start.structure[self.box_y][self.box_x] = '0'
            self.counter += 1
            print("Tube Plastique ramassé !")

        # We collect the needle
        if self.start.structure[self.box_y][self.box_x] == 'n':
            self.start.structure[self.box_y][self.box_x] = '0'
            self.counter += 1
            print("Aiguille ramassée !")

        # We collect the ether
        if self.start.structure[self.box_y][self.box_x] == 'e':
            self.start.structure[self.box_y][self.box_x] = '0'
            self.counter += 1
            print("Ether ramassé !")
