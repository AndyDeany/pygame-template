# Importing modules that are required for the error logging function to work
import os
import ctypes
import datetime

# Obtaining the location of the game files
file_directory = "".join((os.path.dirname(os.getcwd()), "\\"))

# Defining functions for logging errors
execfile("error_logging.py")

# Defining functions for loading assets such as images, videos, sounds etc.
execfile("asset_loading.py")

### ---------- IMPORTING MODULES - START ---------- ###
try:    # Importing and initialising pygame
    import pygame
    try:
        import pygame._view     # sometimes necessary. If it isn't this will cause an error
        #! UPDATE: this might only be necessary for py2exe to work, so if you can
        # compile without it, then there's no need to import pygame_view whatsoever
    except Exception:
        pass
    pygame.init()
except Exception as error:
    log("Failed to initialise pygame")

try:    # Importing other modules
    import sys
    import time
    import math
    import random
except Exception as error:
    log("Failed to import modules")
### ---------- IMPORTING MODULES - END ---------- ###


### ---------- INITIALISING GLOBAL VARIABLES - START ---------- ###
try:    # Initialising game screen
    screen = pygame.display.set_mode(
        (0, 0),     # (0, 0) resolution defaults to the user's screen size
        pygame.HWSURFACE | pygame.DOUBLEBUF     #!|pygame.FULLSCREEN)
        )
    #! Decide how the window should be when the game opens. Fullscreen? Borderless? Windowed?
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    MONITOR_WIDTH = screen_width
    MONITOR_HEIGHT = screen_height

    # Defining a function to change the screen settings after it has been created
    def reinitialise_screen(resolution=(screen_width, screen_height), mode="fullscreen"):
        global error
        try:
            global screen, screen_width, screen_height
            screen_width = resolution[0]
            screen_height = resolution[1]
            if mode == "fullscreen":
                screen = pygame.display.set_mode(
                    resolution,
                    pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN
                    )
            elif mode == "windowed":
                # Positioning the window in the centre of the screen
                os.environ['SDL_VIDEO_WINDOW_POS'] = "".join((
                    str((MONITOR_WIDTH - screen_width)/2), ",",
                    str((MONITOR_HEIGHT - screen_height)/2)
                    ))
                screen = pygame.display.set_mode(
                    resolution,
                    pygame.HWSURFACE | pygame.DOUBLEBUF
                    )
            elif mode == "borderless":
                os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
                screen = pygame.display.set_mode(
                    resolution,
                    pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.NOFRAME
                    )
            else:
                raise Exception("".join(("Unknown mode for reinitialise_screen(): \"", mode, "\" "
                                         "[syntax error].")))
        except Exception as error:
            log("".join(("Failed to reinitialise screen in ", mode, " mode "
                         "at ", str(screen_width), "x", str(screen_height), " resolution")))

    #! This (below) could all be removed, along with reinitialise_screen,
    # if you decide to have a fixed resolution.
    # resolutions = [_list of tuples of available resolutions_]
    # if (MONITOR_WIDTH, MONITOR_HEIGHT) not in resolutions:
    #      screen_width = 0
    #      screen_height = 0
    #      for resolution in resolutions:
    #          if resolution[0] <= MONITOR_WIDTH:
    #              if screen_width < resolution[0]:
    #                  screen_width = resolution[0]
    #                  screen_height = resolution[1]
    #              elif (screen_width == resolution[0] and
    #                    resolution[1] <= MONITOR_HEIGHT and
    #                    screen_height < resolution[1]):
    #                  screen_height = resolution[1]
    #
    #      reinitialise_screen(screen_width, screen_height)

    pygame.display.set_caption("insertnamehere (Alpha 1.0)")
    #! pygame.display.set_icon()    add the path to an image for the icon as the argument
except Exception as error:
    log("Failed to initialise game screen")

## Initialising other global variables
current = "main menu"   # The part of the game the screen is showing
fps = 60
frame = 1   # The current frame the game is on (since the game was opened)
try:    # Creating variables for keyboard and mouse inputs
    execfile("reset_inputs.py")
    execfile("input_attributes.py")
except Exception as error:
    log("Failed to initialise keyboard/mouse input variabes")
# Text input related variables
execfile("text_input.py")

def return_key(n):
    """Returns the keyboard key with key n in pygame.key.get_pressed()"""
    return keys[n]
# keys = pygame.key.get_pressed(), which should be assigned before this function is called

character_keys = (  # A list of all the keys that can produce characters when pressed
    [n for n in range(44, 58)] +
    [n for n in range(96, 123)] +
    [n for n in range(256, 272)] +
    [39, 59, 60, 61, 91, 92, 93]
    )
### ---------- INITIALISING GLOBAL VARIABLES - END ---------- ###

### ---------- FUNCTION DEFINITIONS - START ---------- ###
def display(image, coordinates, area=None, special_flags=0):
    """Takes coordinates for a 1920x1080 window"""
    try:
        coordinates = (coordinates[0]*(screen_width/1920.0), coordinates[1]*(screen_height/1080.0))
        screen.blit(image, coordinates, area, special_flags)
    except Exception as error:
        log(" ".join(("Failed to display image at", str(coordinates))))
### ---------- FUNCTION DEFINITIONS - END ---------- ###

### ---------- CLASS DEFINITIONS - START ---------- ###
### ---------- CLASS DEFINITIONS - END ---------- ###

### ---------- PROGRAM DISPLAY - START ---------- ###
# Initialising essential display variables
ongoing = True
try:
    clock = pygame.time.Clock()
    start_time = time.time()
except Exception as error:
    log("Failed to initialise essential display variables")
#!!! TEST - REMOVE
TextInput.take_input(50, "test")
#!!! TEST - REMOVE
## Game window while loop
while ongoing:
    try:
        current_time = time.time() - start_time
    except Exception as error:
        log("Failed to update game run time")

    try:
        execfile("reset_inputs.py")
    except Exception as error:
        log("Failed to reset user input values")

    try:
        (mouse_x, mouse_y) = pygame.mouse.get_pos()
    except Exception as error:
        log("Failed to determine mouse position")

    try:
        execfile("input_timer.py")
    except Exception as error:
        log("Failed to calculate key held duration")
    #!!! TEST - REMOVE
    screen.fill((0, 0, 0))
    screen.blit(pygame.font.SysFont(
        "Arial Black", 40, False, False
        ).render(TextInput.text, True, (255, 255, 255)), (0, 0))
    #!!! TEST - REMOVE
    try:    # Receiving user inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # When the user exits the game manually
                ongoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: left_held = 1
                elif event.button == 2: middle_held = 1
                elif event.button == 3: right_held = 1
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    left = 1
                    left_held = 0
                elif event.button == 2:
                    middle = 1
                    middle_held = 0
                elif event.button == 3:
                    right = 1
                    right_held = 0
            elif event.type == pygame.KEYDOWN:
                execfile("keydown.py")
                TextInput.receive_single_characters()
            elif event.type == pygame.KEYUP:
                execfile("keyup.py")
    except Exception as error:
        log("Failed to receive user inputs correctly")

    try:
        TextInput.receive_multiple_characters()
    except Exception as error:
        log("Failed to receive multiple characters for text input correctly")

    frame += 1
    try:
        pygame.display.flip()   # Updating the screen
        clock.tick(fps)         # [fps] times per second
    except Exception as error:
        log("Failed to update screen")
### ---------- PROGRAM DISPLAY - END ---------- ###

#! Add code for autosaving the game

pygame.quit()
