# Encoding * utf-8 *
"""
This serves as the singleton event access module

Before any player input handling call setup(..) with appropriate args, otherwise an error will raise
Inversion of Control - if passed None, the setup with work via normal PyGame event.

Attributes:
    _setup_flag (bool): flag is setup() hasn't been called
    default_flag (bool): flag True is standard pygame library is to be used
    _handler (InputHandler_t): EventHandler object to be used globally
"""
import pygame as pg
import inputhandler.inputhandler as inputhandler

# Define Globals
_setup_flag = False
default_flag = None
_handler = None
# Do setup here, I feel this is probably harmless
pg.init()


def setup(key_map=None):
    """
    Setup EventHandler context for global use

    This method must be called before any global

    Args:
        key_map (dict[str, pg.event], None): keymapping of events used for custom EventHandler
            if None, then pygame's default event stream is sued

    Returns:
        None
    """
    global _setup_flag, default_flag, _handler
    if key_map is not None:
        _handler = inputhandler.EventHandler(key_map)
        _setup_flag = True
        default_flag = False
    else:
        _setup_flag = True
        default_flag = True


def get():
    """
    Get all user events since last call

    This is a wrapper for pg.event.get() around the current EventHandler

    Returns:
        list[Event]: list of custom user events

    Raises:
        RuntimeError: If called before setup()
    """
    if not _setup_flag:
        raise RuntimeError("Event Handling was not initialized before calling get()")
    if not default_flag:
        return _handler.get()


def pump():
    """
    Pump and auto-_handler events

    pg.event.pump wrapper

    Returns:
        None

    Raises:
        RuntimeError: If called before setup()
    """
    if not _setup_flag:
        raise RuntimeError("Event Handling was not initialized before calling pump()")
    pg.event.pump()


def poll_button(key):
    """
    Poll individual button
    Args:
        key:

    Returns:
        bool: True is key is pressed down, False otherwise

    Raises:
        RuntimeError: If called before setup()
        ValueError: if pygame event is used while custom event handling is setup, or custom event key if standard
            pygame handling is setup
    """
    return _handler.poll_button(key)