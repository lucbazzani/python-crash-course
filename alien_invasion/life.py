import pygame
from pygame.sprite import Sprite

class Life(Sprite):
    """A class to represent a single life in the lifes remaining."""

    def __init__(self, game):
        """Initialize the star and set its starting position."""
        
        super().__init__()
        self.screen = game.screen
        self.stats = game.stats

        self.image = pygame.image.load('alien_invasion/images/heart.png')
        self.rect = self.image.get_rect()
        self.screen_rect = game.screen.get_rect()
        
        # self.rect.topright = self.screen_rect.topright
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
