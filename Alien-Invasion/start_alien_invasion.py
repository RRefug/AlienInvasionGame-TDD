import pygame
from pygame.sprite import Group

from settings import Settings
from screen_settings import Screen_Settings
from ship_settings import Ship_Settings
from bullet_settings import Bullet_Settings
from alien_settings import Alien_Settings
from dynamic_settings import Dynamic_Settings

from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf



def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()

    # Aggregation design pattern
    screen_settings = Screen_Settings()
    ship_settings = Ship_Settings()
    bullet_settings = Bullet_Settings()
    alien_settings = Alien_Settings()
    alien_invasion_settings = Settings(screen_settings, ship_settings, bullet_settings, alien_settings)
    

    print('This is the screen width from Screen_Settings class: ', alien_invasion_settings.settings_screen.get_screen_width())

    screen_width = alien_invasion_settings.settings_screen.get_screen_width()
    screen_height = alien_invasion_settings.settings_screen.get_screen_height()

    print('This is the screen height from Screen_Settings class: ', alien_invasion_settings.settings_screen.get_screen_height())
    screen = pygame.display.set_mode(
        (screen_width, screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(alien_invasion_settings, screen, "Play")

    # Create an instance to store game statistics, and a scoreboard.
    stats = GameStats(alien_invasion_settings)
    sb = Scoreboard(alien_invasion_settings, screen, stats)

    # Set the background color.
    bg_color = (230, 230, 230)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(alien_invasion_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(alien_invasion_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(
            alien_invasion_settings, screen, stats, sb, play_button, ship, aliens, bullets
        )

        if stats.game_active:
            ship.update()
            gf.update_bullets(alien_invasion_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(alien_invasion_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(
            alien_invasion_settings, screen, stats, sb, ship, aliens, bullets, play_button
        )


run_game()
