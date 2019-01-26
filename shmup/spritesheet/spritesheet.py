# encoding * utf - 8 *
"""
Spritesheet class used for quickly loading in Assets from individual Spritesheet

todo: transparency loading more clear
todo: make method parameters more clear, use transparent for color_key flagging
todo: change logic so calling a function with transparent != has_colorkey changes colorkey on
"""
import sys, os
import pygame as pg


class Spritesheet:
    """
    Spritesheet class for loading large images and loading individual sprites or lists of sprites

    Args:
        filename (str, path): Path to select base image
        colorkey (bool): check to true to use the colorkey at (0,0)
            TODO: Make a potentially more expandable interface

    Raises:
         pg.error: Raised if Pygame display hasn't been initialized
         OSError: Raised if filename invalid
    """
    def __init__(self, filename, colorkey):
        try:
            self.sheet = pg.image.load(filename).convert()
        except pg.error:
            raise RuntimeError("Pygame display has not yet been intialized")
        except OSError:
            raise RuntimeError("Path: {} is invalid".format(filename))
        finally:
            self.has_key = colorkey
            self.colorkey = self.sheet.get_at((0, 0))

    @property
    def size(self):
        """Returns the width and height of underlying sheet"""
        return self.sheet.get_size()

    def get_sheet(self, colorkey=True):
        """Get the core sheet as one image

        Args:
            colorkey (bool): Use default colorkey

        Return:
            pg.Surface with optional transparency
        """
        im = self.sheet.copy()
        if colorkey and self.has_key:
            im.set_colorkey(self.colorkey)
        elif colorkey:
            im.set_colorkey(
                im.get_at((0, 0))
            )
        return im

    def get_image(self, rectangle, colorkey=True) -> pg.SurfaceType:
        """
        Clip and return an image from the sheet

        Args:
            rectangle (pg.Rect): Rectangle of sample area
            colorkey (bool): If True use the default colorkey if there is one

        Returns:
            pg.Surface of Image at Rect, optional to colorkey transparency
        """
        rect = pg.Rect(rectangle)
        image = pg.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey and self.has_key:
            image.set_colorkey(self.colorkey)
        elif colorkey:
            image.set_colorkey(
                image.get_at((0, 0))
            )
        return image

    def get_list(self, *rects, colorkey=True) -> list:
        """
        Get series of clipped images

        Args:
            *rects (pg.Rect): series of Rects to clip from
            colorkey (True): Use default colorkey transparency

        Returns:

        """
        return [self.get_image(rect, colorkey) for rect in rects]

    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey=True) -> list:
        """
        Makes a list of every rect-sizes image in one horizontal strip
        Will not work
        :param rect: Size of individual image
        :param image_count: number of images to load
        :param colorkey: Colorkey param to be passed to get_list()
        :return: List of Surfaces
        """
        tups = [pg.Rect(rect.x + rect.w * i, rect.y, rect.w, rect.h)
                for i in range(image_count)]
        return self.get_list(*tups, colorkey=colorkey)

    def full_load(self, size, colorkey=True) -> list:
        """
        Loads a standard, fullsize colorsheet

        Args:
            size (tuple<int, int>): Size of grid interval in (width, height)
            colorkey (bool): If True, use default colorkey

        Returns:
            list<pg.Surface> list of all surface elements
        """
        canon_rect = pg.Rect((0, 0), size)
        w, h = size
        m, n = self.size
        rects = list()
        for j in range(m // w):  # for Y in ROWS
            for i in range(n // h):  # for X in COLUMNS
                rects.append(canon_rect.move(w * j, h * i))
        return [self.get_image(r, colorkey) for r in rects]
