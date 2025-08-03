
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

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.3

        # Scoring.
        self.alien_points = 50

        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
