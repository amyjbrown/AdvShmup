# encoding * utf - 8 *
"""
Level
Base and implementation for level spawning mechanism

*InfiniteLevel: Infinite Level Mechanic
"""
import random
import pygame as pg
from shmup.config import *
import shmup.entity


class InfiniteLevel:
    """
    Infinite Mode Spawning Unit
    """
    MonsterTimer = [0, 2]  # time in seconds
    ScoreTimer = [45, 90]
    HealthTimer = [30, 60]
    X_Spawn_Space = [0, 448]

    def __init__(self, scene):
        self.scene = scene
        self.mon1 = random.randint(*self.MonsterTimer) + 3
        self.mon2 = random.randint(*self.MonsterTimer) + 3
        self.mon3 = random.randint(*self.MonsterTimer) + 3
        self.mon4 = random.randint(*self.MonsterTimer) + 3
        self.mon5 = random.randint(*self.MonsterTimer) + 3

        self.health = random.randint(*self.HealthTimer)
        self.point = random.randint(*self.HealthTimer)

        # self.all = [self.mon1, self.mon2., self.mon3, self.mon4, self.mon5, self.health, self.point]
        # self.mons = [self.mon1, self.mon2., self.mon3, self.mon4, self.mon5,]

    def spawn_coords(self):
        return random.randint(0, 480), -32

    def update(self, dt):
        """
        Updates and spawns appropriate encounters

        Args:
            dt (float): Time delta that has passed in 'level time'

        Returns:
            None
        """
        # For item in mon1, etc., decrement and then spawn
        self.mon1 -= dt
        if self.mon1 <= 0:
            self.mon1 = random.randint(*self.MonsterTimer) + 4
            shmup.entity.Asteroid(*self.spawn_coords())

        self.mon2 -= dt
        if self.mon2 <= 0:
            self.mon2 = random.randint(*self.MonsterTimer)
            shmup.entity.Asteroid(*self.spawn_coords())

        self.mon3 -= dt
        if self.mon3 <= 0:
            self.mon3 = random.randint(*self.MonsterTimer)
            shmup.entity.Asteroid(*self.spawn_coords())

        self.mon4 -= dt
        if self.mon4 <= 0:
            self.mon4 = random.randint(*self.MonsterTimer)
            shmup.entity.Asteroid(*self.spawn_coords())

        self.mon5 -= dt
        if self.mon5 <= 0:
            self.mon5 = random.randint(*self.MonsterTimer)
            shmup.entity.Asteroid(*self.spawn_coords())

        self.health -= dt
        if self.health <= 0:
            self.health = random.randint(*self.HealthTimer)
            shmup.entity.HealthToken(*self.spawn_coords())

        self.point -= dt
        if self.point <= 0:
            self.point = random.randint(*self.ScoreTimer)
            shmup.entity.HighPointToken(*self.spawn_coords())
