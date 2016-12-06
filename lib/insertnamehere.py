import os, ctypes, datetime # Importing modules that are required for the log function to work

file_directory = os.path.dirname(os.getcwd())   # Obtaining the location of the game files
file_directory = "E:\Users\Andrew\Desktop\lib\insertnamehere\\" #! temp because running with komodo gives wrong path
def log(error_message): # Defining the error logging function
    try:
        error_log = open("".join((file_directory, "log.txt")), "a")
        try:
            error_log.write("".join((str(datetime.datetime.utcnow())[0:19], " - ", error_message, ": ", str(error), "\n")))
        except:
            error_log.write("".join((str(datetime.datetime.utcnow())[0:19], " - ", error_message, ": Details Unknown\n")))
        error_log.close()
    except:    # This will likely happen only when file_directory has not yet been defined
        ctypes.windll.user32.MessageBoxA(0, "".join(("An error has occurred:\n\n    ", error_message, ".\n\n\nThis error occurred very early during game initialisation and could not be logged.")), "Error", 1)
        raise
    #! Add some code here to show a message in game that doesn't force quit the game unless the error is sufficiently bad
    ctypes.windll.user32.MessageBoxA(0, "".join(("An error has occurred:\n\n    ", error_message, ".\n\n\nPlease check log.txt for details.")), "Error", 1)
    raise

def load_image(image_name, fade_enabled=False): # Defining a function to load images
    try:    #! Add stuff for loading images of the correct resolution depending on the player's resolution
        if not fade_enabled:
            return pygame.image.load("".join((file_directory, "Image Files\\", image_name, ".png"))).convert_alpha()
        else:
            return pygame.image.load("".join((file_directory, "Image Files\\", image_name, ".png"))).convert()
    except Exception as error:
        log("".join(("Failed to load image: ", image_name, ".png")))

### ---------- IMPORTING MODULES - START ---------- ###
try:    # Importing and initialising pygame
    import pygame
    try:
        import pygame._view # sometimes necessary. If it isn't this will cause an error
    except Exception, error:
        pass
    pygame.init()
except Exception as error:
    log("Failed to initialise pygame")

try:    # Importing other modules
    import sys
    import datetime, time
    import math, random
except Exception as error:
    log("Failed to import modules")
### ---------- IMPORTING MODULES - END ---------- ###


### ---------- INITIALISING GLOBAL VARIABLES - START ---------- ###
try:    ## Initialising game screen
    screen = pygame.display.set_mode((0,0), pygame.HWSURFACE|pygame.DOUBLEBUF)#|pygame.FULLSCREEN)  # (0,0) defaults to the user's screen size
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    MONITOR_WIDTH = screen_width
    MONITOR_HEIGHT = screen_height
    # Defining a function to change the screen settings after it has been created
    def reinitialise_screen(resolution=(screen_width,screen_height), mode="fullscreen"):
        global error
        try:
            global screen, screen_width, screen_height
            screen_width = resolution[0]
            screen_height = resolution[1]
            if mode == "fullscreen":
                screen = pygame.display.set_mode(resolution, pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
            elif mode == "windowed":
                os.environ['SDL_VIDEO_WINDOW_POS'] = "".join((str((MONITOR_WIDTH - screen_width)/2), ",", str((MONITOR_HEIGHT - screen_height)/2)))
                screen = pygame.display.set_mode(resolution, pygame.HWSURFACE|pygame.DOUBLEBUF)
            elif mode == "borderless":
                os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
                screen = pygame.display.set_mode(resolution, pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.NOFRAME)
            else:
                raise Exception("".join(("Unknown mode for reinitialise_screen(): \"", mode, "\" [syntax error].")))
        except Exception as error:
            log("".join(("Failed to reinitialise screen in ", mode, " mode at ", str(screen_width), "x", str(screen_height), " resolution")))

    #! resolutions = [_list of tuples of available resolutions_]    #! This could all be removed, along with reinitialise_screen, if we decide to have a fixed resolution.
    #! if (MONITOR_WIDTH, MONITOR_HEIGHT) not in resolutions:
    #!      screen_width = 0
    #!      screen_height = 0
    #!      for resolution in resolutions:
    #!          if resolution[0] <= MONITOR_WIDTH:
    #!              if screen_width < resolution[0]:
    #!                  screen_width = resolution[0]
    #!                  screen_height = resolution[1]
    #!              elif screen_width == resolution[0] and resolution[1] <= MONITOR_HEIGHT and screen_height < resolution[1]:
    #!                  screen_height = resolution[1]
    #!
    #!      reinitialise_screen(screen_width, screen_height)

    pygame.display.set_caption("insertnamehere (Alpha 1.0)")
    #! pygame.display.set_icon()    add the path to an image for the icon as the argument
except Exception as error:
    log("Failed to initialise game screen")
## Initialising other global variables
current = "main menu"   # The part of the game the screen is showing
fps = 60
frame = 1
# Keyboard and mouse input related variables
accepting_text = True#!!!  # Showing whether the program is accepting text input from the user
input_text = ""         # The input text from the user
maximum_characters = 50#!!!  # The maximum amount of allowed characters in an input text
def return_key(n):  # Returns the keyboard key with key n.
    return keys[n]  # keys = pygame.key.get_pressed() (should be assigned before this function is called)
character_keys = [n for n in range(44,58)] + [n for n in range(96,123)] + [n for n in range(256,272)] + [39, 59, 60, 61, 91, 92, 93]    # A list of all the keys that can produce characters when pressed
try:
    execfile("reset_inputs.py")
    execfile("input_attributes.py")
except Exception as error:
    log("Failed to initialise keyboard/mouse input variabes")
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
    screen.fill((0,0,0))    #!!
    screen.blit(pygame.font.SysFont("Arial Black", 40, False, False).render(input_text, True, (255,255,255)), (0,0))    #!!
    try: ## Receiving user inputs
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
                if accepting_text:
                    if event.key == 8 and input_text != "":
                        input_text = input_text[:-1]
                    elif event.key == 9:
                        pass    #! This is the TAB key. Perhaps it should make the cursor go to the next box and
                                #! this would be a good place to do it, since it would only be applicable when inputting text.
                                #! The only reason this would be pointless is if there are never two text boxes to fill in on
                                #! the same screen, which isn't that unlikely, so it may actually be pointless.
                    elif event.key == 13:
                        accepting_text = False    # This is the enter key. It will cause the text to be accepted.
                    elif len(input_text) < maximum_characters:
                        input_text = "".join((input_text, event.unicode))
            elif event.type == pygame.KEYUP:
                execfile("keyup.py")
    except Exception as error:
        log("Failed to receive user inputs correctly")

    if accepting_text:
        keys = pygame.key.get_pressed()
        (numlock, capslock) = (keys[300], keys[301])
        execfile("multiple_character_input.py")

    frame += 1
    try:
        pygame.display.flip()   # Updating the screen
        clock.tick(fps)         # [fps] times per second
    except Exception as error:
        log("Failed to update screen")
### ---------- PROGRAM DISPLAY - END ---------- ###

#! Add code for autosaving the game

pygame.quit()

raw_input("Press Enter to Quit")    #! Remove this before compiling. It's only useful for debugging.
