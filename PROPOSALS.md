# Pygame template proposals

## Patch

* Don't pass `game` to classes which don't use it.

* Fix pylint issues.

* When `Game.switch_view()` is called, the rest of the method in
which it is called is probably still run. This shouldn't be how it
works - switching view should be a breaking action somehow.
Might just end up being expecting people to use
`return self.game.switch_view()` though...


## Minor

* Remove `Game().pygame` member if possible and just import pygame where needed.

* Add a `core.load_video()` method.

* Add a `core.load_sound()` method.

* Add `pygametemplate.Video` class to match `pygametemplate.Image`.
This cannot use `pygame.movie` as it has been deprecated (and removed) from pygame.
It will have to somehow be created using images and sounds instead.

* Rename `Button.pressed` to `Button.is_pressed`? Same with `.held` and `.released`.
`is_released` sounds a bit weird though, maybe `was_released`?
It makes more sense, even if it's less uniform.

* If `self.game.screen` is used a lot in `View` classes,
add a `self.screen = game.screen` to `View.__init__()`,
so that `self.game.screen` can be referred to as `self.screen`.

* Possibly remove `load_image()` and move the code to `Image.load()`.
Is there a reason to ever use `load_image()` over the `Image` class?
`pygame.image.load(icon).convert()` can be used in `Game.__init__()`
for icon loading, as this is the only real place an image file is used
for something other than blitting to a surface.


## Major

There are currently no major proposals.
