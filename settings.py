class Settings(object):
    '''Class to store all settings for the game'''

    def __init__(self,
            screen_width=1200, 
            screen_height=800, 
            bg_color=(230, 230, 230),
            ship_speed_factor=2.5,
            bullet_width=3,
            bullet_height=15,
            bullet_color=(60, 60, 60),
            bullet_speed_factor=3,
            bullet_num_limit=5):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.bg_color = bg_color
        self.ship_speed_factor = ship_speed_factor
        self.bullet_width = bullet_width
        self.bullet_height = bullet_height
        self.bullet_color = bullet_color
        self.bullet_speed_factor = bullet_speed_factor
        self.bullet_num_limit = bullet_num_limit