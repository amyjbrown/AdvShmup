"""
Main application file
Run this script to play the game
TODO relative path towards the assets folder
"""
# imports
import pygame as pg
from shmup.config import *
import shmup.inputhandler as inputhandler
import shmup.scene.gamescene

pg.init()
screen = pg.display.set_mode(GAME_AREA)
inputhandler.setup(KEY_MAP)
mainscene = shmup.scene.gamescene.GameScene()

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
