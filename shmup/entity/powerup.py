"""
Powerups
Contains tokens that can be picked up
*Health Pack
*Score Items
*Missile Pack
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
    IMAGE_PATH = "Health Token.bmp"
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
        dy = dt * self.SPEED
        self.position.y += dy
        self.rect.y = self.position.y
        # print(self.SPEED, self.position, self.rect)
        # If bullet is out of space despawn
        if not self.rect.colliderect(GAME_RECT):
            self.kill()

    def effect(self, target):
        """Logic for enemy being hit"""
        if target.health + self.HEAL >= 100:
            ds = int((target.health + self.HEAL) - 100) * 2
            self.OBSERVER.add_score(ds, False)
            target.health = 100
        else:
            target.health += self.HEAL
        self.kill()


class HighPoint(Health):
    """
    Highscore object

    Adds Score to game
    """
    IMAGE_PATH = "gold.bmp"
    RECT = pg.Rect(0, 0, 24, 32)
    VALUE = 750

    def __init__(self, x, y):
        super().__init__(x, y)
        return

    def effect(self, target):
        """
        Adds Value to Score

        Args:
            target (Actor): Placeholder value

        Returns:
            None
        """
        self.OBSERVER.add_score(self.VALUE, False)
        self.kill()
