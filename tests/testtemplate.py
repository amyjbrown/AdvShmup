# encoding * utf-8 *
"""
{Module being tested}
{Behavior being tested}
PASS? <TimeStamp>

Notes:
    Notes go here
"""
import pygame as pg
from shmup.config import *
import shmup.inputhandler as inputhandler


# initialization
pg.init()
inputhandler.setup(DEBUG_MAP)
screen = pg.display.set_mode(GAME_AREA)


# Items to be tested go here

# Game Loop
clock = pg.time.Clock()
game = True
while game:
    dt = clock.tick(FPS) / 1000
    for event in inputhandler.get():
        if event.key == "QUIT":
            game = False
        elif event.key == "console" and event.down:
            # debug prompts go here
            pass
        # per event code
    # per loop code
    pg.display.flip()

# cleanup
pg.quit()