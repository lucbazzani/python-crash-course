import sys

from random import random, uniform

import pygame

from keyboard_handler import Keyboard
from settings import Settings
from star import Star
from ship import Ship
from bullet import Bullet
from alien import Alien

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

        # to enable fullscreen mode, use the following block instead of the code above:
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        # after the screen has been created, we make an instance of ship.
        self.stars = pygame.sprite.Group()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_constellation()
        self._create_fleet()

        # Set the background color.
        self.bg_color = (0, 25, 50)

    def run_game(self):
        """Start the main loop for the game."""

        while True:            
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
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
            # Move the ship to right.
            self.ship.move_right()

        elif self.keyboard.is_left_key(event):
            # Move the ship to left.
            self.ship.move_left()
        
        elif self.keyboard.is_up_key(event):
            # Move the ship up.
            self.ship.move_up()
       
        elif self.keyboard.is_down_key(event):
            # Move the ship down.
            self.ship.move_down()

        elif self.keyboard.is_spacebar_key(event):
            # Fire bullet
            self._fire_bullet()

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

        elif self.keyboard.is_up_key(event):
            # Stop moving the ship up.
            self.ship.stop_moving_up()
       
        elif self.keyboard.is_down_key(event):
            # Stop moving the ship down.
            self.ship.stop_moving_down()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            # The add() method is similar to append(), 
            # but it’s written specifically for Pygame groups.
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets.""" 
        
        # the group automatically calls update_position() for each sprite in the group.
        self.bullets.update()

        # Get rid of bullets that have disappeared
        # We can’t remove items from a list or group within a for loop, 
        # so we have to loop over a copy of the group. 
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions."""

        self._check_fleet_edges()
        self.aliens.update()

    def _create_constellation(self):
        """Create a random constellation of stars."""
        
        scale = uniform(0.4, 0.9)
        star = Star(self, scale)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        
        while current_y < (self.settings.screen_height - 2 * star_height):
            while current_x < (self.settings.screen_width - 2 * star_width):
                # Randomly decide whether to place a star at this location.
                if random() < 0.1: # 10% chance to create a star
                    self._create_star(current_x, current_y)
                
                # Move to the next potential star position in the row.
                current_x += 2 * star_width

            # Reset for the next row.
            current_x = star_width
            current_y += 2 * star_height

    def _create_star(self, x_position, y_position):
        """Create a star and place it in the constellation."""
        
        # Create a star with a random size.
        scale = uniform(0.3, 0.9)
        new_star = Star(self, scale=scale)        
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)

    def _create_fleet(self):
        """Create the fleet of aliens."""

        # Create an alien and keep adding aliens until there's no room left. 
        # Spacing between aliens is one alien width and one alien height.
        # get the alien’s width and height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # refers to the horizontal position of the next alien we intend 
        # to place on the screen
        current_x, current_y = alien_width, alien_height
        screen_width = self.settings.screen_width

        # add a little margin on the right side of the screen. As long as 
        # there’s at least two alien widths’ worth of space at the right edge of
        # the screen, we enter the loop and add another alien to the fleet.
        
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (screen_width - 2 * alien_width):            
                self._create_alien(current_x, current_y)
                # add two alien widths to the horizontal position, to move past the
                # alien we just added and to leave some space between the aliens as well.
                current_x += 2 * alien_width  

            # Finished a row; reset x value, and increment y value
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        # set the precise horizontal position to the current value of current_x
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""

        # fill the screen with the background color during each pass 
        # through the loop.
        self.screen.fill(self.settings.bg_color)


        # After filling the background, we draw the ship, aliens, stars and
        # bullets on screen
        # When draw() is called on a group, Pygame draws each element in the 
        # group at the position defined by its rect attribute.
        self.stars.draw(self.screen)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


# only runs if the file is called directly
if __name__ == '__main__':
    # Make a game instance and run the game.
    game = AlienInvasion()
    game.run_game()
