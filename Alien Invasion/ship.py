import pygame

class Ship:
    """A class to manage ship"""
    def __init__(self,ai_game):
    
        """initialize the ship and its starting point"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.setting

        # Load Ship image and get its rect
        self.image = pygame.image.load('F:\\practice\\python\\Alien Invasion\\ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's  horizontal position
        self.x = float(self.rect.x)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Updating the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Update rect object from self.x
        self.rect.x = self.x
        
    def blitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image, self.rect)    