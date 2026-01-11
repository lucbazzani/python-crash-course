import pygame

class GameOver:
    """A class to the 'Game Over' text."""

    def __init__(self, game):
        """Initialize the text sprite and set its starting position."""

        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # Load image and prepare for transparency
        self.image = pygame.image.load(
            'alien_invasion/images/game_over.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Fade-in attributes
        self.alpha = 0
        self.fade_speed = 10.0
        self.image.set_alpha(self.alpha)

    def update(self):
        """Update the sprite's alpha for the fade-in effect."""
        
        if self.alpha < 255:
            self.alpha += self.fade_speed
            if self.alpha > 255:
                self.alpha = 255
            self.image.set_alpha(self.alpha)

    def blitme(self):
        """Draw the 'Game Over' message on the center of the  screen."""
        
        self.screen.blit(self.image, self.rect)