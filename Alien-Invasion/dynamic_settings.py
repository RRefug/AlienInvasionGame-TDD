class Dynamic_Settings:
    def __init__(self):
        """Initialize settings that change throughout the game."""
        self.speed_factor_ship = 1.5
        self.speed_factor_bullet = 3
        self.speed_factor_alien = 0.3

        # TODO: rename bottom variables to something more meaningful!!!
        # Scoring.
        self.alien_points = 50

        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1

    
    def get_speed_factor_ship(self):
        return self.speed_factor_ship
    
    def set_speed_factor_ship(self, new_round_ship_speed):
        self.speed_factor_ship = new_round_ship_speed

    
    def get_speed_factor_bullet(self):
        return self.speed_factor_bullet
    
    def set_speed_factor_bullet(self, new_round_bullet_speed):
        self.speed_factor_bullet = new_round_bullet_speed

    
    def get_speed_factor_alien(self):
        return self.speed_factor_alien
    
    def set_speed_factor_alien(self, new_round_alien_speed):
        self.speed_factor_alien = new_round_alien_speed

    
    def get_alien_points(self):
        return self.alien_points
    
    def set_alien_points(self, current_alien_point_score):
        self.alien_points = current_alien_point_score

    
    def get_fleet_direction(self):
        return self.fleet_direction
    
    def set_fleet_direction(self, fleet_direction):
        self.fleet_direction = fleet_direction
    

    
