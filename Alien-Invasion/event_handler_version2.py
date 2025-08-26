import sys
import pygame
import game_functions as gf

class EventHandlerAltVersion:
    ''' Handle keyboard and mouse inputs. 
    This class is to try out using attributes. 
    It WORKS, but this way won't 100% work for every class like it did here
    since attributes can
    be ALTERED by other functions in other classes and we don't return a newer version to be stored in our class attributes here.
    SO the shift might be to use design patterns like observer, state or command. Going to experiment in another branch!!'''
    def __init__(self, alien_invasion_settings, screen, stats, score_board, play_button, ship, aliens, bullets):
        self.alien_invasion_settings = alien_invasion_settings
        self.screen = screen
        self.stats = stats
        self.score_board = score_board
        self.play_button = play_button
        self.ship = ship
        self.aliens = aliens
        self.bullets = bullets
    
    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # TODO: I haven't made a GameStateManager class yet to use check_playbutton(...).
                # So that's why I just imported gf for now and everywhere else in file.
                # Exploring design patterns right now... 8/26/2025 
                gf.check_play_button(
                    self.alien_invasion_settings,
                    self.screen,
                    self.stats,
                    self.score_board,
                    self.play_button,
                    self.ship,
                    self.aliens,
                    self.bullets,
                    mouse_x,
                    mouse_y,
                )

    def check_keydown_events(self, event):
        """Respond to keypresses made by player."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            gf.fire_bullet(self.alien_invasion_settings, self.screen, self.ship, self.bullets)
        elif event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
