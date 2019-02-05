# encoding: * utf - 8 *
"""
Projectiles and bullets

Contains all Projectile and Bullet objects and logic
*Bullet: Player Bullet, serves as Base class to Missile and Splash for code reuse
*Missile: Player missile explosive
*Splash: Splash `bullet` used for area of effect damage
*Zap: Enemy Bullet
"""
import pygame as pg
from shmup.config import *
import shmup.spritesheet as spritesheet


class Bullet(pg.sprite.Sprite):
    """
    Bullet object and prototype
    Used for player fire projectiles
    """
    init_flag = False
    OBSERVER = None
    IMAGE = None
    IMAGE_PATH = "../assets/player bullet.bmp"
    RECT = pg.Rect(0, 0, 16, 16)
    SPEED = -120  # Pixels per Second
    DAMAGE = 10

    def __init__(self, x, y):
        if not self.init_flag:
            raise RuntimeError("Bullet class was not initialized")
        super().__init__(self.OBSERVER.bullets)
        self.position = pg.Vector2(x, y)
        self.image = self.IMAGE
        self.rect = self.RECT.move(x, y)

        self.hitbox = self.rect

    @classmethod
    def setup(cls, observer):
        if not cls.init_flag:
            cls.OBSERVER = observer
            cls.IMAGE = spritesheet.load(cls.IMAGE_PATH, True)
            # cls.DEFAULT_GROUPS = observer.bullets
            cls.init_flag = True

    def update(self, dt):
        dy = self.SPEED * dt
        self.position.y += dy
        self.rect.move_ip(0, dy)
        # If bullet is out of space despawn
        if not self.rect.colliderect(GAME_RECT):
            self.kill()

    def collide(self, target):
        """Logic for enemy being hit"""
        target.health -= self.DAMAGE


class Missile(Bullet):
    """
    Missile object
    Used for fast moving, dangerous missiles that do direct damage and and spawn an area of effect damage entity
    """
    SPEED = 240
    DAMAGE = 20

    @classmethod
    def setup(cls, observer):
        pass  # Need to properly setup things for it


class Zap(Bullet):
    """
    Object for enemy ranged attacks
    Basically Bullet, but in reverse
    """
