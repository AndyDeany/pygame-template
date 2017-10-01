from pygametemplate import Game
from example_view import ExampleView


class TestGame(Game):   # TODO: remove this useless class
    """An altered Game class for testing purposes."""
    def __init__(self, StartingView, resolution):
        super(TestGame, self).__init__(StartingView, resolution)


game = TestGame(ExampleView, (1280, 720))
