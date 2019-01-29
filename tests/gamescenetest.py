# encoding * utf-8 *
"""
Game Scene logic
Testing to see if Game Scene runs
Goals: gamescene should be constructed and load() called
Gamescene should have a simple moving player object, a scrolling background, and quits upon hitting `ESC` or quitting

"""
import pygame as pg
from shmup.config import *
import shmup.inputhandler as inputhandler
import shmup.scene.gamescene as gamescene

# setup
pg.init()
inputhandler.setup(DEBUG_MAP)
screen = pg.display.set_mode(GAME_AREA)

Scene = gamescene.GameScene()
Scene.load(reset=True)

# gameloop
game = True
clock = pg.time.Clock()
while game:
    dt = clock.tick(FPS) / 1000
    for event in inputhandler.get():
        Scene.handle_input(event)
        if Scene.final:
            game = False
        # Event based code goes here
    Scene.update(dt)
    Scene.draw(screen)
    pg.display.flip()
