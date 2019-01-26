# encoding * utf - 8 *
"""
spritesheet assetloading service
Unless otherwise needed, use this for loading in sprites and images

*API for loading in images
*Cache for spritesheets and open images
"""
import sys
import os
import pygame as pg
import spritesheet.spritesheet as spritesheet
pg.init()

# Locally creates cache
_cache = dict()
# Appropriate Alias
Spritesheet = spritesheet.Spritesheet


def load(path, colorkey):
    """
    Loads and gets one spritesheet or image

    Args:
        path (str, path): Path (relative or local) to asset to load
        colorkey (bool): Point from which to set colorkey transparency
            if None, colorkey will not be used, if True the topleft corner (0,0) is used

    Returns:
        pg.Surface Surface of file, converted and using colorkey at point (x,y) if specified
    """
    # Automaticaly return if file has already been loaded
    if path in _cache:
        return _cache[path].get_sheet(colorkey)
    else:
        sheet = Spritesheet(path, colorkey)
        _cache[path] = sheet
        return sheet.get_sheet(colorkey)


def get_image(path, rect, colorkey):
    """Returns the image located at rect"""
    if path in _cache:
        return _cache[path].get_image(rect, colorkey)
    else:
        sheet = Spritesheet(path, colorkey)
        _cache[path] = sheet
        return sheet.get_image(rect, colorkey)


def get_list(path, *rects, colorkey=True):
    """Get a series of images from path"""
    if path in _cache:
        return _cache[path].get_list(*rects, colorkey)
    else:
        sheet = Spritesheet(path, colorkey)
        _cache[path] = sheet
        return sheet.get_list(*rects, colorkey=colorkey)


def get_full(path, size, colorkey=True):
    """Get every image from a grid of size Rects"""
    if path in _cache:
        return _cache[path].full_load(size, colorkey)
    else:
        sheet = Spritesheet(path, colorkey)
        _cache[path] = sheet
        return sheet.full_load(size, colorkey)


def clear_cache():
    """Clears Cache"""
    global _cache
    _cache = dict()
