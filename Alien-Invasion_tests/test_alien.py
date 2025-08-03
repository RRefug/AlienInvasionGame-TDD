from alien import Alien           # importing the file for alien
from settings import Settings     # importing the file for settings
import pygame       # importing the package
import pytest


################################################################################
# FIXTURES MUST BE OUTSIDE CLASS (if you don't want them bound to "this.")
#  you could have them within class, but we ain't there yet :) )

# fixture for screen_display configuration.
@pytest.fixture
def game_screen_display():
    pygame.init() # making sure Pygame is initialized safely
    game_screen_width = 200
    game_screen_height = 200
    game_screen_size = (game_screen_width, game_screen_height)
    game_screen = pygame.display.set_mode(game_screen_size)
    yield game_screen   # returns screen
    pygame.quit()   # closes screen too

@pytest.fixture
def all_Settings_For_Alien_Invasion():
    all_alien_invasion_settings = Settings()
    
    move_right = 1
    move_left = -1

    alien_speed_factor = 0.3

    all_alien_invasion_settings.fleet_direction = move_right
    all_alien_invasion_settings.alien_speed_factor = alien_speed_factor
    
    return all_alien_invasion_settings  # return a settings object
######################################################################################


# Todo count: 3 
class Test_Alien_Existence:    
    # Arrange - use 2 fixtures: settings and screen_display
    def test_creation_of_one_alien_enemy(self, game_screen_display, all_Settings_For_Alien_Invasion):
        '''
        Testing that one alien is created by the Alien class. 
        (TODO: maybe could mock Sprite if you want to isolate your class from Sprite(parent class since Alien(child class) is using super()))
        (TODO: not parameterized, but you could if you want to!)
        '''
        # Act - Instantiate alien object
        alien_enemy = Alien(all_Settings_For_Alien_Invasion, game_screen_display)

        # Assert - Is it an alien object? yes
        assert isinstance(alien_enemy, Alien)
    

    def test_creation_of_no_alien_enemies_in_sprite_group(self):
        ''' 
        Testing that there are no aliens on the screen 
        (Test that a sprite group is empty)
        '''
        alien_enemies = []
        alien_enemies = pygame.sprite.Group() # method that acts as a simple container to hold multiple sprites

        assert len(alien_enemies) == 0
    
    def test_pygame_image_load_method(self):
        '''
        TODO: If the image path is wrong or missing, pygame.image.load() will crash. You can:
        - Mock it in tests
        - Or wrap it in a try/except in production code
        '''
        pass



class Test_Alien_Position:
    def test_alien_enemy_initial_position_topleft_of_screen(self, all_Settings_For_Alien_Invasion, game_screen_display):
        alien_enemy = Alien(all_Settings_For_Alien_Invasion, game_screen_display)

        # One alien = one sprite (sprite is a picture, a rectangle with a width and height)
        # alien object has attributes: image, rect, and x 
        assert alien_enemy.rect.x == alien_enemy.rect.width
        assert alien_enemy.rect.y == alien_enemy.rect.height

        assert alien_enemy.x == float(alien_enemy.rect.x)
    

    def test_alien_enemy_moving_to_the_right_x(self, all_Settings_For_Alien_Invasion, game_screen_display):
        # arrange
        print('This is the type of settings:', type(all_Settings_For_Alien_Invasion))
        print('This guy doesnt exist apparently: ', all_Settings_For_Alien_Invasion)

        alien_enemy = Alien(all_Settings_For_Alien_Invasion, game_screen_display)
        rectangle_width = 50
        rectangle_height = 50
        expected_rect_width = 50
        expected_rect_height = 50
        expected_alien_speed_factor = 0.3
        expected_calculated_alien_width_x = 60.3 # 60.0 + 0.03 + 50? (alien_enemy.x + alien_enemy.ai_settings.alien_speed_factor + rectangle_width)

        alien_enemy.rect.x = rectangle_width # used in alien_enemy update() method, alien_enemy.rect.x = 50
        alien_enemy.rect.y = rectangle_height

        assert alien_enemy.rect.x == expected_rect_width
        assert alien_enemy.rect.y == expected_rect_height

        # act - should multiply current 
        print('alien_enemy.x: ', alien_enemy.x)
        print('alien_enemy.all_Settings_For_Alien_Invasion object exists: ', alien_enemy.ai_settings)
        print('alien_enemy.all_Settings_For_Alien_Invasion.alien_speef_factor exists: ', alien_enemy.ai_settings.alien_speed_factor)
        
        alien_enemy.update() # self.rect.x = 60.3 -> 50 (after line 99) + 60.0 + 0.3

        assert alien_enemy.ai_settings.alien_speed_factor == expected_alien_speed_factor
        assert alien_enemy.x == expected_calculated_alien_width_x




class Test_Alien_Image_Loading:
    def test_an_aliens_image_loading(self):
        pass






'''
WAYS TO IMPROVE YOUR TEST COVERAGE!

- Test alien movement across the screen and edge detection
- Mock pygame.image.load() to avoid file dependency
- Use pytest-cov to measure how much of your game logic is covered
- Parameterize tests to simulate different screen sizes or alien speed


'''