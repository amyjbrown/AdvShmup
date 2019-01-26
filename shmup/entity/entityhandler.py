# encoding * utf - 8 *
"""
High level entity control and management

*EntityHandler: Handler component for entities to be used in a scene
*hitbox_check: callback function for custom Actor type's hitboxes
TODO: Fully Implement EntityHandler
"""
import pygame as pg


# TODO move this collision function elsewhere
def hit_collide(a, b):
    """
    Check if two sprites hitboxes are interacting

    Args:
        a (Sprite): Sprite A to be collided. Must have hitbox field
        b (Sprite): Sprite B to check Collision. Must have hitbox field

    Returns:
        True is hitboxes are colliding, Fale otherwise
    """
    if a.hitbox.collide(b.hitbox):
        return True
    return False


class EntityHandler:
    """
    Entity controller and _handler

    Args:
        observer (Scene): Observing Scene element

    Attributes:
        observer (Scene): Scene containing element
        player (Actor):
        enemy (Group):
        powerups (Group):
        bullets (Group):
        enemy_bullets (Group)
        effects (Group):
    """

    def __init__(self, observer):
        self.observer = observer
        # Group declaration
        self.player = None
        self.enemy = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.enemy_bullets = pg.sprite.Group()
        self.effects = pg.sprite.Group()
        # Internal handling
        self.groups = [self.effects, self.enemy, self.enemy_bullets, self.bullets, self.powerups]
        return

    def setup(self):
        # Performs setup
        # TODO: Implement
        pass

    def update(self, dt):
        """
        Update all entities
        TODO: IMPLEMENT

        Args:
            dt (float): Time update

        Returns:
            None
        """
        # Updates and handles player status and all entities movement
        self.player.update(dt)
        for g in self.groups:
            g.update(dt)

        for enemy in pg.sprite.spritecollide(self.player, self.enemy, False, collided=hit_collide):
            enemy.collide(self.player)

        for bullet in pg.sprite.spritecollide(self.player, self.enemy_bullets, dokill=True, collided=hit_collide):
            bullet.collide(self.player)

        for token in pg.sprite.spritecollide(self.player, self.powerups, dokill=False, collided=hit_collide):
            token.effect(self.player)

        for colissions in pg.sprite.spritecollide(self.player, self.powerups, dokill=False, collided=hit_collide):
            pass  # TODO the collisions detection bit


    def draw(self, screen):
        screen.blit(
            self.player,
            self.player.rect
        )
        for g in self.groups:
            g.draw(screen)

    def clear_enemy(self):
        """
        Clears all animations, enemies and bullets
        """
        self.enemy.empty()
        self.enemy_bullets.empty()
        self.effects.empty()

    def score(self, score, combo=False):
        """
        Pushes score event to gamescene
        Args:
            score (int): Score to be added
            combo (bool): Score can be combo'd

        Returns:
            None
        """
        self.observer.add_score(score, combo)
        return
