import pygame
from pygame.sprite import Sprite

class Bullet:
    """A class to manage bullets fired from the ship"""

    def __init__(self,ai_game):
        """Create a bullet object at the ships current position"""
        super().__init__()
        self.screen = ai_game.screen 
        self.settings = ai_game.setting
        self.color = self.settings.bullet_color

        # Create a bullet revt at (0,0)  and thenset correct position
        self.rect = pygame.Rect(
            0,0,self.settings.bullet_width,self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""  
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)