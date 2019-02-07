# encoding * utf-8 *
"""
text.py test
testing to see if I can actually post fonts in

Notes:
    Want this for general purpose text drawing
"""
import pygame as pg
from shmup.config import *
import shmup.inputhandler as inputhandler
import shmup.text as text

# initialization
pg.init()
inputhandler.setup(DEBUG_MAP)
screen = pg.display.set_mode(RESOLUTION)

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
    text.draw(screen,
              "Hello World!",
              GREEN,
              (20, 20),
              size=30)
    pg.display.flip()
