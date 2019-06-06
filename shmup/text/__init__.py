# encoding * utf - 8 *
"""
This is the public interface for text_rendering

*load_font: push a font into the cache with appropriate flags
*get_font: get a font object and add it to the cache
*basic_draw: easy to use textdrawing function
*markup_draw: Draw MiniMarkup string
*clear_cache: clear local cache
*get_log: get results of logging file
"""
from typing import *
import pygame as pg

Font = pg.font.Font


def load_font(*fonts: List[str], size: int = 20, use_default: bool = True, **kwargs) -> None:
    """
    Load one font from a series of hierarchically ranked choices

    Use this for adding a font you want to the setup of fonts, and also for various other features
    This houses an interface for all the messy stuff

    Args:
        *fonts: List of fonts to be chosen, with preference towards first listed font
        size: size of the wanted loaded fonts
        use_default: Use Default python Font, False is otherwise - will raise an exception if can't find other fonts

    Kwargs:
        italic(bool|None): True for get Italic version of font, False for non-italic, None to add both. Default False
        bold(bool|None): True to get Bolded version of font, False for non-italic, None to add both
        underline(bool|None): True to get Underlined font version, False for none, None for both

    Returns: None

    Raises:
        pygame.Error:  Error if loaded font can't be found
    """
    pass


def get_font(*fonts: List[str], size: int = 20, **kwargs) -> Font:
    """
    Get font object from appropriate font_name, use this for anything where you handle Fonts directly

    This will cache a font object, unless otherwise specified. Use this for any and all direct testing or weird things
    you gotta do.

    Args:
        *fonts: Hierarchical font choices to load, first being the highest rated
        size: Size of font element

    Kwargs:
        italic(bool): True for Italic font version, False for normal
        bold(bool): True for Bolded font version, false for otherwise
        underline(bool): True for Underlined font version, False for normal

    Returns: Appropriate Font object with params all preset

    Raises:

    """
    pass


def basic_draw(text: str, target: pg.Surface, font: Font = None, antialias: bool = None) -> None:
    """
    Todo: What kind of format do I want?
    Args:
        text:
        target:
        font:

    Kwargs:

    Returns:

    """
    pass


def markup_draw(text) -> bool:
    """
    Draw a MiniMarkup styled string

    This is *the* function I'm making for this whole mini-library

    Args:
        text: MiniMarkup string

    Returns:

    """
    pass


def clear_cache() -> None:
    """
    Clears local cache of fonts, including pre-loads

    Returns: None
    """
    pass


def get_log(export: str = None) -> str:
    """
    Print out the text rendering debug log, optionally store it in a file

    Args:
        export: Path to where outputed debug log should be put, if None then don't output

    Returns:
        str: outputs whole log
    """