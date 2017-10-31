# Pygame template proposals

## Patch

* Don't pass `game` to classes which don't use it.

* Fix pylint issues.


## Minor

* Remove `Game().pygame` member if possible and just import pygame where needed.

* Possibly remove `load_image()` and move the code to `Image.load()`.
Is there a reason to ever use `load_image()` over the `Image` class?
`pygame.image.load(icon).convert()` can be used in `Game.__init__()`
for icon loading, as this is the only real place an image file is used
for something other than blitting to a surface.


## Major

There are currently no major proposals.
