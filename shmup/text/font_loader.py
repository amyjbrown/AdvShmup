# encoding - * utf - 8 * -
"""
This is the private API for loading and managing fonts

_cache: Dictionary of cache fonts
FontID: Alias for Font item
*init: appropriately setups up how fonts will be loaded, check if font and truefont are installed and work
*cahce_font
*id_font: Generates the appropriate Font-Identifying Tuple
"""
from typing import *
from pygame.font import Font

FontID: Tuple[str, int, bool, bool, bool]

_cache: Dict[Tuple[str, int, bool, bool, bool], Font] = dict()


def setup() -> None:
    """
    Initialize and check to see if things are properly installed

    This should be autocalled

    Returns:
        None
    """
    pass


def cache_font(font: Font) -> None:
    pass