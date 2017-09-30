from __future__ import absolute_import


from example_game import ExampleGame
from example_view import ExampleView


if __name__ == "__main__":
        game = ExampleGame(ExampleView)
        game.run()
