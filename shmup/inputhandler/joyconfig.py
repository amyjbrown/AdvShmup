# encoding: * utf - 8 *
"""
Querrying interfaces for joysticks to virtual buttons
*VAxis: Virtual Axis output
*VHat: Virtual had button
*VButton: Virtual button handling
"""
import pygame as pg


class VAxis:
    """
    Virtual Axis querrying

    Attributes:
        joy (pg.Joystick): referene to Joystick object to querry
        axis (int): hardware axis to check
        high (str): Token for when axis > tolerance
        low (str): Token for when axis < - tolerance
        tolerance (float): Positive value [0,1] that used for querrying if a button should be pushed up or down
            High := (tolerance, 1], Low := [-1, -tolerance)
    """
    def __init__(self, joy, axis, high, low, tolerance = 0.5):
        self.joy = joy
        self.axis = axis
        self.high, self.low = high, low
        self.tolerance = tolerance

    def get(self):
        if self.joy.get_axis(self.axis) > self.tolerance:
            return self.high
        elif self.joy.get_axis(self.axis) < -1 * self.tolerance:
            return self.low
        else:
            return None

class VHat:
    """
    Virtual hat -> button interface
    """
    def __init__(self, joy, id, up, down, left, right):
        self.joy = joy
        self.id = id
        self.up, self.down, self.left, self.right = up, down, left, right


class VButton:
    """
    Virtual Button query object

    Attributes:
        joy (pg.Joystick): reference to joystick to check
        button (list<int>): list of hardware references to querry
        mapping (str): token identifier of virtual button
    """

    def __init__(self,joy, button, mapping):
        self.joy = joy
        self.button = button
        self.mapping = mapping

    def get(self):
        """
        Get state of virtual buttons

        Returns:

        """
        for b in self.button:
            if self.joy.get_button(b):
                return True
        else:
            return False
