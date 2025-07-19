from alien import Alien           # importing the file for alien
from settings import Settings     # importing the file for settings
import pygame       # importing the package
import pytest


################################################################################
# FIXTURES MUST BE OUTSIDE CLASS (if you don't want them bound to "this.")
#  you could have them within class, but we ain't there yet :) )

# fixture for screen_display configuration.
@pytest.fixture
def screen_display():
    pygame.init() # making sure Pygame is initialized safely
    screen_width = 200
    screen_height = 200
    screen_size = (screen_width, screen_height)
    screen = pygame.display.set_mode(screen_size)
    yield screen   # returns screen
    pygame.quit()   # closes screen too

@pytest.fixture
def settings():
    return Settings()  # return a settings object
######################################################################################


# Todo count: 3 
class Test_Alien_Existence:    
    # Arrange - use 2 fixtures: settings and screen_display
    def test_creation_of_one_alien(self, screen_display, settings):
        '''
        Testing that one alien is created by the Alien class. 
        (TODO: maybe could mock Sprite if you want to isolate your class from Sprite(parent class since Alien(child class) is using super()))
        (TODO: not parameterized, but you could if you want to!)
        '''
        # Act - Instantiate alien object
        alien_one = Alien(settings, screen_display)

        # Assert - Is it an alien object? yes
        assert isinstance(alien_one, Alien)
    

    def test_creation_of_no_alien(self):
        ''' 
        Testing that there are no aliens on the screen 
        (Maybe test that a sprite group is empty)
        '''
        aliens = []
        aliens = pygame.sprite.Group() # method that acts as a simple container to hold multiple sprites

        assert len(aliens) == 0
    
    def test_pygame_image_load_method(self):
        '''
        TODO: If the image path is wrong or missing, pygame.image.load() will crash. You can:
        - Mock it in tests
        - Or wrap it in a try/except in production code
        '''
        pass



class Test_Alien_Position:
    def test_alien_initial_position(self, settings, screen_display):
        alien = Alien(settings, screen_display)

        # One alien = one sprite (sprite is a picture, a rectangle with a width and height)
        # alien object has attributes: image, rect, and x 
        assert alien.rect.x == alien.rect.width
        assert alien.rect.y == alien.rect.height
        assert alien.x == float(alien.rect.x)


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