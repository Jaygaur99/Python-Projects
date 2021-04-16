import pygame
from pygame.sprite import Sprite

class Alien:
    """A class to represent a single alien in the fleet"""

    def __init__(self,ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.setting
        # Load the image and  set its rect attribute
        self.image = pygame.image.load("F:\\practice\\python\\Alien Invasion\\alien.bmp")
        self.rect = self.image.get_rect()

        # Start new alien at the left top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien exect horizontal position
        self.x = float(self.rect.x)

    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Retrun true if alien has hit an edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True