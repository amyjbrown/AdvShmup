# encoding * utf - 8 *
"""
Gamescene
Where almost everything lives and works
"""
import shmup.background as background
import shmup.entity as entity
import shmup.inputhandler as inputhandler
import shmup.scene.scenebase as scenebase
import shmup.entity
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
            entity.setup(self)

            self.player = entity.Player((100, 100))

            self.background = background.BackGround("../assets/BG1.bmp", FPS)

    def handle_input(self, event):
        """
        Takes an input and appropriate updates the game
        Has now been fully decoupled
        """
        # general exit or other thing keys
        if event.key == "menu":
            self.final = True
        elif event.key == "QUIT":
            self.final = True

        # Movement keys and handling
        elif event.key == "up" and event.down:
            if self.player.vy == 0:
                self.player.vy = -self.player.speed
                return
            elif self.player.vy > 0:  # player is holding down, shift to going up
                self.player.vy = 0
                return

        elif event.key == "up" and event.up:
            if self.player.vy == 0:
                self.player.vy = self.player.speed
            elif self.player.vy < 0:
                self.player.vy = 0

        elif event.key == "down" and event.down:
            if self.player.vy == 0:
                self.player.vy = self.player.speed
                return
            elif self.player.vy < 0:  # player is holding up, shift to going down
                self.player.vy = 0
                return

        elif event.key == "down" and event.up:
            if self.player.vy == 0:
                self.player.vy = - self.player.speed
            elif self.player.vy > 0:
                self.player.vy = 0

        elif event.key == "right" and event.down:
            if self.player.vx == 0:
                self.player.vx = self.player.speed
                return
            elif self.player.vx < 0:  # player is holding down, shift to going up
                self.player.vx = 0
                return

        elif event.key == "right" and event.up:
            if self.player.vx == 0:
                self.player.vx = - self.player.speed
            elif self.player.vx > 0:
                self.player.vx = 0

        elif event.key == "left" and event.down:
            if self.player.vx == 0:
                self.player.vx = - self.player.speed
                return
            elif self.player.vx > 0:  # player is holding down, shift to going up
                self.player.vx = 0
                return

        elif event.key == "left" and event.up:
            if self.player.vx == 0:
                self.player.vx = self.player.speed
            elif self.player.vx < 0:
                self.player.vx = 0

        elif event.key == "fire":
            if event.down:
                self.player.firing()
            else:
                self.player.firing(False)

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

        for bullet, enemy_list in pg.sprite.groupcollide(self.bullets, self.enemy,
                                                         dokilla=True, dokillb=False,
                                                         collided=entity.hit_collide).items():
            for enemy in enemy_list:
                bullet.collide(enemy)

        # if the player is at zero health, do appropriate transition
        if self.player.health <= 0:
            self.final = True

    def draw(self, screen):
        self.background.draw(screen)
        for g in self.groups:
            g.draw(screen)
        self.player_group.draw(screen)
