import sys
import pygame
from bullet import Bullet
from pygame.sprite import Group
from settings import Settings
from ship import Ship


class Game(object):
    '''Main class for the game'''

    def __init__(self, settings):
        self.settings = settings
        pygame.init()
        pygame.display.set_caption("Space Battle")
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.bullets = Group()

    def add_ship(self, ship=None):
        '''Add a space ship to the game'''
        if ship is not None:
            self.ship = ship
        self.ship = Ship(self.screen, self.settings)

    def check_events(self):
        '''watching keyboard and cursor events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_SPACE:
            new_bullet = Bullet(self.settings, self.screen, self.ship)
            self.bullets.add(new_bullet)

    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def clear_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def run_game(self):
        '''Run the goddam game'''
        while True:
            self.check_events()
            self.ship.update_position()
            self.bullets.update()            
            self.update_screen()

    def update_screen(self):
        '''Rerender everything necessary'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blit_me()
        for bullet in self.bullets:
            bullet.draw_bullet()
        pygame.display.flip()


# Built all the objects and run the game
settings = Settings()

game = Game(settings)
game.add_ship()
game.run_game()
