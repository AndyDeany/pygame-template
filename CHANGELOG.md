# Changelog

## 0.3.0

* Change `_inputs()`, `_update()` and `_check_quit()` to be "private" methods
of the `Game` class by prepending an underscore to their names.

* Add `toggle_fps_hotkey` parameter to `Console.__init__()`
(defaults to `ctrl+f`) so that it can be customised.

* Add 1280x720 as the default window resolution if one isn't passed in.

## 0.2.0

* Add Python 3 support.

* Create the `pygametemplate.exceptions` module and move `CaughtFatalException` there.
This module will contain all exceptions added from now on.
