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

        self.settings = game.settings

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

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag: start with a ship that's not moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update_position(self):
        """Update the ship's position based on the movement flags."""

        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed  
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        
        # Update rect object from self.x. 
        # Only the integer portion of self.x will be assigned to self.rect.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        
        # draws the image to the screen at the position specified by self.rect
        self.screen.blit(self.image, self.rect)

    def move_right(self):
        self.moving_right = True
    
    def move_left(self):
        self.moving_left = True
    
    def move_up(self):
        self.moving_up = True
    
    def move_down(self):
        self.moving_down = True

    def stop_moving_right(self):
        self.moving_right = False
    
    def stop_moving_left(self):
        self.moving_left = False
        
    def stop_moving_up(self):
        self.moving_up = False
    
    def stop_moving_down(self):
        self.moving_down = False
