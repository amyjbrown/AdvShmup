# encoding * utf - 8 *
"""
Tests custom event handling function
SUCCESS
"""
# Import
import pygame as pg
import shmup.inputhandler as inputhandler
from shmup.config import *
# Setup
pg.init()
inputhandler.setup(KEY_MAP)
screen = pg.display.set_mode((500, 500))

game = True
while game:
    for event in inputhandler.get():
        if event.key == "QUIT":
            game = False
        print(event)

