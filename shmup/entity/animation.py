# encoding * utf - 8 *
"""
Animation component and entities
*Animation: Basic structure of an animation
*AnimComp: Animation mixin for various entity objects

TODO: Figure out structure

Basic idea:
Animation {Identifier, list[Images], *args}: e.g. default, stop, cycle
"""
import pygame as pg


class Animation(pg.sprite.Sprite):
    """
    Animated effect that cycles

    Unlike other sprite extensions, I want this to be able to load and run arbitrary animations


    Args:
        position (tuple<int, int> | pg.Vector): Starting position of animation
        frames (list<pg.Surface>): List of animation frames
        *groups (pg.Group): Groups for element to be added to
        fps (int): Frames per second, default 30 so keyword I can experiment with
        cycle (bool): False if should self delete on completion, true if should be recurring

    Attributes:
        frames (list<pg.Surface>): List of pygame surfaces
        cycle_length (int): length of animation cycle
        current_frame (int): index of current frame
        counter (float): counter til next frame
        FPS (float): frames per second
        rect (Rect): Rect of image location for rendering
    """
    def __init__(self,
                 position,
                 frames,
                 *groups,
                 fps=30,
                 cycle=False,
                 ):
        super().__init__(*groups)
        self.frames = frames
        self.current_frame = 0
        self.cycle_length = len(frames)
        self.counter = fps
        self.rect = pg.Rect(
            *position,
            frames[0].get_size(),
        )
        self.cycle = cycle
        return

    @property
    def image(self):
        """Get current frame"""
        return self.frames[self.current_frame]

    def update(self, dt):
        self.counter -= dt
        if self.counter >= 0:
            self.current_frame += 1
            if self.cycle:
                pass
        self.counter = 0.0


class AnimComp:
    """Mixin for Actors to do Animation

    Attributes:
        frame (int): Current index of animation frame
        anima_state (str): Animation State name
        timer (float): timer of how many frames are spent on frame
        FPS (float): Frames per second
    """

    @property
    def image(self):
        """
        pg.Surface: returns current frame of animation for rendering
        """
        return


def Explosion(position, *groups):
    """

    Args:
        position (tuple<int, int>, Vector2): position explosion should start in
        *groups (Group):

    Returns:

    """