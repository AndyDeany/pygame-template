# Pygame template proposals

## Minor

* `Image` class with an `Image.display(surface: pygame.Surface)` method,
along with loading and unloading from RAM.

* Remove `Game().pygame` member if possible and just import pygame where needed.

* Don't pass `game` to classes which don't use it.

* Possibly remove `load_image()` and move the code to `Image.load()`.
Is there a reason to ever use `load_image()` over the `Image` class?

## Major

There are currently no major proposals.
