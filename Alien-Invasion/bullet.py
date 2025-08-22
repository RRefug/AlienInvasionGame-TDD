import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object, at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen

        bullet_width = ai_settings.settings_bullet.get_bullet_width()
        bullet_height = ai_settings.settings_bullet.get_bullet_height()

        # Create bullet rect at (0, 0), then set correct position.
        self.rect = pygame.Rect(
            0, 0, bullet_width, bullet_height
        )
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store a decimal value for the bullet's position.
        self.y = float(self.rect.y)

        self.color = ai_settings.settings_bullet.get_bullet_color()
        self.speed_factor = ai_settings.settings_dynamic.get_speed_factor_bullet()

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
