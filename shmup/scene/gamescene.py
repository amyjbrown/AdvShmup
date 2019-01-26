# encoding * utf - 8 *
"""
Gamescene
Where almost everything lives and works
"""
import pygame as pg
import inputhandler
import entity.entityhandler as entityhandler
import scene.scenebase
from config import *


class GameScene(scene.scenebase.Scene):
    """
    GameScene
    """
    def __init__(self):
        super().__init__()
        # Entity Handler setup
        self.entity_handler = entityhandler.EntityHandler(self)
        self.player = self.entity_handler.player

        # base game objects
        self.score = 0
        self.lives = 3

        # game
        # Todo Screenbackground
        # Todo background = scroller()

        self.game_progress = 0.0

    def load(self, level=0):
        """
        Overload

        Args:
            level: number id of level to be loaded

        Returns:
            None
        """

        # TODO: loading in level properly
        self.entity_handler.setup()
        self.game_progress = 0

    def handle_input(self, event):
        if event.type == "menu":
            self.final = True
        elif event.type == "QUIT":
            self.final = True

        if inputhandler.poll_button("up") and not inputhandler.poll_button("down"):
            self.player.velocity.y = self.player.speed * -1
        elif inputhandler.poll_button("down") and not inputhandler.poll_button("up"):
            self.player.velocity.y = self.player.speed * 1
        else:
            self.player.velocity.y = 0

        if inputhandler.poll_button("left") and not inputhandler.poll_button("right"):
            self.player.velocity.x = self.player.speed * -1
        elif inputhandler.poll_button("right") and not inputhandler.poll_button("left"):
            self.player.velocity.x = self.player.speed * 1
        else:
            self.player.velocity.x = 0

    def update(self, dt):
        self.player.update(dt)
        self.entity_handler.update(dt)
        self.background.scroll(dt)