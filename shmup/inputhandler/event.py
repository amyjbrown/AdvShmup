# encoding: * utf - 8 *
"""
Event request object
"""

class Event:
    """
    Custom event container class

    Attributes:
        key (str): name of event type
        down (bool): True if this was a down button event
        up (bool): True if up button event

    Args:
        key(str): name of event type
        down (bool): True if event was downpress
    """
    def __init__(self, key, down):
        self.key = key
        self.down = down
        self.up = not down

    def __repr__(self):
        return "<Event {}: {}>".format(self.key, "Down" if self.down else "Up")
