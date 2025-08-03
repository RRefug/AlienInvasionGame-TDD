

class Screen_Settings:
    '''This class initializes the static screen settings.'''
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230, 230, 230)

    def get_screen_width(self):
        return self.screen_width
    
    def get_screen_height(self):
        return self.screen_height
    
    def get_background_color(self):
        return self.background_color