class Helper(object):
    """Class holding helper functions."""
    def __init__(self, game):
        self.game = game

    def load_class_assets(self, calling_object, assets_dict):
        """Loads class assets. Should only be calling if self.class_assets_loaded is False."""
        try:
            for attribute_name in assets_dict:
                calling_class = calling_object.__class__
                setattr(calling_class, attribute_name, assets_dict[attribute_name])
        except Exception:
            self.game.log("Failed to load ", calling_class.__name__, " class assets")
        setattr(calling_class, "class_assets_loaded", True)
