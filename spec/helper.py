from expects import *

from example_view import ExampleView
from pygametemplate import Game

import datetime


class TestGame(Game):
    """An altered Game class for testing purposes."""
    def __init__(self, StartingView, resolution):
        super(TestGame, self).__init__(StartingView, resolution)

    def log(self, *error_message):
        """Altered log function which just raises errors."""
        raise


game = TestGame(ExampleView, (1280, 720))
