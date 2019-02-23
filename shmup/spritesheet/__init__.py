# encoding * utf - 8 *
"""
spritesheet assetloading service
Unless otherwise needed, use this for loading in sprites and images

*API for loading in images
*Cache for spritesheets and open images
*Standard, module wide path for assets to be loaded from
"""
import os.path
import pygame as pg
from shmup.config import *
import shmup.spritesheet.spritesheet
pg.init()

# Locally creates cache
_cache = dict()
# Appropriate Alias
Spritesheet = spritesheet.Spritesheet

# Create asset path for use that will be unambigious in the entire file
ASSET_PATH = os.path.join(GLOBAL_PATH, "assets")


def _path(name: str):
    """
    Get static path to asset named

    Use this for all asset loading

    Args:
        name (str): Name or Path of file in asset folder

    Returns:
        (str) Absolute path to asset file in name.

    Raises:
        OSError: The file doesn't exist
    """
    return os.path.join(ASSET_PATH, name)


def load(path, colorkey):
    """
    Loads and gets one spritesheet or image

    Args:
        path (str, path): Path (relative) to asset to load
        colorkey (bool): Point from which to set colorkey transparency
            if None, colorkey will not be used, if True the topleft corner (0,0) is used

    Returns:
        pg.Surface Surface of file, converted and using colorkey at point (x,y) if specified
    """
    tpath = _path(path)
    if tpath in _cache:
        return _cache[tpath].get_sheet(colorkey)
    else:
        sheet = Spritesheet(tpath, colorkey)
        _cache[tpath] = sheet
        return sheet.get_sheet(colorkey)


def get_image(path, rect, colorkey):
    """Returns the image located at rect"""
    tpath = _path(path)
    if tpath in _cache:
        return _cache[tpath].get_image(rect, colorkey)
    else:
        sheet = Spritesheet(tpath, colorkey)
        _cache[tpath] = sheet
        return sheet.get_image(rect, colorkey)


def get_list(path, *rects, colorkey=True):
    """Get a series of images from path"""
    tpath = _path(path)
    if tpath in _cache:
        return _cache[tpath].get_list(*rects, colorkey)
    else:
        sheet = Spritesheet(tpath, colorkey)
        _cache[tpath] = sheet
        return sheet.get_list(*rects, colorkey=colorkey)


def get_full(path, size, colorkey=True):
    """Get every image from a grid of size Rects"""
    tpath = _path(path)
    if tpath in _cache:
        return _cache[tpath].full_load(size, colorkey)
    else:
        sheet = Spritesheet(tpath, colorkey)
        _cache[tpath] = sheet
        return sheet.full_load(size, colorkey)


def clear_cache():
    """Clears Cache"""
    global _cache
    _cache = dict()
