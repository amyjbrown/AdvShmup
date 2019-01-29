# encoding * utf - 8 *
"""
Unit Test for Button Polling
PASS
"""
# Import
import pygame as pg
import shmup.inputhandler as inputhandler
from shmup.config import *
# Setup
pg.init()
inputhandler.setup(KEY_MAP)
screen = pg.display.set_mode((500, 800))
font = pg.font.SysFont(
    pg.font.get_default_font(),
    30
)


def screen_print():
    for i, button in enumerate(KEYS):
        text = ">{}: {}".format(button,
                                inputhandler.poll_button(button)
                                )
        im = font.render(text, False, GREEN, BLACK)
        screen.blit(im, (5, 5 + 30 * i))



game = True
clock = pg.time.Clock()
while game:
    screen.fill(BLACK)
    clock.tick(60)
    for event in inputhandler.get():
        if event.key == "QUIT":
            game = False
    screen_print()
    pg.display.flip()
