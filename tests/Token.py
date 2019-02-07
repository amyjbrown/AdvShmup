# encoding * utf-8 *
"""
Testing Topic Goes Here
"""
# imports
import pygame as pg
from shmup.config import *
import shmup.inputhandler as inputhandler
import shmup.scene.gamescene
import shmup.entity

pg.init()
screen = pg.display.set_mode(RESOLUTION)
inputhandler.setup(DEBUG_MAP)
mainscene = shmup.scene.gamescene.GameScene()

shmup.entity.HighPointToken.setup(mainscene)

mainscene.load(reset=True)

playing = True
clock = pg.time.Clock()
while playing:
    dt = clock.tick(FPS) / 1000
    for event in inputhandler.get():
        mainscene.handle_input(event)
        if mainscene.final:
            playing = False
    mainscene.update(dt)
    mainscene.draw(screen)
    pg.display.flip()
