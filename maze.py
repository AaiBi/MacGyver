#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
MacGyver, maze game
MacGyver must move through a labyrinth to collect items that will allow him to kill the guardian and
finish the game.

files : maze.py, classes_maze.py, constants_maze.py. README.md
folder : ressource, .idea
"""

from pygame.locals import QUIT, KEYDOWN, K_F1, K_ESCAPE, K_RIGHT, K_LEFT, K_UP, K_DOWN

from classes_maze import Start, Person, pygame
from constants_maze import WINDOW_SIZE, WINDOW_TITLE, HOME_IMAGE, MACGYVER_IMAGE, BACKGROUND_IMAGE
import time


class LaunchGame:
    """Class used to launch the game"""

    pygame.init()

    # Opening the Pygame window (square: width = height)
    window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    # Title
    pygame.display.set_caption(WINDOW_TITLE)

    # Font for the game over window
    font = pygame.font.SysFont("comicsansms", 13)
    font1 = pygame.font.SysFont("comicsansms", 40)
    # Text for the game over window
    text = font.render("GAME OVER ! Un ou des objet(s) n'a (n'ont) pas été ramassé(s)", True, (0, 128, 0))
    # Text for when you win the game
    text1 = font1.render("PARTIE REUSSIE !", True, (0, 128, 0))

    # Main loop
    repeat = 1

    while repeat:
        # Loading and viewing the home screen
        home = pygame.image.load(HOME_IMAGE).convert()
        window.blit(home, (0, 0))

        # Refreshment
        pygame.display.flip()

        # We reset these variables to 1 at each loop round
        repeat_game = 1
        repeat_home = 1

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
                        choice = 'maze_file'  # We launch the loading
                        # of maze_file which contains the labyrinth

        # We check that the player has clicked on F1 for not charge the file if he leaves
        if choice != 0:
            # launch of the background
            fond = pygame.image.load(BACKGROUND_IMAGE).convert()

            # Generation of the maze_file, file containing the labyrinth
            start = Start(choice)
            start.generate()
            start.show(window)

            # Creation of the game
            mac = Person(MACGYVER_IMAGE, MACGYVER_IMAGE
                         , MACGYVER_IMAGE, MACGYVER_IMAGE, start)  # mac = MacGyver

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
                        mac.move('right')
                    elif event.key == K_LEFT:
                        mac.move('left')
                    elif event.key == K_UP:
                        mac.move('top')
                    elif event.key == K_DOWN:
                        mac.move('bottom')

            # Displays at new positions
            window.blit(fond, (0, 0))
            start.show(window)
            window.blit(mac.direction, (mac.x, mac.y))  # direction
            pygame.display.flip()

            if mac.counter >= 4:
                # Back to home page
                if start.structure[mac.box_y][mac.box_x] == 'a':
                    # Window white
                    window.fill((255, 255, 255))
                    # Display the game over window
                    window.blit(text1,
                                (240 - text.get_width() // 2, 240 - text.get_height() // 2))
                    pygame.display.flip()
                    # 2 seconds of breaks before going to the home page
                    time.sleep(2)
                    repeat_game = 0
            elif 0 <= mac.counter < 4 and start.structure[mac.box_y][mac.box_x] == 'a':
                # Window white
                window.fill((255, 255, 255))
                # Display the game over window
                window.blit(text,
                            (240 - text.get_width() // 2, 240 - text.get_height() // 2))
                pygame.display.flip()
                # 2 seconds of breaks before going to the home page
                time.sleep(3)
                repeat_game = 0


def main():
    """main function"""
    lg = LaunchGame()


if __name__ == "__main__":
    main()
