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

    def __init__(self, position):
        super().__init__(position, self.observer.player_group)
        # todo every other deal in this thing
        self.fire_side = False

    def update(self, dt):
        self._move(dt)

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

    def fire(self):
        """Spawns an appropriate bullet object"""
        projectile.Bullet(self.position.x + 20 + 8 * self.fire_side,
                          self.position.y - 5)
        self.fire_side = not self.fire_side
