# encoding * utf - 8 *
"""
Scrolling
"""
import pygame as pg
pg.init()


class BackGround:
    """
    Scrolling Background object

    Args:
        background (pg.Surface): Surface holding image
        speed (float): Speed in pixels/frame

    Attributes:
        background (pg.Surface): Surface holding image
        speed (float): Speed in pixels/frame
    """
    def __init__(self,  background, speed):
        self.im = pg.image.load(background).convert()
        self.h = self.im.get_height()
        self.y1 = 0
        self.y2 = -self.h
        self.speed = speed

    def update(self, dt):
        """
        Procedure
        Scrolls the background in the play area
        """
        self.y1 += self.speed * dt
        self.y2 += self.speed * dt
        return

    def draw(self, screen):
        """
        Draws background onto screen and then resets position

        Args:
            screen (pg.Surface): Render Scene

        Returns:

        """
        screen.blit(self.im,
                    (0, self.y1))
        screen.blit(self.im,
                    (0, self.y2))
        if self.y1 > self.h:
            self.y1 = -self.h
        if self.y2 > self.h:
            self.y2 = -self.h
        return


