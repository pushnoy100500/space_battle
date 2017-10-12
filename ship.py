import pygame

class Ship(object):

    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.position = float(self.screen_rect.centerx)

        # Every new ship appears at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def update_position(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.position += self.settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.position -= self.settings.ship_speed_factor
        self.rect.centerx = self.position
