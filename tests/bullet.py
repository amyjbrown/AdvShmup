# encoding * utf-8 *
"""
Testing Topic Goes Here
"""
import pygame as pg
from shmup.config import *
import shmup.inputhandler as inputhandler

# setup
pg.init()
inputhandler.setup(DEBUG_MAP)
screen = pg.display.set_mode(GAME_AREA)

# gameloop
game = True
clock = pg.time.Clock()
while game:
    dt = clock.tick(FPS) / 1000
    for event in inputhandler.get():
        if event.key == "QUIT":
            game = False
        elif event.key == "console":
            pass
        # Event based code goes here
    # Loop based code goes here
    pg.display.flip()
