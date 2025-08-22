class ShipSettings:
    '''This class initializes the static ship settings. '''
    def __init__(self):
        self.ship_lives_limit = 3
    
    def get_ship_limit(self):
        return self.ship_lives_limit