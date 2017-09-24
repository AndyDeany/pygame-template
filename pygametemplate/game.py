from __future__ import absolute_import


import os
import sys
import ctypes
import traceback
import datetime
import time

import pygame
try:
    import pygame._view     # sometimes necessary. If it isn't this will cause an error
    #! UPDATE: this might only be necessary for py2exe to work, so if you can
    # compile without it, then there's no need to import pygame_view whatsoever
except ImportError:
    pass

from pygametemplate.exceptions import CaughtFatalException
from pygametemplate.system import System
from pygametemplate.helper import Helper
from pygametemplate.console import Console
from pygametemplate.userinput import Input
from pygametemplate.hotkey import Hotkey
from pygametemplate.text_input import TextInput


class Game(object):
    def __init__(self, resolution, mode="windowed"):
        self.directory = os.getcwd()

        try:
            pygame.init()
            self.pygame = pygame
        except Exception:
            self.log("Failed to initialise pygame")
        self.system = System(self)
        self.width, self.height = resolution
        self.mode = mode
        self.initialise_screen()
        pygame.display.set_caption("insertnamehere (Alpha 1.0)")
        #! pygame.display.set_icon(self.load_image("icon_name", file_extension=".ico"))

        self.current = "main menu"
        self.fps = 60
        self.frame = 0  # The current frame the game is on (since the game was opened)

        self.input = Input(self)
        self.helper = Helper(self)
        self.console = Console(self)

        self.quit_condition = Hotkey(self, "f4", alt=True).pressed

    def logic(self):
        raise NotImplementedError

    def draw(self):
        raise NotImplementedError

    def quit(self):
        raise NotImplementedError

    def _logic(self):
        self.check_quit()
        self.console.logic()
        self.logic()

    def _draw(self):
        self.screen.fill((0, 0, 0))
        self.draw()
        self.console.draw()

    def _quit(self):
        self.quit()
        pygame.quit()

    def path_to(self, *path):
        """Returns the complete absolute path of the path given."""
        return os.path.join(self.directory, *"/".join(path).split("/"))

    def log(self, *error_message, **options):
        """Takes 1 or more variables and concatenates them to create the error message."""
        fatal = options.get("fatal", True)  # `fatal` option defaults to True
        error_message = "".join(map(str, error_message))
        try:
            with open(self.path_to("log.txt"), "a") as error_log:
                error_log.write("%s - %s.\n" % (datetime.datetime.utcnow(), error_message))
                error_log.write(traceback.format_exc() + "\n")
        except Exception:
            error_info = "This error occurred very early during game initialisation and could not be logged"
        else:
            error_info = "Please check log.txt for details"

        if fatal:
            text = "".join(("An error has occurred:\n\n    ",
                            error_message, ".\n\n\n",
                            error_info, "."))
            ctypes.windll.user32.MessageBoxA(0, text, "Error", 0)   # Error popup
            raise CaughtFatalException(sys.exc_info()[1])
        else:
            pass    #! Add some code here to show an error message in game

    def initialise_screen(self, resolution=None, mode=None):
        """(Re)initialises the screen using the given arguments."""
        try:
            if resolution is None:
                resolution = (self.width, self.height)
            if mode is None:
                mode = self.mode
            flags = pygame.HWSURFACE | pygame.DOUBLEBUF
            if mode == "fullscreen":
                flags |= pygame.FULLSCREEN
            elif mode == "windowed":
                os.environ["SDL_VIDEO_CENTERED"] = "1"
            elif mode == "borderless":
                os.environ["SDL_VIDEO_WINDOW_POS"] = "0,0"
                flags |= pygame.NOFRAME
            else:
                raise ValueError("Unknown mode for reinitialise_screen(): \" %s \"" % mode)

            self.screen = pygame.display.set_mode(resolution, flags)
            self.width, self.height = resolution
            self.mode = mode
        except Exception:
            self.log("Failed to reinitialise screen in ", mode, " mode "
                     "at ", self.width, "x", self.height, " resolution")

    # Asset loading
    def load_image(self, image_name, fade_enabled=False, file_extension=".png"):
        """fade_enabled should be True if you want images to be able to fade"""
        try:
            #! Add stuff for loading images of the correct resolution
            # depending on the player's resolution settings
            if not fade_enabled:
                return pygame.image.load(
                    self.path_to("assets/images", image_name + file_extension)
                    ).convert_alpha()   # Fixes per pixel alphas permanently
            else:
                return pygame.image.load(
                    self.path_to("assets/images", image_name + file_extension)
                    ).convert()
        except Exception:
            self.log("Failed to load image: ", image_name, file_extension)

    def load_font(self, font_name, font_size, file_extension=".ttf"):
        try:
            return pygame.font.Font(
                self.path_to("assets/fonts", font_name + file_extension), font_size
                )
        except Exception:
            self.log("Failed to load font: ", font_name, file_extension)

    def display(self, image, coordinates, area=None, special_flags=0):
        """Takes coordinates and area for a 1920x1080 window"""
        try:
            x_scale = self.width/1920.0
            y_scale = self.height/1080.0
            coordinates = (coordinates[0]*x_scale, coordinates[1]*y_scale)
            if area is not None:
                area = (area[0]*x_scale, area[1]*y_scale,
                        area[2]*x_scale, area[3]*y_scale)
            self.screen.blit(image, coordinates, area, special_flags)
        except Exception:
            self.log("Failed to display image at ", coordinates)

    def inputs(self):
        self.input.reset()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEMOTION:
                self.input.mouse_pos = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.input.buttondown(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.input.buttonup(event.button)
            elif event.type == pygame.KEYDOWN:
                self.input.buttondown(event)
                TextInput.receive_single_characters(event)
            elif event.type == pygame.KEYUP:
                self.input.buttonup(event.key)
        TextInput.receive_multiple_characters()

    def update(self):
        self.frame += 1
        try:
            pygame.display.flip()   # Updating the screen
            self.clock.tick(self.fps)    # [fps] times per second
        except Exception:
            self.log("Failed to update screen")

    def runtime(self):
        try:
            return time.time() - self.start_time
        except Exception:
            self.log("Failed to calculate and return game run time")

    def check_quit(self):
        if self.quit_condition():
            self.running = False

    def run(self):
        self.running = True
        try:
            self.clock = pygame.time.Clock()
            self.start_time = time.time()
        except Exception:
            self.log("Failed to initialise essential time related display variables")

        while self.running:
            self.inputs()
            self._logic()
            self._draw()
            self.update()

        self._quit()