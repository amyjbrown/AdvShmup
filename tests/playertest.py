# encoding * utf-8 *
"""
Actor and Play
Testing Player Startup, screen loading, and simple movement
PASS 1/25/2019
"""
import shmup.entity.actor.player as player
import shmup.inputhandler as inputhandler
from shmup.config import *

# setup
pg.init()
inputhandler.setup(DEBUG_MAP)
screen = pg.display.set_mode(GAME_AREA)

Player = player.Player
Player.setup(None)  # None is fine since you do no operations on it

SPEED = 90  # Pixels per second

draw_group = pg.sprite.Group()
p1 = Player(
    (0, 0),
    draw_group
)

# gameloop
game = True
clock = pg.time.Clock()
while game:
    screen.fill(BLACK)
    dt = clock.tick(FPS) / 1000
    for event in inputhandler.get():
        if event.key == "QUIT":
            game = False
        elif event.key == "console" and event.down:
            try:
                SPEED = int(input("Enter new player speed: "))
            except ValueError:
                print("Invalid Speed")
        if event.down:
            if event.key == "up":
                p1.velocity.y = -SPEED
            elif event.key == "down":
                p1.velocity.y = SPEED
            elif event.key == "right":
                p1.velocity.x = SPEED
            elif event.key == "left":
                p1.velocity.x = -SPEED
        else:
            if event.key in ["up", "down"]:
                p1.velocity.y = 0
            elif event.key in ["left", "right"]:
                p1.velocity.x = 0
    p1.update(dt)
    draw_group.draw(screen)
    pg.display.flip()
