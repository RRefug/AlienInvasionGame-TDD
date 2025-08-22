🧩 Settings Architecture

Settings are split into domain-specific classes:

- `ScreenSettings`: Screen width, height, background color
- `ShipSettings`: Ship lives
- `BulletSettings`: Bullet width, height, color, bullet count
- `AlienSettings`: Alien drop speed

These are aggregated into `GameSettings`, which acts as a central config hub.

```python
screen_settings = ScreenSettings()
ship_settings = ShipSettings()
bullet_settings = BulletSettings()
alien_settings = AlienSettings()

alien_invasion_settings = GameSettings(screen, ship, bullet, alien)
