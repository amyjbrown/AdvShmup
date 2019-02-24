# encoding * utf - 8 *
"""
Scene Base class and Scene Handler
"""


class Scene:
    """
    Base class for scene

    Attributes:
        next (str): Name of next scene
        **next_kwargs (dict): Key word arguements
        do_unload (bool): Boolean for if the scene should unload itself
        final (Bool): Flag for if this is final scene
        loaded (bool): Flag for is assets are loaded and working 'as normal'

    """

    def __init__(self):
        self.next = None,
        self.kwargs = dict()
        self.do_unload = False
        self.final = False
        self.loaded = False

    def load(self, **kwargs):
        """
        Initialize and setup new scene

        Note self.loaded will be False and this should change it

        Args:
            **kwargs: Keyword args for loading

        Returns:
            None
        """
        pass

    def unload(self, **kwargs):
        """
        Shutdown scene and free up resources

        This doesn't really need to be used, but good for saving and deserialize after something changes.
        Must set self.loaded to False

        Args:
            **kwargs: Keyword args for unloading and despawning entities

        Returns:

        """
        pass

    def transition(self, next):
        """
        Updates the state machine to next state

        Args:
            next (str): Name of next scene

        Returns:
            None
        """
        pass

    def handle_input(self, event):
        """
        Parse and handle a single user input

        This will serve as a the foundation of the User interface

        Args:
            event (Event): Event type to be parsed

        Returns:
            None
        """
        pass

    def update(self, dt):
        """
        Updates the simulation

        Args:
            dt (float): Time delta to update the simulation by

        Returns:
            None
        """
        pass

    def draw(self, screen):
        """
        Draw onto the main screen

        Args:
            screen: Screen to draw onto

        Returns:
            None
        """
        pass


class SceneHandler:
    """
    Finite State Automata the delegates Screen work

    Attributes:
        current (Scene): current Scene object
        scenes (dict[str, Scene]): mapping of identifiers to Scene objects
    """

    def __init__(self, scenes, intro):
        self.scenes = scenes
        self.current = self.scenes[intro]
        pass

    def transition(self):
        """
        Transitions SceneHandler to next scene

        todo make it so the game doesn't overload when switchig to next scene

        Args:
            next (str): Code for next scene. If left blank, current scene is checked if ready to transition
                if self.current.next True, then transition happens
            **kwargs: Keyword args for loading an appropriate scene

        Returns:
            None
        """
        if self.current.next is not None:
            new = self.scenes[self.current.next]
            new.load(self.current.kwargs)
            # Check if should unload resources, if so perform shutdown
            if self.current.do_unload():
                self.current.unload()
                self.current.loaded = False
            self.current = new
        return

    def parse_input(self, events):
        """
        Parses all user input since last frame update

        Args:
            *events (list[Event]): list of Events to be parsed by the SceneHandler

        Returns:
            None
        """
        for event in events:
            self.current.handle_input(event)
            self.transition()

    def update(self, dt):
        """
        Updates game by time delta

        Args:
            dt: time delta to update simulation by

        Returns:
            None
        """
        self.current.update(dt)
        self.transition()

    def draw(self, screen):
        """
        Draws current scene onto appropriate Surface

        Args:
            screen (pg.Surface): Surface to be drawn onto

        Returns:
            None
        """
        self.current.draw()
