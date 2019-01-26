# Encoding * utf-8 *
"""
Module namespace for custom user input events

This package itself should serve as a singleton namespace for event buffering and io.
This provides the core foundation of the structure



*Event: the custom user input wrapper object
*EventHandler: EventHandler object
*Global get(), poll_button(), handlers for singleton usage
"""
import pygame as pg
import inputhandler.event as event
Event = event.Event


class EventHandler:
    """
    Event Manager class is a wrapper that initializes the Pygame Events -> Custom Event Keys
    Should work like pygame Events does

    Args:
        key_map (dict[str, pg.event]): Mapping of custom event types to Pygame event types

    Attributes:
        buttons (list[str]): List of custom user Event types that this object produces
        inputs (list[pg.event]): List of pygame events that map to user events
        key_map (dict[pg.event, str]): Dictionary of pygame events to custom event codes
        Todo: add the inverse of key_map, custom events -> list<pg.event>
    """

    def __init__(self, key_map):
        self.buttons = [k for k in key_map]  # Note QUIT is a special type here
        self.key_map = dict()
        self.inputs = list()
        self.key_pressed = dict()
        # Initialize allows for multiple keys to map to commands
        for custom in key_map:
            for pygame_key in key_map[custom]:
                self.key_map[pygame_key] = custom
        # Here for polling
        for button in self.buttons:
            self.key_pressed[button] = False
        # for python _pressed method
        # Sets values we are allowed to have as input
        self.inputs = list(self.key_map.keys())
        return

    def get(self) -> list:
        """
        Get all events since last call

        This is just a wrapper for pg.event.get() that should return the custom user events

        Returns:
            list[Event]: List of custom user events
        """
        event_list = []
        for event in pg.event.get():
            if event.type == pg.QUIT:
                event_list.append(Event("QUIT", False))
            elif event.type == pg.KEYDOWN and (event.key in self.inputs):
                key = self.key_map[event.key]
                event_list.append(Event(key, True))
                self.key_pressed[key] = True
            elif event.type == pg.KEYUP and (event.key in self.inputs):
                key = self.key_map[event.key]
                event_list.append(Event(key, False))
                self.key_pressed[key] = False
        return event_list

    def poll_button(self, button) -> bool:
        """
        Check if key is pressed down

        Regularly call get to access this
        Todo: Generalize this so I can make calls to Joystick as well

        Args:
            button: Button to poll

        Returns:
            bool: True if Key is pressed down, False is key is up
        """
        return self.key_pressed[button]


