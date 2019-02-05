# encoding * utf - 8 *
"""
Global Constants and other useful info for initialization

Attributes:
    GAME_AREA (list<int>): total size of the game area and Screen space
    GAME_RECT (pg.Rect): Total Rect of playable screenspace
    EXTENDEND_RECT (pg.Rect): Extended Rect used for enemy despawning
    KEYS (list<str>): List of ingame Keys
    KEY_MAP (dict<str, pg.event>): default key mapping
    DEBUG_MAP (dict<str, pg.event>): Extended key mappings for debug mode and testing
"""
import pygame as pg

GAME_AREA = (480, 640)
GAME_RECT = pg.Rect(0, 0, 480, 640)
EXTENDED_RECT = pg.Rect(-64, -64, 608, 768)
FPS = 60

# Keymaps
KEYS = [
    "menu",
    "up", "down", "left", "right",
    "fire", "missile", "bomb"
]

DEBUG_KEYS = [
    *KEYS,
    "console",
    "debug1", "debug2", "debug3", "debug4", "debug5"
]

KEY_MAP = {"up": [pg.K_UP, pg.K_w],
           "down": [pg.K_DOWN, pg.K_s],
           "right": [pg.K_RIGHT, pg.K_d],
           "left": [pg.K_LEFT, pg.K_a],
           "menu": [pg.K_ESCAPE],
           "fire": [pg.K_SPACE],
           "missile": [pg.K_x],
           "bomb": [pg.K_z],
           }

DEBUG_MAP = {
    **KEY_MAP,
    "console": [pg.K_RETURN],
    "debug1": [pg.K_1],
    "debug2": [pg.K_2],
    "debug3": [pg.K_3],
    "debug4": [pg.K_4],
    "debug5": [pg.K_5]
}

# Color Constants
RED = pg.Color(255, 0, 0)
BLUE = pg.Color(0, 0, 255)
GREEN = pg.Color(0, 255, 0)
YELLOW = pg.Color(255, 255, 0)
PURPLE = pg.Color(255, 0, 255)
ORANGE = pg.Color(255, 128, 0)
CYAN = pg.Color(0, 255, 255)
WHITE = pg.Color(255, 255, 255)
BLACK = pg.Color(0, 0, 0)
GREY = pg.Color(127, 127, 127)