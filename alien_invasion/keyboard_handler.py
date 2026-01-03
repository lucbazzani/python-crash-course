import pygame

class Keyboard:
    """A class to represent the user's keyboard."""

    def __init__(self):
        """Initialize the keyboard."""
        pass

    def is_quit_key(self, event):
        """
        Did the player press the ESC or Q key?
        """
        return event.key == pygame.K_ESCAPE or event.key == pygame.K_q
    
    def is_right_key(self, event):
        """ Is the event related to the right arrow key or the D key? """
        return event.key == pygame.K_RIGHT or event.key == pygame.K_d
    
    def is_left_key(self, event):
        """ Is the event related to the left arrow key or the A key? """
        return event.key == pygame.K_LEFT or event.key == pygame.K_a
    
    def is_up_key(self, event):
        """ Is the event related to the up arrow key or the W key? """
        return event.key == pygame.K_UP or event.key == pygame.K_w
    
    def is_down_key(self, event):
        """ Is the event related to the down arrow key or the S key? """
        return event.key == pygame.K_DOWN or event.key == pygame.K_s
    
    def is_spacebar_key(self, event):
        """ Is the event related to the Spacebar key? """
        return event.key == pygame.K_SPACE
