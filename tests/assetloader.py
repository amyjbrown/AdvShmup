# encoding * utf-8 *
"""
Image Loading via Sprite
Check if IMAGE can be loaded, and if Spritesheet color works
PASS 1/25/2019 12: 12
"""
import pygame as pg
import os.path
from pprint import pprint
from config import *
import shmup.inputhandler as inputhandler
import spritesheet

# setup
pg.init()
inputhandler.setup(DEBUG_MAP)
screen = pg.display.set_mode(GAME_AREA)

rpath = r"../assets"
shippath = os.path.join(rpath, "Ship.bmp")
sheetpath = os.path.join(rpath, "IslandTiles.bmp")

# test items go here
ship = spritesheet.load(
    shippath,
    True
)

strip = spritesheet.get_list(
    sheetpath,
    pg.Rect(0, 0, 64, 64),
    pg.Rect(64, 0, 64, 64),
    pg.Rect(128, 0, 64, 64),
    pg.Rect(192, 0, 64, 64),
    colorkey=False
)

solo = spritesheet.get_image(
    os.path.join(rpath, "IslandTiles.bmp"),
    pg.Rect(64, 64, 64, 64),
    False
)

full_strip = spritesheet.get_full(
    os.path.join(rpath, "IslandTiles.bmp"),
    (64, 64),
    False
)

pprint(spritesheet._cache)

# gameloop
game = True
clock = pg.time.Clock()
while game:
    dt = clock.tick(FPS) / 1000
    for event in inputhandler.get():
        if event.key == "QUIT":
            game = False

        elif event.key == "debug5" and event.down:
            screen.fill(BLACK)

        elif event.key == "debug1" and event.down:
            screen.fill(BLACK)
            im = spritesheet.load(shippath, colorkey=True)
            screen.blit(im, (0, 0))

        elif event.key == "debug2" and event.down:
            screen.fill(BLACK)
            im = spritesheet.load(shippath, colorkey=False)
            screen.blit(im, (0, 0))

        elif event.key == "debug3" and event.down:
            screen.fill(BLACK)
            for i, im in enumerate(strip):
                screen.blit(im, (0, 64 * i))

        elif event.key == "debug4" and event.down:
            screen.fill(BLACK)
            for i in range(4):
                for j in range(4):
                    screen.blit(
                        full_strip[i * 4 + j],
                        (64 * i, 64 * j)
                    )

    # Loop based code goes here
    pg.display.flip()
