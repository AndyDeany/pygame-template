# Changelog


## 0.9.0

* Rename `Game.quit()` to `Game.on_quit()` and make it optional to implement.
If you want to add custom functionality, you can now define the `on_quit()`
method on your `Game` subclass.

* Add new `Game.quit()` method which signals the game to exit.

* Add new `Game.get_memory_use() -> int` method which returns the current
memory usage of the game (RSS) in bytes.

* `Game.__init__()` now takes an optional `max_allowed_ram` keyword argument,
which defaults to `1**30` bytes (1GB). Previous views are now cached by the
game and are reused if they're still loaded into RAM. Old views are only
unloaded from RAM if the current RAM usage of the game goes over the maximum
allowed amount.

* `Image.load()` no longer reloads the image if the image is already loaded
when it's called. This means that even if `Image.load()` is called twice
sequentially, the image is only loaded once, saving CPU cycles.


## 0.8.2

* Change `Game.set_view()` to take `view_name: str` instead of
`View: pygametemplate.View`, as taking a `View` class meant that
other `View` classes needed to import each other, which was causing
circular imports, and thus erroring code. This was considered to be a bug as
views could not switch between each other before. `View` classes are now expected
to be members of the `lib.views` module in your project. You can change this
by setting the `VIEW_MODULE` attribute of your `Game` subclass.
Alternatively, you can override the `Game.get_view_class(view_name: str)`
method of your `Game` subclass to have your own custom
view name -> View class conversion functionality.


## 0.8.1

* Fix a bug where using `pygame` functions in your `StartingView`
(passed to `Game.__init__()`) would throw an error saying
`pygame not initialised` or something similar.


## 0.8.0

* Rename the `pygametemplate.game`, `pygametemplate.view`, and `pygametemplate.image`
modules to `_game`, `_view` and `_image` respectively.
These modules shouldn't be imported from anyway, as their members
are available as direct members of `pygametemplate`.

* `pygametemplate.load_image()` now expects the name of the image file
**including** the file extension, not excluding it, as was the case before.
The same goes for `pygametemplate.Image.__init__()`,
and for the `icon` argument of `pygametemplate.Game`.


## 0.7.0

* `pygametemplate.Game.__init__()` now optionally takes
`caption` and `icon` arguments.
	* `caption` specifies the caption (window title) at the top of the game window.

	* `icon` should be the name of a `.ico` file
	which will be used as the game window's icon.
	For example, if you have a `assets/images/tree.ico` file,
	you would pass in `icon="tree"`.
	These must be passed in as keyword arguments.

* There is now a new `pygametemplate.Image` class,
which helps with keeping RAM taken by images in check.
Instances of `Image` have the following methods:
	* `Image.__init__(image_name)`: Takes the name of the image.
	For example, if your image file is `assets/images/heart.png`,
	pass in `"heart"`.

	* `Image.load()`: Load the image's `pygame.Surface` object into RAM.
	Minimal RAM will be used before this method is called.

	* `Image.unload()`: Unload the image's `pygame.Surface` object from RAM.
	This will clear up almost all usage of RAM by the `Image` instance.

	* `Image.display(surface: pygame.Surface, coordinates, area=None, special_flags=0)`:
	Display the image on the given `surface`. The arguments other than `surface`
	are the same as the arguments passed to `pygame.Surface.blit()`.


## 0.6.1

* Remove some silly `try`/`except` blocks.
This means that fewer `pygametemplate.CaughtFatalException`s will be raised,
as the actual raised exceptions will be raised in their place.

* Add some missing docstrings and function annotations.


## 0.6.0

First pypi release.

* [**Backwards incompatible change**]<br>
Remove Python 2 support.

* [**Backwards incompatible change**]<br>
`Console.__init__()`'s `toggle_fps_hotkey` argument must now be passed in as a keyword.

* `pygametemplate.core.load_image()` now raises a `FileNotFoundError` instead
of an `IOError` when an image file with the given name can't be found.


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
