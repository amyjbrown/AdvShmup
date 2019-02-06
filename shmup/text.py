"""
Text Drawing Helper Function

[Experimental]
Library of helper functions for drawing text on screen and cache of font items for quick and easy rendering
"""
import pygame as pg
from shmup.config import *

pg.init()

default_font = pg.font.SysFont(pg.font.get_default_font(), 20)

_cache = {}


def draw(surface, text, position, color, antialias=True, font=default_font, size=20):
    """
    Drawas the text
    Args:
        surface (Text to draw on the screen):
        text (str): Single line of text to draw on the screen1
        position (tuple<int, int>):
        color (Color, Tuple<int, int, int>): Color of font to be used
        antialias (bool): True to use Antialiasizing
        font (Font): Font to be used. Defaults to system Font
        size (int): Size for drawing glyphs, in pixels height. Defaults to 20

    Returns:
        None
    """
    temp = pg.font.SysFont(font, size, antialias, color).render(text, antialias, color)
    surface.blit(temp, position)
