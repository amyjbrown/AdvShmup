# encoding * utf-8 *
"""
Basic Font shit
<Detail>
"""
import pygame as pg
import random
import string
import os.path
from pprint import pprint
from shmup.config import *
import shmup.inputhandler as inputhandler


# setup
pg.init()
inputhandler.setup(DEBUG_MAP)
screen = pg.display.set_mode(RESOLUTION)
pg.font.init()

# test items go here
test_font = pg.font.SysFont(None, 20)
texts = [*string.ascii_letters, *string.digits, " "]


def ran_text(size: int=10) -> str:
    """Generate a `size` sized random text"""
    t = random.choices(texts, k=size)
    return "".join(t)


# game-loop
game = True
clock = pg.time.Clock()
while game:
    dt = clock.tick(FPS) / 1000
    for event in inputhandler.get():

        if event.key == "fire" and event.down:
            screen.fill(BLACK)
            test_text = ran_text(30)
            sfv = test_font.render(test_text, True, RED)
            screen.blit(sfv, (7, 6))

        elif event.key == "menu" or event.key == "exit":
            game = False
            continue

        elif event.key == "console" and event.down:
            screen.fill(BLACK)
            test_text = input("Enter Displayed Test")
            print(test_font.size(test_text))  # Get output of size
            sfv = test_font.render(test_text, True, RED)
            screen.blit(sfv, (7, 6))

        elif event.key == "debug1" and event.down:
            screen.fill(BLACK)
            print(test_font.size("".join(texts)))  # Get output of size
            sfv = test_font.render("".join(texts), True, RED)
            screen.blit(sfv, (7, 6))

        elif event.key == "debug2":
            screen.fill(BLACK)
            wid = []
            for i in texts:
                y = test_font.size(i)
                wid += y
                print("`{}`: {}".format(i, y))
            print(sum(wid) / len(wid))
    # Loop based code goes here
    # Render code
    pg.display.flip()
