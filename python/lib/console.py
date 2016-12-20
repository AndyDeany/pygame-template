import pygame

class Console(object):
    def __init__(self, game):
        self.game = game
        try:
            self.font = pygame.font.SysFont("consolas", 15)
            self.text_colour = (255, 255, 255)  # white

            self.show_fps = False
            self.fps_coordinates = (game.width - self.font.size("FPS: 000")[0], 0)
        except Exception as game.error:
            game.log("Failed to initialise console object")

    def run(self):
        if self.show_fps:
            self.display_fps

    def display_fps(self):
        self.game.screen.blit(self.font.render(
            "FPS: " + str(int(self.game.clock.get_fps())),
            True, self.text_colour
            ), self.fps_coordinates)
