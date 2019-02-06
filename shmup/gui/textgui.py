"""
Text Gui for drawing simple information

"""
import pygame as pg

pg.init()
from shmup.config import *


class TextGUI:
    """
    Simple Text based heads up display for showing player information

    Args:
        scene (Scene): Scene the gui will render on

    Attributes:
        font (Font): Font used for rendering

    """

    def __init__(self, scene):
        self.font = pg.font.SysFont("comicsansms", 16, bold=True)
        self.scene = scene

    def draw(self, screen, dt):
        """
        Draws heads up display info onto screen

        Args:
            screen (Surface): Screen to be rendered onto
            dt (float): Elapsed time
        """
        hp_text = "HEALTH {:03} | 100".format(self.scene.player.health)
        lives_text = "LIVES {:02}".format(self.scene.lives)
        score_text = "SCORE {:06}".format(self.scene.score)
        fps_text = "{:02.2f} fps".format(1 / dt)

        screen.blit(
            self.font.render(hp_text, True, GREEN),
            (4, 4)
        )
        screen.blit(
            self.font.render(lives_text, True, GREEN),
            (4, 22)
        )
        screen.blit(
            self.font.render(score_text, True, YELLOW),
            (4, 42)
        )
        screen.blit(
            self.font.render(fps_text, True, RED),
            (4, 62)
        )
