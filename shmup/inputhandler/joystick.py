# Encoding * utf-8 *
"""
Custom virtual joystick and hat options [EXPERIMENTAL]

This module contains custom joystick and hat wrapper options. Note these do not need to map onto a real joystick, but
instead provide the interface for interacting equivalently, along with the appropriate Factory Methods

*VJoy: Virtual custom Joystick
*VAxis: Virtual custom 1-dimensional axis
*VHat: Virtual hat object
"""
from enum import Enum
import pygame as pg


class BindType(Enum):
    """
    Binding Type enum used for structure
    """
    Mouse = Enum.auto()
    Axis = Enum.auto()
    Hat = Enum.auto()
    QuadButton = Enum.auto()


class VJoy:
    """
    Virtual Joystick Object

    Virtual Joystick Object can accept multiple types of input, as labelled below
    Mouse (None) -> Use relative mouse position for the axis
    Axis (tuple[int, int]): Accepts id of current

    Attributes:
        active_type (BindType): active binding type
        binding (None, dict[str, pg.event], int, tuple[int, int]]: materials that go
    """

    def poll(self):
        """
        Get current state of Virtual Joystick

        Returns:
            Tuple[Float, Float]: Current relative X, Y position of Joystick
                Note the return value has a norm of 1, distinct from a hat
        """
