"""
Core gui loop protoype
*core loop
*Widget / view tree
*other assets
"""
import random
from collections import namedtuple
import pygame as pg
pg.init()
# Screen Size Constants
SCREEN = pg.display.set_mode((300,300))
SCREEN_SIZE = pg.Rect(0, 0, 300, 300)


class Event:
    """EventListener listens and does events"""
    def __init__(self):
        self.listeners = []

    def listen(self, callback):
        """Attaches a callback function to this listener"""
        self.listeners.append(callback)

    def trigger(self):
        """Triggers every listener callback function"""
        for listener in self.listeners:
            listener()
            return


class Button:
    """Button prototype"""
    on_click = Event()

    def __init__(self, scene):
        scene.on_click.listen(self.handle_click)

    def handle_click(self, event):
        """Pushes event up"""
        pass


class Scene:
    def __init__(self):
        self.on_click = Event()
        self.on_key = Event()

inventory_button = Button()