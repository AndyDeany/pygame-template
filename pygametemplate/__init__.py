"""pygametemplate module for making creating games with Pygame easier."""
from __future__ import absolute_import


__version__ = "0.4.0"

__url__ = "https://github.com/AndyDeany/pygame-template"
__download_url__ = "{}/archive/v{}.tar.gz".format(__url__, __version__)

__author__ = "Andrew Dean"
__author_email__ = "oneandydean@hotmail.com"


from pygametemplate.core import log, load_image, load_font
from pygametemplate.game import Game
from pygametemplate.view import View
