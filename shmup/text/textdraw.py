# encoding * - utf - 8 - *
"""
TODO
"""
import pygame as pg


def word_length(text: str, font: pg.font.Font) -> pg.Rect:
    """

    Args:
        text:
        font:

    Returns:

    """
    return font.size(text)


def render_text(text: str, font: pg.font.Font, size) -> pg.Surface:
    """
    Algorithim for outputing a complex line of string

    TODO
        Much of the work and what parameters to use
        This function should be used for MiniMarkup Text, and will be reworked many times

    Args:
        text: Text to be rendered
        font: Font to be used
        size: of rendering

    Returns:
        pygame Surface: Return the text all drawn onto an image
    """

    local_surface = pg.Surface(*size)

    line_width = size[0]
    line_height = size[1]
    cursor = pg.Vector2(*size)

    word = ""
    for n, char in enumerate(text):

        if char in ["\n", " ", "\t"] or n == len(text) -1:
            # TODO implement printing text
            pass

        else:
            word += char
