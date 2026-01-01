import sys

import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
    
        pygame.init()

        # create a display window (surface) and assign it to self.screen
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""

        while True:
            # Watch for keyboard and mouse events.            
            # pygame.event.get() function returns a list of events that have 
            # taken place since the last time this function was called. 
            # Any keyboard or mouse event will cause this for loop to run
            for event in pygame.event.get():

                # when the player clicks the game window’s close button
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible.
            pygame.display.flip()


# only runs if the file is called directly
if __name__ == '__main__':
    # Make a game instance and run the game.
    game = AlienInvasion()
    game.run_game()
