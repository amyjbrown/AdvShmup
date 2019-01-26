# encoding * utf - 8 *
"""
Player base object

*Player
"""
import entity.actor.actor as actor
from config import *


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

    def __init__(self, position, *groups):
        super().__init__(position, *groups)
        # todo every other deal in this thing

    def update(self, dt):
        self._move(dt)

    @classmethod
    def setup(cls, observer):
        super().setup(observer)
        cls.IMAGE.set_colorkey(
            cls.IMAGE.get_at((0, 0))
        )
        return

    def fire(self):
        pass
