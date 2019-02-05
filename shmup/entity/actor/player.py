# encoding * utf - 8 *
"""
Player base object

*Player
"""
import shmup.entity.actor.actor as actor
import shmup.entity.projectile as projectile
from shmup.config import *


class Player(actor.Actor):
    """
    Player Class

    Notes:
        Check Actor for all in-game structure
    """
    IMAGE_PATH = "../assets/Ship.bmp"
    IMAGE = None
    init_flag = False
    HITBOX = pg.Rect(9, 6, 46, 52)
    RECT = pg.Rect(0, 0, 64, 64)
    MAX_HEALTH = 100
    speed = 120
    COOLDOWN = 0.1

    def __init__(self, position):
        super().__init__(position, self.observer.player_group)
        self.fire_side = False
        self.is_firing = False
        self.fire_timer = 0

    def update(self, dt):
        self._move(dt)
        if self.is_firing:
            self._fire()
        self.fire_timer -= dt

    @property
    def vx(self):
        """Value of x component of velocity"""
        return self.velocity.x

    @vx.setter
    def vx(self, x):
        self.velocity.x = x

    @property
    def vy(self):
        """Value of y component of velocity"""
        return self.velocity.y

    @vy.setter
    def vy(self, y):
        self.velocity.y = y

    @classmethod
    def setup(cls, observer):
        super().setup(observer)
        cls.IMAGE.set_colorkey(
            cls.IMAGE.get_at((0, 0))
        )
        return

    def _fire(self):
        """
        Spawns a bullet if cooldown has finished, positioning item
        Returns:
            None
        """
        if self.fire_timer <= 0:
            projectile.Bullet(self.position.x + 15 + 8 * self.fire_side,
                          self.position.y - 5)
            self.fire_side = not self.fire_side
            self.fire_timer = self.COOLDOWN

    def firing(self, start=True):
        """
        Makes the player start firing. This is used to simulate holding down a key for firing

        Args:
            start (bool): If the player should start firing

        Returns:
            None
        """
        self.is_firing = start
