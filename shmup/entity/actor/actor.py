# encoding * utf-8 *
"""
Contains abstract base for Actor class
"""
import pygame as pg


class Actor(pg.sprite.Sprite):
    """
    Active game entity base class

    This serves both as a generic interface for game actors, and as some basic functions that shouldn't need to be
    overloaded, e.g. _move(). This also doesn't define certain advanced properties, like animation, which is instead a
    mixin that replaces some of the entity

    Note:
        When creating a new Actor entity in a gamespace, do:
        > Actor(position, group1, group2,,,); .e.g.:
        > Swarmer((10, 10), enemy_group, render_group,,,)
        This may look strange, but is the default pygame sprite behavior: the constructor acts as a spawning function
        as well.

    Args:
        position (List[float, float], pg.Vector2): Starting position of sprite
            May be either list<float>, tuple<float>, or pg.Vector2
        *groups: Groups Actor should be added to
            Use observer for group access

    Attributes:
        *STATIC*
        init_flag (bool): True if setup() has been called
        RECT (pg.Rect): Canonical Rect showing size of image of
            (x,y) MUST be zero
        HITBOX (pg.RECT): Canonical rect of hitbox region
            (x,y) should be defined in terms of Rect, thus (5,5) is five pixels down and left from Graphical rect
        MAX_HEALTH (int): Starting and maximum health of an entity
        IMAGE_PATH (str, path): Path to basic image to be used for non-animated entities
        IMAGE (str, path): Static image for reference

        *INSTANCE*
        position (pg.Vector2): Position vector representing current accurate location of actor's top, left corner
            When moving item, update position first!
        velocity (pg.Vector2): Current moving speed of object
            Set velocity to change how character is moving
        rect (pg.Rect): Current screenspace region of sprite, used for rendering
        hitbox (pg.Rect): Current collision detection region of sprite, used for collisions
        image (pg.Surface): Image to be rendered on draw

    Raises:
        pg.Error: Haven't setup
    """
    # Statics
    IMAGE_PATH = str()
    IMAGE = None
    init_flag = False
    HITBOX = None
    RECT = None
    MAX_HEALTH = int()

    def __init__(self, position, *groups):
        if not self.init_flag:
            raise pg.error("Didn't initialize class before calling constructor")
        super().__init__(*groups)
        self.position = pg.Vector2(position)
        self.velocity = pg.Vector2()  # Initialize to zero, unless set otherwise
        self.hitbox = pg.Rect(self.HITBOX)
        self.rect = pg.Rect(self.RECT)
        self.image = pg.Surface(self.IMAGE)
        self.health = self.MAX_HEALTH

    @classmethod
    def setup(cls, observer):
        """
        Initializes static class values for use

        Args:
            observer (Handler): Handler for managing this class

        Returns:
            None
        """
        if not cls.init_flag:
            cls.IMAGE = pg.image.load(cls.IMAGE_PATH).convert()
            cls.init_flag = True
            cls.observer = observer
        return

    def update(self, dt):
        """
        Updates object. Should be overloaded

        Args:
            dt: Time delta

        Returns:
            None
        Raises:
            NotImplemented: if code is not overloaded

        """
        raise NotImplemented("Update wasn't implemented")

    def _move(self, dt):
        """Basic movement update code"""
        dr = dt * self.velocity
        self.position += dr
        self.rect.move_ip(*dr)
        self.hitbox.move_ip(*dr)
        pass

    def collide(self, other, dt):
        """
        Script when colliding with other entity

        Args:
            other (Actor):
            dt (float): time_delta

        Returns:
            None
        """
        pass

    def on_death(self):
        """
        Actions to engage with on death

        Use this for spawning explosions, dropping loot, damaging entities near it

        Returns:
            None
        """