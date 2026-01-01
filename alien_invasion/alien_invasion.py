import sys

import pygame

from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
    
        # initialize all the imported pygame modules
        pygame.init()
        
        # make an instance of the class Clock for frame rate management
        self.clock = pygame.time.Clock()

        # make an instace of the class Settings with the default settings data
        self.settings = Settings()

        # create a display window (surface) and assign it to self.screen
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Set the background color.
        self.bg_color = (0, 25, 50)

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

            # fill the screen with the background color during each pass 
            # through the loop.
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()

            # The tick() method takes the value of 60 in the argument so Pygame 
            # will do its best to make the loop run exactly 60 times per second.
            self.clock.tick(self.settings.frame_rate)


# only runs if the file is called directly
if __name__ == '__main__':
    # Make a game instance and run the game.
    game = AlienInvasion()
    game.run_game()
