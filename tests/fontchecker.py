# encoding * utf-8 *
"""
Test every font in sysfonts
{Behavior being tested}
PASS?

Notes:
    Notes go here
"""
import pygame as pg
from shmup.config import *
import shmup.inputhandler as inputhandler

# initialization
pg.init()
inputhandler.setup(DEBUG_MAP)
screen = pg.display.set_mode((1000, 300))

# Items to be tested go here
fonts = pg.font.get_fonts()
end = len(fonts) - 1
index = 0  # index of font to be tested
TEXT = "The quick brown fox jumps over the lazy dog."


def render():
    global index
    screen.fill(BLACK)
    f = pg.font.SysFont(fonts[index], 16)
    fb = pg.font.SysFont(fonts[index], 16, bold=True)
    fi = pg.font.SysFont(fonts[index], 16, italic=False)
    fbi = pg.font.SysFont(fonts[index], 16, bold=True, italic=True)
    # print font title
    print(fonts[index])
    screen.blit(f.render(fonts[index], True, WHITE),
                (2, 2))
    # print f, bold, italic, bold italic
    screen.blit(f.render(TEXT, True, WHITE),
                (2, 20))
    screen.blit(fb.render(TEXT, True, WHITE), (2, 38))
    screen.blit(fi.render(TEXT, True, WHITE, ), (2, 56))
    screen.blit(fbi.render(TEXT, True, WHITE), (2, 74))


# Game Loop
clock = pg.time.Clock()
game = True
while game:
    dt = clock.tick(FPS) / 1000
    for event in inputhandler.get():
        if event.key == "QUIT" or event.key == "menu":
            game = False
        elif (event.key == "fire" or event.key == "right") and event.down:
            if index == end:
                break
            index += 1
            render()
        elif event.key == "left" and event.down:
            if index == 0:
                break
            index -= 1
            render()
        elif event.key == "console" and event.down:
            # debug prompts go here
            pass
        # per event code
    # per loop code
    pg.display.flip()
