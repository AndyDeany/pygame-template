import os
import ctypes
import datetime
import time

import pygame
try:
    import pygame._view     # sometimes necessary. If it isn't this will cause an error
    #! UPDATE: this might only be necessary for py2exe to work, so if you can
    # compile without it, then there's no need to import pygame_view whatsoever
except ImportError:
    pass

from system import System
from console import Console


class Game(object):
    def __init__(self):
        self.directory = os.path.dirname(os.getcwd())
        self.error = "Details unknown"  # Default error message

        try:
            pygame.init()
        except Exception as self.error:
            self.log("Failed to initialise pygame")
        self.system = System(self)
        self.width = self.system.MONITOR_WIDTH
        self.height = self.system.MONITOR_HEIGHT
        #! Decide how the window should be when the game opens. Fullscreen? Borderless? Windowed?
        # How big should it be? User's monitor dimensions? Something else?
        self.initialise_screen((1280, 720), "windowed")
        pygame.display.set_caption("insertnamehere (Alpha 1.0)")
        #! pygame.display.set_icon(self.load_image("icon_name.ico"))

        self.current = "main menu"
        self.fps = 60
        self.frame = 0  # The current frame the game is on (since the game was opened)

        self.console = Console(self)


    def path_to(self, *path):
        """Returns the complete absolute path of the path given."""
        return os.path.join(self.directory, *"/".join(path).split("/"))

    def log(self, *error_message):
        """Takes 1 or more strings and concatenates them to create the error message."""
        def error_popup(error_info):
            ctypes.windll.user32.MessageBoxA(
                0,
                "".join(("An error has occurred:\n\n    ",
                         error_message, ".\n\n\n",
                         error_info, ".")),
                "Error",
                1
                )

        try:
            error_message = "".join(map(str, error_message))
            with open(self.path_to("log.txt"), "a") as error_log:
                error_log.write("".join((
                    str(datetime.datetime.utcnow())[0:19], " - ",
                    error_message, ": ",
                    str(self.error), " (", self.error.__class__.__name__, ")\n"
                    )))
            self.error = "Details unknown"  # Resetting to default value
        except:    # Likely only when file_directory has not yet been defined
            error_popup("This error occurred very early during"
                        "game initialisation and could not be logged")
            raise
        #! Add some code here to show a message in game instead of
        # force quitting the game unless the error is sufficiently bad.
        # fatal_error (below) should depend on this code,
        # or it can be passed in to log() as a argument.
        fatal_error = True
        if fatal_error:
            error_popup("Please check log.txt for details")
            raise

    def initialise_screen(self, resolution=(0, 0), mode="fullscreen"):
        """(Re)initialises the screen using the given arguments."""
        try:
            flags = pygame.HWSURFACE | pygame.DOUBLEBUF
            if mode == "fullscreen":
                flags = flags | pygame.FULLSCREEN
            elif mode == "windowed":
                # Positioning the window in the centre of the screen
                os.environ['SDL_VIDEO_WINDOW_POS'] = "".join((
                    str((self.system.MONITOR_WIDTH - resolution[0])/2), ",",
                    str((self.system.MONITOR_HEIGHT - resolution[1])/2)
                    ))
            elif mode == "borderless":
                os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
                flags = flags | pygame.NOFRAME
            else:
                raise ValueError("".join((
                    "Unknown mode for reinitialise_screen(): \"", mode, "\""
                    )))

            self.screen = pygame.display.set_mode(resolution, flags)
            self.width, self.height = resolution
        except Exception as self.error:
            self.log("Failed to reinitialise screen in ", mode, " mode "
                     "at ", self.width, "x", self.height, " resolution")

    # Asset loading
    def load_image(self, image_name, fade_enabled=False):
        """fade_enabled should be True if you want images to be able to fade"""
        try:
            #! Add stuff for loading images of the correct resolution
            # depending on the player's resolution settings
            if not fade_enabled:
                return pygame.image.load(
                    self.path_to("assets/images", image_name + ".png")
                    ).convert_alpha()   # Fixes per pixel alphas permanently
            else:
                return pygame.image.load(
                    self.path_to("assets/images", image_name + ".png")
                    ).convert()
        except Exception as self.error:
            self.log("Failed to load image: ", image_name, ".png")

    def load_font(self, font_name, font_size):
        try:
            return pygame.font.Font(
                self.path_to("assets/fonts", font_name + ".ttf"), font_size
                )
        except Exception as self.error:
            self.log("Failed to load font: ", font_name, ".ttf")

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
        except Exception as self.error:
            log("Failed to display image at ", coordinates)


