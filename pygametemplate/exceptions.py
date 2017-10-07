"""Module containing all the exceptions included in the pygametemplate module."""
from pygame import error as PygameError


class CaughtFatalException(Exception):
    """Raised by pygametemplate.core.log() when it catches a fatal exception."""

    pass
