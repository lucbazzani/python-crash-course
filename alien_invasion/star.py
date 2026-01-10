import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star in the constellation."""

    def __init__(self, game, scale):
        """Initialize the star and set its starting position."""
        
        super().__init__()
        self.screen = game.screen

        # Load the star image and set its rect attribute. 
        star_image = pygame.image.load('alien_invasion/images/star.png')
        self.image = self._resize(star_image, scale)

        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the star's exact horizontal position.
        self.x = float(self.rect.x)

    def _resize(self, image, scale):
        """ Resize the image and its rect. """

        new_width = int(image.get_width() * scale)
        new_height = int(image.get_height() * scale)
        return pygame.transform.smoothscale(
            image, (new_width, new_height))
