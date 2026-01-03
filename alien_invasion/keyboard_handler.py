import pygame

class Keyboard:
    """A class to represent the user's keyboard."""

    def __init__(self):
        """Initialize the keyboard."""
        pass

    def is_quit_event(self, event):
        """
        Did the player click the game window’s close button or 
        press the ESC key?
        """
        return event.type == pygame.QUIT \
            or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)
    
    def is_right_key(self, event):
        """ Is the event related to the right arrow key or the D key? """
        return event.key == pygame.K_RIGHT or event.key == pygame.K_d
    
    def is_left_key(self, event):
        """ Is the event related to the left arrow key or the A key? """
        return event.key == pygame.K_LEFT or event.key == pygame.K_a
