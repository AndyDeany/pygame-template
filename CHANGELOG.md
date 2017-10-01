# Changelog

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
`View` classes are expected to implement the following methods:
    * `View.load(self)`: load all the assets/other things needed for the view to work.
    This means you only load images (for example) into RAM when you need them.

    * `View.unload(self)`: unload assets that were used by the view,
    but aren't needed after the view is no longer the current view.
    Should mostly do the opposite of what `View.load()` does.

    * `View.logic(self)`: run the logic for the view.

    * `View.draw(self)`: run all drawing code for the view.

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
