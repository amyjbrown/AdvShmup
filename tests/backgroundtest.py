# encoding * utf-8 *
"""
Scrolling Background Test
PASS
"""

import pygame as pg
from shmup.config import *
import shmup.inputhandler as inputhandler
import shmup.background as background

pg.init()
inputhandler.setup(DEBUG_MAP)
screen = pg.display.set_mode(GAME_AREA)

path = r"../assets/BG1.bmp"
bg = background.BackGround(path, FPS)


clock = pg.time.Clock()
game = True
while game:
    dt = clock.tick(FPS) / 1000
    for event in inputhandler.get():
        if event.key == "QUIT":
            game = False
        elif (event.key == "console" or event.key == "debug1") and event.down:
            try:
                bg.speed = int(input("New scroll speed: "))
                bg.y1 = 0
                bg.y2 = bg.h
            except ValueError:
                print("Invalid speed, reverting speed to " + str(bg.speed))
            finally:
                print("Speed is currently " + str(bg.speed))
    bg.update(dt)
    bg.draw(screen)
    pg.display.flip()

# cleanup
pg.quit()
