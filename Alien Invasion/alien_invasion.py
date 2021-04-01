import sys
import pygame 
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        
        self.setting = Settings()
        self.screen = pygame.display.set_mode((0,0) , pygame.FULLSCREEN)
        self.setting.screen_width = self.screen.get_rect().width
        self.setting.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Start of the main loop of the program"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullet()
            self._update_alien()    
            self._update_screen()

    def _check_events(self):
        """Respond to keyword and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    # Refactoring the check events
    def _check_keydown_events(self,event):
        """Responds to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()    
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        """Responds to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.setting.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add_internal(new_bullet)
    def _update_bullet(self):
        self.bullets.update()
        # Get rid of bullets that have disappeared 
        for bullet in self.bullets:
            if bullet.rect.bottom <= 0:
                self.bullets.remove_internal(bullet)  

    def _create_fleet(self):
        """Create a fleet of aliens"""
        alien = Alien(self)
        alien_width , alien_height = alien.rect.size
        available_space_x = self.setting.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2*alien_width)
        # Row
        ship_height = self.ship.rect.height
        available_space_y = (self.setting.screen_height - (3*alien_height) - ship_height)
        number_rows = available_space_y // (2* alien_height)

        # Creating first row of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number,row_number)         

    def _check_fleet_edge(self):
        """Responds if any alien has reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""        
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.setting.fleet_direction *= -1    

    def _create_alien(self,alien_number,row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 *alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2* alien.rect.height * row_number
        self.aliens.add_internal(alien)

    def _update_screen(self):
        #Redraw the screen during each pass through the loop
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)    
        #Make the most recently drawn screen visible
        pygame.display.flip()    

    def _update_alien(self):
        self._check_fleet_edge()
        self.aliens.update()

if __name__ == '__main__':
    #make instance of class and run the game            
    ai = AlienInvasion()
    ai.run_game()