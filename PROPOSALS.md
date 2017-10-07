# Pygame template proposals

## Minor

* Add `pygametemplate.additional` module with `DebugConsole` class.

* `Image` class with `Image.display(pygame.Surface())` method,
along with loading and unloading from RAM.

* Remove silly `try/except` blocks.

## Major

* Remove Python 2 support.
    * Change `IOError`s to `FileNotFoundError` (most of them, at least).
    * Add `encoding="utf-8"` to `open()` calls.
