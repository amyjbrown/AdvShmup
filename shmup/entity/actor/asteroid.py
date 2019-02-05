"""
Asteroid object
"""
import random
import pygame as pg
from shmup.config import *
import shmup.entity.actor.actor as actor


class Asteroid(actor.Actor):
    """
    Free roaming ASteroid object that damages the player on hit
    """
    IMAGE_PATH = "../assets/asteroid.bmp"
    IMAGE = None
    init_flag = False
    HITBOX = pg.Rect(8, 8, 46, 46)
    RECT = pg.Rect(0, 0, 64, 64)
    MAX_HEALTH = 20
    speed = 90

    def __init__(self, x, y):
        super().__init__((x, y), self.observer.enemy)
        self.velocity = pg.Vector2(0, self.speed)

    def update(self, dt):
        self._move(dt)
        if self.health <= 0:
            self.kill()
        if not self.rect.colliderect(EXTENDED_RECT):
            self.kill()

    def collide(self, other):
        other.health -= 20
        self.kill()
