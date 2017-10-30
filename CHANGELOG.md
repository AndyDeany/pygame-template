# Changelog

## 0.5.0

**Warning**: This release is broken. Please use `0.6.0` instead.

* [**Backwards incompatible change**]<br>
Replace `core.load_image()`'s `fade_enabled` parameter with a `fix_alphas`
parameter. If you used to pass in `fade_enabled=True`, you should now pass in
`fix_alphas=False`.

* Add `pygametemplate.exceptions.PygameError` as an alias for `pygame.error`.

* Add new `pygametemplate.debug` module with a `DebugConsole` member.
This `DebugConsole` can be initialised in your game code, similar to
`pygametemplate.Console`. The difference here is that this `DebugConsole`
(which can be opened by pressing ` [default]) allows you to type in oneline
Python code which will be executed using `exec()` or, failing this,
evaluated using `eval()`. If this fails too, the original raised exception
will be shown.


## 0.4.1

* Add missing `pygame` import in the `pygametemplate.core` module which
was causing the `load_image()` and `load_font()` functions to throw an error.

* Add unit tests for the `pygametemplate.core` module.

* Make `pygametemplate.core.load_image()` raise `IOError` instead of `pygame.error`
when trying to load an image that can't be found, so that it actually passes unit tests.

* Add `TEST` environment variable functionality.
Set this to `"1"` to indicate that your game is being run by automated tests.
Currently, doing this enables the following behaviour:
    * `core.log()` will reraise the last thrown exception,
    instead of doing `raise CaughtFatalException`.
    This makes it easier to test that your functions/methods raise
    the errors you expect them to, as they will just raise these errors.

    * `core.log()` will not open a popup window on fatal errors.
    This is because interacting with this window from automated tests is very difficult.

## 0.4.0

* [**Backwards incompatible change**]<br>
Move the `path_to()`, `log()`, `load_image()` and `load_font()` methods of
the `Game` class to be functions of a new `pygametemplate.core` module.
`log()`, `load_image()` and `load_font()` are also accessible as direct
members of the `pygametemplate` module.

* [**Backwards incompatible change**]<br>
Remove `pygametemplate.helper.Helper` class and move its methods to
be functions as members of the `pygametemplate.helper` module.
`Game` instances no longer have a `helper` attribute, meaning that all
references to `game.helper.method()` will have to be replaced with
`pygametemplate.helper.method()`.


## 0.3.0

* [**Backwards incompatible change**]<br>
Add the concept of "views" to pygametemplate.
`View`s are classes which represent a "section" of your game.
Every view should inherit from `pygametemplate.View`.
All `View`s have a `self.game` member for accessing the main `Game` instance.
To switch to the next view in your game, you can call `self.game.set_view(NextViewClass)`.
**`pygametemplate.Game` now takes `StartingView` as its first argument.**
`View` classes are expected to implement the following methods:
    * `View.load()`: load all the assets/other things needed for the view to work.
    This means you only load images (for example) into RAM when you need them.

    * `View.unload()`: unload assets that were used by the view,
    but aren't needed after the view is no longer the current view.
    Should mostly do the opposite of what `View.load()` does.

    * `View.logic()`: run the logic for the view.

    * `View.draw()`: run all drawing code for the view.

* Change `_inputs()`, `_update()` and `_check_quit()` to be "private" methods
of the `Game` class by prepending an underscore to their names.

* Add `toggle_fps_hotkey` parameter to `Console.__init__()`
(defaults to `ctrl+f`) so that it can be customised.

* Add 1280x720 as the default window resolution if one isn't passed in.


## 0.2.0

* Add Python 3 support.

* [**Backwards incompatible change**]<br>
Create the `pygametemplate.exceptions` module and move `CaughtFatalException` there.
This module will contain all exceptions added from now on.
