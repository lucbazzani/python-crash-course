import pygame

class Ship:
    """A class to manage the ship."""

    # the game parameter is a reference to the current instance of the 
    # AlienInvasion class. This will give Ship access to all the game resources 
    # defined in AlienInvasion
    def __init__(self, game):
        """Initialize the ship and set its starting position."""

        # screen is assigned to an attribute of Ship, so we can access it easily 
        # in all the methods in this class.
        self.screen = game.screen

        # accessing the screen’s rect attribute using the get_rect() method and 
        # assigning it to self.screen_rect allows us to place the ship in
        # the correct location on the screen.
        self.screen_rect = game.screen.get_rect()

        # Load the ship image and get its rect.
        # pygame.image.load() returns a surface representing the ship.
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        
        # access the ship surface’s rect attribute so we can later use it 
        # to place the ship
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        # the ship image is centered horizontally and aligned with the bottom 
        # of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        
        # draws the image to the screen at the position specified by self.rect
        self.screen.blit(self.image, self.rect)