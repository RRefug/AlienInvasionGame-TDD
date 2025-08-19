class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, alien_invasion_settings_object):
        """Initialize statistics."""
        self.alien_invasion_settings = alien_invasion_settings_object
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        # self.ships_left = self.alien_invasion_settings.ship_limit
        self.ships_left = self.alien_invasion_settings.settings_ship.get_ship_limit()
        print('this is the current allowed number of ships: ', self.ships_left)
        self.score = 0
        self.level = 1
