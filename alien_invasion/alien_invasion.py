import sys

import pygame

from keyboard_handler import Keyboard
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
    
        # initialize all the imported pygame modules
        pygame.init()
        
        # make an instance of the class Clock for frame rate management
        self.clock = pygame.time.Clock()

        # make an instance of the class Settings with the default settings data
        self.settings = Settings()

        # make an instance of the class Keyboard to help handling the user's inputs
        self.keyboard = Keyboard()

        # create a display window (surface) and assign it to self.screen
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # after the screen has been created, we make an instance of ship.
        self.ship = Ship(self)

        # Set the background color.
        self.bg_color = (0, 25, 50)

    def run_game(self):
        """Start the main loop for the game."""

        while True:            
            self._check_events()
            self.ship.update_movement()
            self._update_screen()

            # The tick() method takes the value of 60 in the argument so Pygame 
            # will do its best to make the loop run exactly 60 times per second.
            self.clock.tick(self.settings.frame_rate)
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""

        # pygame.event.get() function returns a list of events that have 
        # taken place since the last time this function was called.
        # Watch for keyboard and mouse events.             
        # Any keyboard or mouse event will cause this for loop to run
        for event in pygame.event.get():
            # when the player clicks the game window’s close button
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)                

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)                
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""

        if self.keyboard.is_right_key(event):
            # Move the ship to the right.
            self.ship.move_to_right()

        elif self.keyboard.is_left_key(event):
            # Move the ship to the left.
            self.ship.move_to_left()

        elif self.keyboard.is_quit_key(event):
            sys.exit()
            
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        
        if self.keyboard.is_right_key(event):
            # Stop moving the ship to the right.
            self.ship.stop_moving_right()

        elif self.keyboard.is_left_key(event):
            # Stop moving the ship to the left.
            self.ship.stop_moving_left()
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""

        # fill the screen with the background color during each pass 
        # through the loop.
        self.screen.fill(self.settings.bg_color)

        # After filling the background, we draw the ship on the screen
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


# only runs if the file is called directly
if __name__ == '__main__':
    # Make a game instance and run the game.
    game = AlienInvasion()
    game.run_game()
