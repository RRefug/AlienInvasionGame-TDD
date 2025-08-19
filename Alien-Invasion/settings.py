from dynamic_settings import Dynamic_Settings

class Settings:
    """A class to store all settings for Alien Invasion. Game settings is a better name."""

    def __init__(self, screen_settings_object, ship_settings_object, bullet_settings_object, alien_settings_object):
        """Initialize the game's static settings."""

        self.settings_screen = screen_settings_object
        self.settings_ship = ship_settings_object
        self.settings_bullet = bullet_settings_object
        self.settings_alien = alien_settings_object

        # How quickly the game speeds up.
        self.speedup_scale = 1.1
        # How quickly the alien point values increase.
        self.score_scale = 1.5

        # Composite association - the contained object cannot exist without the containing object.
        # Ex: if settings is destroyed, dynamic settings can't exist without it.
        self.settings_dynamic = Dynamic_Settings()


    def increase_speed_settings(self):
        """Increase speed settings and alien point values."""
        
        new_round_ship_speed = self.settings_dynamic.get_speed_factor_ship()
        new_round_bullet_speed = self.settings_dynamic.get_speed_factor_bullet()
        new_round_alien_speed = self.settings_dynamic.get_speed_factor_alien()

        new_round_ship_speed *= self.speedup_scale
        new_round_bullet_speed *= self.speedup_scale
        new_round_alien_speed *= self.speedup_scale

        self.settings_dynamic.set_speed_factor_ship(new_round_ship_speed)
        self.settings_dynamic.set_speed_factor_bullet(new_round_bullet_speed)
        self.settings_dynamic.set_speed_factor_alien(new_round_alien_speed)

        self.increase_alien_point_value()


    def increase_alien_point_value(self):
        '''This function increments the score after defeating one alien. '''

        set_new_round_alien_points = self.settings_dynamic.get_alien_points()
        self.settings_dynamic.set_alien_points(int(set_new_round_alien_points * self.score_scale))


