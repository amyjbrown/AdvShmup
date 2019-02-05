# encoding * utf - 8 *
"""
Gamescene
Where almost everything lives and works
TODO: Move all entity handler code into here
"""
import shmup.background as background
import shmup.entity as entity
import shmup.inputhandler as inputhandler
import shmup.scene.scenebase as scenebase
from shmup.config import *

inputhandler.setup(DEBUG_MAP)


class GameScene(scenebase.Scene):
    """
    GameScene
    """
    def __init__(self):
        super().__init__()
        # base game values
        self.level = None
        self.level_data = None  # This is where level data will live
        self.score = 0
        self.lives = 3

        self.background = None

        # Entity groups

        self.player = None
        self.player_group = pg.sprite.GroupSingle()
        self.enemy = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.enemy_bullets = pg.sprite.Group()
        self.effects = pg.sprite.Group()
        # Internal handling
        self.groups = [self.effects, self.enemy, self.enemy_bullets, self.bullets, self.powerups]

        self.game_progress = 0.0

    def add_score(self, score, combo=False):
        """Adds any scored points to score"""
        self.score += score

    def load(self, level=None, reset=True):
        """
        Overload

        Args:
            level (int): number id of level to be loaded
            reset (bool): fully reset Game on level if True

        Returns:
            None
        """
        if reset:
            # Do all enetity setup
            entity.Player.setup(self)

            for enemy in entity.Enemy:
                enemy.setup(self)

            self.player = entity.Player((100, 100))

            self.background = background.BackGround("../assets/BG1.bmp", FPS)

    def handle_input(self, event):
        if event.key == "menu":
            self.final = True
        elif event.key == "QUIT":
            self.final = True
        elif event.key == "debug1" and event.down:
            print("Player velcoity: ",
                  self.player.vx, self.player.vy)

        # movement handling

        #        elif event.key == "down":
        #            # If player is not moving, set players downward velocity
        #            if event.down and (self.player.vy == 0.0):
        #                self.player.vy = self.player.speed
        #            # If player is moving upwards, pressing down will cancel it out
        #            elif event.down and self.player.vy > 0.0:
        #                self.player.vy = 0
        #            # If player is moving down and lets go of the down key, player will stop moving
        #            elif event.up and self.player.vy > 0.0:
        #                self.player.speed = 0
        #            elif event.up and self.player.vy == 0.0:
        #                self.player.vy = -self.player.speed

        if inputhandler.poll_button("up") and not inputhandler.poll_button("down"):
            self.player.velocity.y = self.player.speed * -1
        elif inputhandler.poll_button("down") and not inputhandler.poll_button("up"):
            self.player.velocity.y = self.player.speed * 1
        else:
            self.player.velocity.y = 0

        if inputhandler.poll_button("left") and not inputhandler.poll_button("right"):
            self.player.velocity.x = self.player.speed * -1
        elif inputhandler.poll_button("right") and not inputhandler.poll_button("left"):
            self.player.velocity.x = self.player.speed * 1
        else:
            self.player.velocity.x = 0

        if inputhandler.poll_button("fire"):
            self.player.fire()

    def update(self, dt):
        self.background.update(dt)
        # Updates and handles player status and all entities movement
        self.player.update(dt)
        for g in self.groups:
            g.update(dt)

        # Do all collision detection
        for enemy in pg.sprite.spritecollide(self.player, self.enemy, False,
                                             collided=entity.hit_collide):
            enemy.collide(self.player)

        for bullet in pg.sprite.spritecollide(self.player, self.enemy_bullets,
                                              dokill=True, collided=entity.hit_collide):
            bullet.collide(self.player)

        for token in pg.sprite.spritecollide(self.player, self.powerups,
                                             dokill=False, collided=entity.hit_collide):
            token.effect(self.player)

        for bullet, enemy in pg.sprite.groupcollide(self.bullets, self.enemy,
                                                    dokilla=False, dokillb=False,
                                                    collided=entity.hit_collide).items():
            bullet.collide(enemy)

        # if the player is at zero health, do appropriate transition
        if self.player.health <= 0:
            self.final = True

    def draw(self, screen):
        self.background.draw(screen)
        for g in self.groups:
            g.draw(screen)
        self.player_group.draw(screen)
