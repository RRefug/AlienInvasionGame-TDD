import sys
import pygame
import game_functions as gf

class EventHandler:
    ''' Handle keyboard and mouse inputs. TODO: Try out using attributes. '''
    def __init__(self, alien_invasion_settings, screen, ship, bullets):
        self.alien_invasion_settings = alien_invasion_settings
        self.screen = screen
        self.ship = ship
        self.bullets = bullets
    
    def check_events(self, alien_invasion_settings, screen, stats, score_board, play_button, ship, aliens, bullets):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event, alien_invasion_settings, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event, ship)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                gf.check_play_button(
                    alien_invasion_settings,
                    screen,
                    stats,
                    score_board,
                    play_button,
                    ship,
                    aliens,
                    bullets,
                    mouse_x,
                    mouse_y,
                )

    def check_keydown_events(self, event, alien_invasion_settings, screen, ship, bullets):
        """Respond to keypresses made by player."""
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            gf.fire_bullet(alien_invasion_settings, screen, ship, bullets)
        elif event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(self, event, ship):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False
