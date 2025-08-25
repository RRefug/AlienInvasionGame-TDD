import pygame
from pygame.sprite import Group

import game_functions as gf

class BulletManager:
    ''' Manage bullets: firing, updating, collisions
    
    NOT WORKING YET, but maybe if you get it working, use it as an instance in start_alien_invasion. 
    :) and yeah that's it. Use this file when you are done. 

    '''
    def __init__(self, alien_invasion_settings, screen, stats, score_board, ship, aliens, bullets):
        self.alien_invasion_settings = alien_invasion_settings
        self.screen = screen
        self.stats = stats
        self.score_board = score_board
        self.ship = ship
        self.aliens = aliens
        self.bullets = bullets

    def get_alien_invasion_settings(self):
        return self.alien_invasion_settings.settings_screen.get_screen_width()
    
    def update_bullets(self):
        '''Update position of bullets, and get rid of old bullets.'''
        top_of_screen_x_axis = 0

        print('We have this many bullets: ', self.bullets)

        # Update bullet positions.
        self.bullets.update()

        print('GOING')

        # if bullet travels beyond top border of screen, delete it
        for bullet in self.bullets.copy():
            print(f'This is bullet at the bottom: {bullet.rect.bottom}')
            if bullet.rect.bottom <= top_of_screen_x_axis:
                self.bullets.remove(bullet)
        
        print('Checking_bullet_alien_collisions...')
        self.check_bullet_alien_collisions()
        print('OUT OF UPDATE_BULLETS()')



    def check_bullet_alien_collisions(self):
        '''Respond to bullet-alien collisions by removing them.'''
        destroy_bullet_group = True
        destroy_alien_group = True

        print('INNER FUNCTION: ABOUT TO CREATE A GROUP COLLISION....')
        # Remove any bullets and aliens that have collided.
        print('This is the aliens: ', self.aliens)
        print('This is the bullets: ', self.bullets)
        collisions_dictionary = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        print('COLLISION CREATED....', collisions_dictionary)
        if collisions_dictionary:
            points_for_shooting_alien = self.alien_invasion_settings.settings_dynamic.get_alien_points()
            for self.aliens in collisions_dictionary.values():
                self.stats.score += points_for_shooting_alien * len(self.aliens)
                self.score_board.prep_score()
            gf.check_high_score(self.stats, self.score_board)

        if len(self.aliens) == 0:
            print('HELLO!??!!?!??!')
            # If the entire fleet is destroyed, start a new level.
            self.bullets.empty()
            self.alien_invasion_settings.increase_speed_settings()

            # Increase level.
            self.stats.level += 1
            self.score_board.prep_level()

            print('CREATING FLEET...')
            gf.create_fleet(self.alien_invasion_settings, self.screen, self.ship, self.aliens)
            print('CREATED FLEET...')

        print('OUT INNER FUNCTION()....')