# encoding * utf - 8 *
"""
High level entity control and management

*EntityHandler: Handler component for entities to be used in a scene
*hitbox_check: callback function for custom Actor type's hitboxes
TODO: Fully Implement EntityHandler
"""
import pygame as pg


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
        pass

    def draw(self, screen):
        # TODO: Implement
        pass

    def kill(self):
        """
        Kills all on screen entities

        Returns:
            None
        """
        # Todo implement
        pass

    def score(self, score, combo=False):
        """
        Pushes score event to gamescene
        Args:
            score (int): Score to be added
            combo (bool): Score can be combo'd

        Returns:
            None
        """
        self.observer.score()
        return