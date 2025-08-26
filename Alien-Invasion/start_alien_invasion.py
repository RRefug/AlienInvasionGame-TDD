import pygame
from pygame.sprite import Group

from game_settings import GameSettings
from screen_settings import ScreenSettings
from ship_settings import ShipSettings
from bullet_settings import BulletSettings
from alien_settings import AlienSettings

from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship

# from bullet_manager import BulletManager
# from event_handler import EventHandler
#from event_handler_version2 import EventHandlerAltVersion

import game_functions as gf  # creating a class object when no class exists within game_functions file.


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()

    screen_settings = ScreenSettings()
    ship_settings = ShipSettings()
    bullet_settings = BulletSettings()
    alien_settings = AlienSettings()

    # Aggregation relationship - one class contains objects of another class. 
    # Settings doesn't own the lifecycle of other sub objects.
    alien_invasion_settings = GameSettings(screen_settings, ship_settings, bullet_settings, alien_settings)
    

    screen_width = alien_invasion_settings.settings_screen.get_screen_width()
    screen_height = alien_invasion_settings.settings_screen.get_screen_height()
    
    screen = pygame.display.set_mode(
        (screen_width, screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(alien_invasion_settings, screen, "Play")

    # Create an instance to store game statistics, and a scoreboard.
    stats = GameStats(alien_invasion_settings)
    score_board = Scoreboard(alien_invasion_settings, screen, stats)

    # Set the background color.
    bg_color = (230, 230, 230)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(alien_invasion_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(alien_invasion_settings, screen, ship, aliens)

    # TODO: Add a BulletManager instance to update bullets
    #print(f'This is the alien group: {aliens}')
    #print(f'This is the bullet group: {bullets}')
    #bullet_manager = BulletManager(alien_invasion_settings, screen, stats, score_board, ship, aliens, bullets)
    #print(f'Bullet manager now has this many aliens: {aliens.sprites()}')
    #print(f'Bullet manager now has this many bullets: {bullets.sprites()}')
    
    #button_events = EventHandler(alien_invasion_settings, screen, ship, bullets)
    #button_eventsV2 = EventHandlerAltVersion(alien_invasion_settings, screen, stats, score_board, play_button, ship, aliens, bullets)

    count = 1
    # Start the main loop for the game.
    while True:
        print(count)
        ###Original code#### 
        gf.check_events(
            alien_invasion_settings, screen, stats, score_board, play_button, ship, aliens, bullets
        )

        ###First event handler version ### button_events.check_events(
        #     alien_invasion_settings, screen, stats, score_board, play_button, ship, aliens, bullets
        # )

        #button_eventsV2.check_events()

        if stats.game_active:
            
            ship.update()
            gf.update_bullets(alien_invasion_settings, screen, stats, score_board, ship, aliens, bullets)
            
            # TODO: Figured out how to refactor this whole file. HOWEVER, we have an issue:
            # TODO: Bullets work fine. After one alien gets shot, we SHOULD drop to 35 aliens in group, but instead we drop to 0 in Group. 
            # TODO: After that, game crashes after one attempted bullet fire. 
            # TODO: Could keep trying bullet manager, but see if update aliens can be refactored. 
            # There is an order of how this happens and we delete bullets as we try doing stuff with them.
            #######My attempted version ######## bullet_manager.update_bullets()
            print('UPDATING ALIENS...')
            gf.update_aliens(alien_invasion_settings, screen, stats, score_board, ship, aliens, bullets)
            print(f'UPDATED ALIENS...{aliens}')

        gf.update_screen(
            alien_invasion_settings, screen, stats, score_board, ship, aliens, bullets, play_button
        )
        count+=1

run_game()
