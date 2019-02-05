# encoding * utf-8 *
"""
Testing Asteroid Hazard
"""
# imports
import pygame as pg
from shmup.config import *
import shmup.inputhandler as inputhandler
import shmup.scene.gamescene
import shmup.entity

pg.init()
screen = pg.display.set_mode(GAME_AREA)
inputhandler.setup(DEBUG_MAP)
mainscene = shmup.scene.gamescene.GameScene()

mainscene.load(reset=True)

print(shmup.entity == shmup.scene.gamescene.entity)

playing = True
clock = pg.time.Clock()
shmup.entity.Asteroid(50, 50)
while playing:
    # for i in mainscene.enemy:
    #    print(i.position)
    dt = clock.tick(FPS) / 1000
    for event in inputhandler.get():
        if event.key == "debug1" and event.down:
            shmup.entity.Asteroid(50, 50)
        mainscene.handle_input(event)
        if mainscene.final:
            playing = False
    mainscene.update(dt)
    mainscene.draw(screen)
    pg.display.set_caption(str(mainscene.player.health))
    pg.display.flip()
