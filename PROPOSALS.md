# Pygame template proposals

## Minor

* Add `pygametemplate.additional` module with `DebugConsole` class.

* Change `helper.Helper` to be a module instead of a class.

* Move methods of `Game` which don't affect it's state to a module
so that game doesn't need to be passed around? Like file loading maybe.

* `Image` class with `Image.display(pygame.Surface())` method,
along with loading and unloading from RAM.

* `View` classes. `Game` needs a `set_view(View())` method.

* Remove silly `try/except` blocks.

## Major

* Remove Python 2 support
