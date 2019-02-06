"""
Powerup
Contains tokens that can be picked up
*Health Pack
*Score Items
*Missle Pack
*Bomb Pack
"""
import pygame as pg
from shmup.config import *
import shmup.spritesheet as spritesheet


class Health(pg.sprite.Sprite):
    """
    Health Token
    Restores Players hitpoints and adds to score if healing excedes player maxhealth

    Use as prototype for other powerups
    """
    init_flag = False
    OBSERVER = None
    IMAGE = None
    IMAGE_PATH = "../assets/Health Token.bmp"
    RECT = pg.Rect(0, 0, 32, 32)
    SPEED = 150  # Pixels per Second
    HEAL = 25

    def __init__(self, x, y):
        if not self.init_flag:
            raise RuntimeError("Health Token was not initialized")
        super().__init__(self.OBSERVER.powerups)
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
        self.rect.y = dy
        # If bullet is out of space despawn
        if not self.rect.colliderect(GAME_RECT):
            self.kill()

    def effect(self, target):
        """Logic for enemy being hit"""
        if target.health + self.HEAL >= 100:
            ds = int(100 - (target.health + self.HEAL)) * 3
            self.OBSERVER.add_score(ds, False)
            target.health = 100
        else:
            target.health += self.HEAL
        self.kill()
