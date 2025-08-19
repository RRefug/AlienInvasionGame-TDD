class Bullet_Settings:
    '''This class initializes the static bullet settings. '''
    def __init__(self):
        self.bullet_width = 3   
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

    def get_bullet_width(self):
        return self.bullet_width
    
    def get_bullet_height(self):
        return self.bullet_height
    
    def get_bullet_color(self):
        return self.bullet_color
    
    def get_allowed_bullet_count(self):
        return self.bullets_allowed