from spec.helper import *

from pygame import Surface

from pygametemplate import Image


with description("pygametemplate.Image"):
    with it("should initialise correctly, without loading a Surface object"):
        self.image = Image("test")
        expect(self.image.name).to(equal("test"))
        expect(self.image.image).to(be(None))

    with it("should be able to load its image Surface into RAM"):
        self.image.load()
        expect(self.image.image).to(be_a(Surface))

    with it("should be able to unload its image Surface from RAM"):
        self.image.unload()
        expect(self.image.image).to(be(None))

    with it("should load its Surface if .display() is called on it"):
        self.image.display(game.screen, (0, 0))
        expect(self.image.image).to(be_a(Surface))
