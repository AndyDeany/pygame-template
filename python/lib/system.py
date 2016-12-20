import pygame

class System(object):
    def __init__(self, game):
        self.game = game
        try:
            display_info = pygame.display.Info()
            self.MONITOR_WIDTH = display_info.current_w
            self.MONITOR_HEIGHT = display_info.current_h
        except Exception as game.error:
            game.log("Failed to initialise system object")
