# encoding * utf-8 *
"""
<Tested Module>
<Test Time>
<Pass>
<Detail>
"""
import pygame as pg
import os.path
from pprint import pprint
from pygame import freetype as freetype
from shmup.config import *
import shmup.inputhandler as inputhandler
# setup
pg.init()
inputhandler.setup(DEBUG_MAP)
screen = pg.display.set_mode(RESOLUTION)

# test items go here
freetype.SysFont(None, 20)

# game-loop
game = True
clock = pg.time.Clock()
while game:
    dt = clock.tick(FPS) / 1000
    for event in inputhandler.get():
        pass
    # Loop based code goes here

    # Render code
    pg.display.flip()
