# Pygame template proposals

## Patch

* Don't pass `game` to classes which don't use it.

* Add `.pylintrc` file and fix issues.


## Minor

* Remove `Game().pygame` member if possible and just import pygame where needed.

* Possibly remove `load_image()` and move the code to `Image.load()`.
Is there a reason to ever use `load_image()` over the `Image` class?

## Major

There are currently no major proposals.
