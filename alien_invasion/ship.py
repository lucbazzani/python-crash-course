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

        # Movement flag: start with a ship that's not moving
        self.moving_right = False
        self.moving_left = False

    def move_to_right(self):
        self.moving_right = True
    
    def move_to_left(self):
        self.moving_left = True
    
    def stop_moving_right(self):
        self.moving_right = False
    
    def stop_moving_left(self):
        self.moving_left = False

    def update_movement(self):
        """Update the ship's position based on the movement flags."""

        if self.moving_right:
            self.rect.x += 1  
        if self.moving_left:
            self.rect.x -= 1  


    def blitme(self):
        """Draw the ship at its current location."""
        
        # draws the image to the screen at the position specified by self.rect
        self.screen.blit(self.image, self.rect)