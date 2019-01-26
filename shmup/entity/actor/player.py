# encoding * utf - 8 *
"""
Player base object

*Player
"""
import pygame as pg
import config
import entity.actor.actor as actor


class Player(actor.Actor):
    """
    Player Class

    Notes:
        Check Actor for all in-game structure
    """

    def __init__(self, position, *groups):
        super().__init__(position, *groups)
