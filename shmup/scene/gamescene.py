# encoding * utf - 8 *
"""
Gamescene
Where almost everything lives and works
"""
import background
import entity.entityhandler as entityhandler
import inputhandler
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

        self.background = None

        # game
        # Todo Screenbackground
        # Todo background = scroller()

        self.game_progress = 0.0

    def add_score(self, score, combo):
        """Adds any scored points to score"""
        self.score += score

    def load(self, level=0, reset=False):
        """
        Overload

        Args:
            level (int): number id of level to be loaded
            reset (bool): fully reset Game on level if True

        Returns:
            None
        """
        if reset:
            self.entity_handler.setup()
            self.game_progress = 0.0
            self.background = background.BackGround(
                "../assets/BG1.bmp",
                speed=FPS
            )

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
        self.background.update(dt)
        if self.player.health <= 0:
            self.final = True

    def draw(self, screen):
        self.background.draw(screen)
        self.entity_handler.draw(screen)
