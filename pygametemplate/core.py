"""Module containing the core functions of pygametemplate."""
import os
import sys
import traceback
from datetime import datetime
from ctypes import windll

from pygametemplate.exceptions import CaughtFatalException


PATH = os.getcwd()


def path_to(*path):
    """Returns the complete absolute path of the path given."""
    return os.path.join(PATH, *"/".join(path).split("/"))


LOG_FILE = path_to("log.txt")

def log(*error_message, fatal=True):
    """Takes 1 or more variables and concatenates them to create the error message."""
    error_message = "".join(map(str, error_message))
    with open(LOG_FILE, "a") as log_file:
        log_file.write("{} - {}.\n".format(datetime.utcnow(), error_message))
        log_file.write(traceback.format_exc() + "\n")

    if fatal:
        text = ("An error has occurred:\n\n    {}.\n\n\n"
                "Please check log.txt for details.").format(error_message)
        windll.user32.MessageBoxW(0, text, "Error", 0)
        raise CaughtFatalException(sys.exc_info()[1])
    else:
        pass    # TODO: Add some code here to show an error message in game


# Asset loading
def load_image(image_name, fade_enabled=False, file_extension=".png"):
    """fade_enabled should be True if you want images to be able to fade"""
    try:
        #! Add stuff for loading images of the correct resolution
        # depending on the player's resolution settings
        if not fade_enabled:
            return pygame.image.load(
                path_to("assets/images", image_name + file_extension)
            ).convert_alpha()   # Fixes per pixel alphas permanently
        else:
            return pygame.image.load(
                path_to("assets/images", image_name + file_extension)
            ).convert()
    except Exception:
        log("Failed to load image: ", image_name, file_extension)


def load_font(font_name, font_size, file_extension=".ttf"):
    try:
        return pygame.font.Font(
            path_to("assets/fonts", font_name + file_extension), font_size
        )
    except Exception:
        log("Failed to load font: ", font_name, file_extension)
